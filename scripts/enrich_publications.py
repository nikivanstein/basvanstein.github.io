#!/usr/bin/env python3
"""Add authors, DOI, arXiv id, PDF link and abstract to publication pages.

Usage (from the repository root):

    python3 scripts/enrich_publications.py            # fill in missing fields
    python3 scripts/enrich_publications.py --force    # look everything up again
    python3 scripts/enrich_publications.py FILE...    # only these publications

For every file in _publications/ the script looks the paper up by title in
Crossref (DOI, authors, venue type), arXiv (preprint, abstract, authors) and
OpenAlex (abstract, open-access PDF). It only accepts close title matches and
only adds fields that are missing, so values you edit by hand are kept. It also
rebuilds the `citation` line from the author list, so names are spelled
consistently (for example "Niki van Stein" rather than "Niki Stein").

Fields it writes to the front matter:
    authors     list of author names
    doi         DOI, without https://doi.org/
    paperurl    link to the publisher's page (from the DOI)
    arxiv       arXiv identifier
    pdf         open-access PDF (arXiv or the publisher)
    venue_type  journal, conference, chapter, book or preprint
    abstract    the paper's abstract
These feed the publication page, its search-engine metadata (Google Scholar
citation_* tags and schema.org) and /llms-full.txt.
"""

import argparse
import difflib
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(ROOT, "_publications")
CONTACT = "n.van.stein@liacs.leidenuniv.nl"
HEADERS = {"User-Agent": f"nikivanstein.nl publication metadata (mailto:{CONTACT})"}
ATOM = "{http://www.w3.org/2005/Atom}"
MIN_SIMILARITY = 0.9
FIELDS = ["authors", "doi", "paperurl", "arxiv", "pdf", "venue_type", "abstract"]
CROSSREF_TYPES = {
    "journal-article": "journal",
    "proceedings-article": "conference",
    "book-chapter": "chapter",
    "book": "book",
    "edited-book": "book",
    "monograph": "book",
    "posted-content": "preprint",
}
# Spellings to use for co-authors whose names publishers record inconsistently.
NAME_FIXES = {"Thomas Back": "Thomas Bäck", "Thomas Baeck": "Thomas Bäck", "Thomas H. W. Bäck": "Thomas Bäck",
              "Thomas H.W. Bäck": "Thomas Bäck", "Thomas HW Bäck": "Thomas Bäck"}
# BibTeX accents left over from older imports, e.g. B{\&quot;a}ck.
LATEX_ACCENTS = {'"': "̈", "&quot;": "̈", "'": "́", "&apos;": "́", "`": "̀",
                 "^": "̂", "~": "̃", "u": "̊", "r": "̊", "v": "̌", "c": "̧"}


def get(url, tries=4):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as err:  # network hiccups and rate limits
            last = err
            time.sleep(3 * (attempt + 1))
    raise last


def norm(text):
    return re.sub(r"[^a-z0-9]", "", html.unescape(text or "").lower())


def similarity(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def clean_text(text):
    text = re.sub(r"<[^>]+>", " ", text or "")  # JATS tags in Crossref abstracts
    text = html.unescape(text)
    text = re.sub(r"^\s*(Abstract|ABSTRACT)[.:]?\s*", "", text)
    return " ".join(text.split())


def unlatex(name):
    def accent(m):
        mark, letter = m.group(1), m.group(2)
        return __import__("unicodedata").normalize("NFC", letter + LATEX_ACCENTS.get(mark, ""))
    name = re.sub(r"\{\\(&quot;|&apos;|[\"'`^~urvc])\s*\{?([A-Za-z])\}?\}", accent, name)
    return name.replace("{", "").replace("}", "")


def site_owner():
    with open(os.path.join(ROOT, "_config.yml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)["author"]["name"]


OWNER = site_owner()
OWNER_FAMILY = norm(OWNER.split(" ", 1)[1])  # "vanstein"


def fix_name(name):
    """Normalise an author name; the site owner always appears under the site's name."""
    name = " ".join(unlatex(name).split())
    if norm(name) in ("n" + OWNER_FAMILY, "b" + OWNER_FAMILY):  # e.g. "n.van.stein"
        return OWNER
    given, _, family = name.rpartition(" ")
    for particle in ("van ", "Van ", "de ", "der ", "van der "):
        if given.endswith(" " + particle.strip()) or given == particle.strip():
            given, family = given[: -len(particle.strip())].strip(), particle + family
    if norm(family) in (OWNER_FAMILY, "stein") and given[:1].upper() in ("N", "B"):
        return OWNER
    return NAME_FIXES.get(name, name)


# --- metadata sources -------------------------------------------------------

def crossref(title, year):
    """Best Crossref match: published versions before preprints, then the closest year."""
    query = urllib.parse.urlencode({"query.bibliographic": title, "rows": 8,
                                    "select": "DOI,title,author,type,abstract,link,published,issued"})
    items = json.loads(get(f"https://api.crossref.org/works?{query}"))["message"]["items"]
    candidates = []
    for item in items:
        if item.get("type") in ("component", "peer-review", "dataset"):
            continue
        if similarity(title, (item.get("title") or [""])[0]) < MIN_SIMILARITY:
            continue
        people = [" ".join(filter(None, [p.get("given"), p.get("family")])) for p in item.get("author", [])]
        if item.get("type") == "posted-content" and people and OWNER not in map(fix_name, people):
            continue  # someone else's preprint with the same title
        parts = (item.get("published") or item.get("issued") or {}).get("date-parts", [[None]])[0]
        gap = abs(parts[0] - year) if parts and parts[0] else 99
        if gap > 2:
            continue
        candidates.append((item.get("type") == "posted-content", gap, item))
    candidates.sort(key=lambda c: (c[0], c[1]))
    return candidates[0][2] if candidates else None


def arxiv(title=None, arxiv_id=None):
    if arxiv_id:
        query = "id_list=" + arxiv_id
    else:
        words = re.sub(r"[^A-Za-z0-9 ]", " ", title)
        query = "search_query=" + urllib.parse.quote(f'ti:"{words}"') + "&max_results=5"
    feed = ET.fromstring(get("https://export.arxiv.org/api/query?" + query))
    time.sleep(3)  # arXiv asks for a pause between requests
    for entry in feed.findall(ATOM + "entry"):
        found = " ".join((entry.findtext(ATOM + "title") or "").split())
        if not found or (title and not arxiv_id and similarity(title, found) < MIN_SIMILARITY):
            continue
        ident = entry.findtext(ATOM + "id").rsplit("/abs/", 1)[-1]
        return {
            "id": re.sub(r"v\d+$", "", ident),
            "abstract": clean_text(entry.findtext(ATOM + "summary")),
            "authors": [" ".join(a.findtext(ATOM + "name").split()) for a in entry.findall(ATOM + "author")],
        }
    return None


def openalex(doi=None, title=None):
    if doi:
        url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
    else:
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": title, "per-page": 3})
    url += ("&" if "?" in url else "?") + "mailto=" + CONTACT
    try:
        data = json.loads(get(url, tries=2))
    except Exception:
        return None
    works = [data] if doi else data.get("results", [])
    for work in works:
        if title and similarity(title, work.get("title") or "") < MIN_SIMILARITY:
            continue
        index = work.get("abstract_inverted_index") or {}
        words = sorted((pos, word) for word, positions in index.items() for pos in positions)
        oa = work.get("best_oa_location") or {}
        return {"abstract": clean_text(" ".join(w for _, w in words)), "pdf": oa.get("pdf_url")}
    return None


# --- front matter -----------------------------------------------------------

def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    return m.group(1), m.group(2)


def dump_field(key, value):
    if key == "abstract":
        body = "\n".join("  " + line for line in wrap(value))
        return f"abstract: >-\n{body}"
    return yaml.safe_dump({key: value}, allow_unicode=True, width=10**6, sort_keys=False).rstrip()


def wrap(text, width=100):
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}" if line else word
    return lines + ([line] if line else [])


def citation_authors(citation):
    head = html.unescape(citation).split(', "', 1)[0]
    return [unlatex(a.strip()) for a in re.split(r",\s+", head) if a.strip()]


def build_citation(authors, title, venue, year):
    names = ",  ".join(authors)
    venue_part = f" {venue}," if venue else ""
    return f" {names}, &quot;{title}.&quot;{venue_part} {year}."


def enrich(path, force):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    fm_text, body = split_front_matter(raw)
    fm = yaml.safe_load(fm_text) or {}
    missing = [f for f in FIELDS if force or not fm.get(f)]
    if not missing and not force:
        return None

    title = html.unescape(str(fm["title"]))
    venue = str(fm.get("venue") or "")
    found = {}

    year = int(str(fm.get("date"))[:4])
    arxiv_in_venue = re.search(r"(\d{4}\.\d{4,5})", venue) if "arxiv" in venue.lower() else None
    known_arxiv = fm.get("arxiv") or (arxiv_in_venue.group(1) if arxiv_in_venue else None)
    cr = crossref(title, year)
    if cr and "arxiv" in cr.get("DOI", "").lower():
        cr = None  # arXiv's own DOIs: the arXiv lookup below covers these
    if cr:
        found["doi"] = cr["DOI"]
        found["paperurl"] = "https://doi.org/" + cr["DOI"]
        found["venue_type"] = CROSSREF_TYPES.get(cr.get("type"), "other")
        authors = [" ".join(filter(None, [a.get("given"), a.get("family")])) or a.get("name", "")
                   for a in cr.get("author", [])]
        if authors:
            found["authors"] = [a for a in authors if a]
        if cr.get("abstract"):
            found["abstract"] = clean_text(cr["abstract"])
        pdfs = [l["URL"] for l in cr.get("link", []) if l.get("content-type") == "application/pdf"
                and l.get("intended-application") != "text-mining"]
        if pdfs and "arxiv" in pdfs[0]:
            found["pdf"] = pdfs[0]

    ax = arxiv(arxiv_id=known_arxiv) if known_arxiv else arxiv(title=title)
    if ax:
        found["arxiv"] = ax["id"]
        found.setdefault("pdf", f"https://arxiv.org/pdf/{ax['id']}")
        if ax["abstract"]:
            found["abstract"] = ax["abstract"]  # author-written, usually the cleanest
        found.setdefault("authors", ax["authors"])
        if not cr:
            found.setdefault("venue_type", "preprint" if "arxiv" in venue.lower() else "other")
            found.setdefault("paperurl", f"https://arxiv.org/abs/{ax['id']}")

    if "abstract" not in found or "pdf" not in found:
        oa = openalex(doi=found.get("doi")) if found.get("doi") else openalex(title=title)
        if oa:
            if oa.get("abstract") and len(oa["abstract"]) > 200:
                found.setdefault("abstract", oa["abstract"])
            if oa.get("pdf"):
                found.setdefault("pdf", oa["pdf"])

    if found.get("authors"):
        found["authors"] = list(dict.fromkeys(fix_name(a) for a in found["authors"]))
    updates = {k: v for k, v in found.items() if k in missing and v}
    authors = updates.get("authors") or fm.get("authors") or citation_authors(str(fm.get("citation", "")))
    authors = list(dict.fromkeys(fix_name(a) for a in authors))  # also drops duplicates
    if authors and "authors" in missing and "authors" not in updates:
        updates["authors"] = authors  # no source found the paper: keep the citation's authors
    citation = build_citation(authors, title, venue, year) if authors else fm.get("citation")

    lines = fm_text.split("\n")
    out, skip = [], False
    for line in lines:  # drop keys that are being replaced (including block values)
        key = line.split(":", 1)[0] if re.match(r"^[A-Za-z_]+:", line) else None
        if key:
            skip = key in updates or key == "citation"
        if not skip:
            out.append(line)
    out.append(dump_field("citation", citation))
    for key in FIELDS:
        if key in updates:
            out.append(dump_field(key, updates[key]))
    body = re.sub(r"^\s*Use \[Google Scholar\]\([^)]*\)\{:target=\"_blank\"\} for full citation\s*$", "", body)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("---\n" + "\n".join(out) + "\n---\n" + body.lstrip("\n"))
    return sorted(updates)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", help="publication files (default: all)")
    parser.add_argument("--force", action="store_true", help="look up and replace every field")
    args = parser.parse_args()
    files = args.files or sorted(os.path.join(PUB_DIR, f) for f in os.listdir(PUB_DIR) if f.endswith(".md"))
    for i, path in enumerate(files, 1):
        try:
            added = enrich(path, args.force)
        except Exception as err:
            print(f"[{i}/{len(files)}] {os.path.basename(path)}: failed ({err})", file=sys.stderr)
            continue
        status = "up to date" if added is None else ("added " + ", ".join(added) if added else "nothing found")
        print(f"[{i}/{len(files)}] {os.path.basename(path)}: {status}", flush=True)


if __name__ == "__main__":
    main()
