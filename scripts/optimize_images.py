#!/usr/bin/env python3
"""Generate resized WebP and fallback variants for the images used on the site.

Usage (from the repository root):

    pip install -r scripts/requirements.txt
    python3 scripts/optimize_images.py            # process new or changed images
    python3 scripts/optimize_images.py --force    # regenerate everything
    python3 scripts/optimize_images.py --check    # exit 1 if anything is out of date
    python3 scripts/optimize_images.py --clean    # also delete orphaned variants

Only images whose path appears somewhere in the site's source files (pages,
layouts, includes, data files, styles) are processed, so unused images in the
repository don't produce variants. Pass --all to process every image.

Animated GIFs become a muted, looping MP4 with a WebP poster (needs the
imageio-ffmpeg package; without it they become animated WebP).

Widths and quality settings live in scripts/image-sizes.yml. The results are
recorded in _data/image_variants.json, which _includes/img.html uses to render
a <picture> element with a WebP srcset and a JPEG/PNG/GIF fallback.
"""

import argparse
import fnmatch
import hashlib
import json
import os
import re
import sys

import subprocess

import yaml
from PIL import Image, ImageOps, ImageSequence

try:  # Optional: used to turn animated GIFs into much smaller MP4 videos.
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "scripts", "image-sizes.yml")
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".jfif", ".gif", ".webp"}
TEXT_EXTS = {".md", ".markdown", ".html", ".yml", ".yaml", ".json", ".scss", ".css", ".js", ".xml"}
TEXT_SKIP_DIRS = {".git", "_site", "node_modules", "vendor", ".bundle", ".jekyll-cache", ".sass-cache"}
# Bump when the encoding logic changes, so --check notices stale variants.
PIPELINE_VERSION = 4


def load_config():
    with open(CONFIG) as fh:
        return yaml.safe_load(fh)


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def find_images(cfg):
    skip_dirs = {d.rstrip("/") for d in cfg.get("skip_dirs", [])}
    out = []
    for src_dir in cfg["source_dirs"]:
        for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, src_dir)):
            dirnames[:] = [d for d in dirnames if rel(os.path.join(dirpath, d)) not in skip_dirs]
            for name in filenames:
                path = rel(os.path.join(dirpath, name))
                if os.path.splitext(name)[1].lower() not in IMAGE_EXTS:
                    continue
                if any(fnmatch.fnmatch(path, p) for p in cfg.get("skip_patterns", [])):
                    continue
                out.append(path)
    return sorted(out)


def source_text(cfg):
    """Concatenated text of every file that could reference an image."""
    manifest = os.path.normpath(os.path.join(ROOT, cfg["manifest"]))
    output_dir = os.path.join(ROOT, cfg["output_dir"])
    chunks = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [
            d for d in dirnames
            if d not in TEXT_SKIP_DIRS and os.path.join(dirpath, d) != output_dir
        ]
        for name in filenames:
            path = os.path.join(dirpath, name)
            if os.path.splitext(name)[1].lower() not in TEXT_EXTS or os.path.normpath(path) == manifest:
                continue
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    chunks.append(fh.read())
            except OSError:
                pass
    return "\n".join(chunks)


def is_referenced(path, text):
    # Templates often prefix a bare file name with /images/ (e.g. teasers),
    # so also look for the path without its leading "images/".
    candidates = {path}
    if path.startswith("images/"):
        candidates.add(path[len("images/"):])
    return any(c in text for c in candidates)


def rule_for(path, cfg):
    settings = dict(cfg["defaults"])
    for rule in cfg.get("rules", []):
        if fnmatch.fnmatch(path, rule["match"]):
            settings.update({k: v for k, v in rule.items() if k != "match"})
            break
    return settings


def slug(path):
    return re.sub(r"[^A-Za-z0-9._/-]+", "-", path)


def file_hash(path, settings):
    h = hashlib.sha1()
    with open(os.path.join(ROOT, path), "rb") as fh:
        h.update(fh.read())
    h.update(json.dumps([settings, PIPELINE_VERSION], sort_keys=True).encode())
    return h.hexdigest()


def target_widths(natural, widths):
    return sorted({min(w, natural) for w in widths})


def has_alpha(img):
    if img.mode in ("RGBA", "LA"):
        return img.getchannel("A").getextrema()[0] < 255
    return img.mode == "P" and "transparency" in img.info


def encode_still(path, settings, out_base):
    img = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, path)))
    alpha = has_alpha(img)
    img = img.convert("RGBA" if alpha else "RGB")
    fallback_ext = ".png" if alpha else ".jpg"
    widths = target_widths(img.width, settings["widths"])
    # One fallback is enough: it is only used by browsers without WebP support.
    fallback_w = max([w for w in widths if w <= settings["fallback_max_width"]] or [widths[0]])
    variants = []
    for w in widths:
        h = round(img.height * w / img.width)
        resized = img if w == img.width else img.resize((w, h), Image.LANCZOS)
        webp = f"{out_base}-{w}.webp"
        resized.save(os.path.join(ROOT, webp), "WEBP", quality=settings["webp_quality"], method=6)
        variant = {"w": w, "h": h, "webp": webp, "fallback": None}
        if w == fallback_w:
            fallback = f"{out_base}-{w}{fallback_ext}"
            if alpha:
                resized.save(os.path.join(ROOT, fallback), "PNG", optimize=True)
            else:
                resized.save(os.path.join(ROOT, fallback), "JPEG", quality=settings["jpeg_quality"],
                             optimize=True, progressive=True)
            # At full size, keep the original when it is already smaller.
            if w == img.width and os.path.splitext(path)[1].lower() != ".webp" and \
                    os.path.getsize(os.path.join(ROOT, path)) <= os.path.getsize(os.path.join(ROOT, fallback)):
                os.remove(os.path.join(ROOT, fallback))
                fallback = path
            variant["fallback"] = fallback
        variants.append(variant)
    return variants, "image/png" if alpha else "image/jpeg"


def encode_animated(path, settings, out_base):
    src = Image.open(os.path.join(ROOT, path))
    durations = []
    frames = []
    for frame in ImageSequence.Iterator(src):
        durations.append(frame.info.get("duration", src.info.get("duration", 100)))
        frames.append(frame.convert("RGBA"))
    variants = []
    for w in target_widths(src.width, settings["widths"]):
        h = round(src.height * w / src.width)
        resized = [f if w == src.width else f.resize((w, h), Image.LANCZOS) for f in frames]
        webp = f"{out_base}-{w}.webp"
        resized[0].save(os.path.join(ROOT, webp), "WEBP", save_all=True, append_images=resized[1:],
                        duration=durations, loop=src.info.get("loop", 0),
                        quality=settings["webp_quality"], method=4)
        variants.append({"w": w, "h": h, "webp": webp, "fallback": None})
    # Browsers without WebP get the original GIF.
    variants[-1]["fallback"] = path
    return variants, "image/gif"


def encode_video(path, settings, out_base):
    """Animated GIF -> muted MP4 (H.264) and WebM (VP9) plus a WebP poster.

    Browsers play the MP4; the WebM is a fallback for the few without H.264.
    """
    src = Image.open(os.path.join(ROOT, path))
    w = min(max(settings["widths"]), src.width)
    w -= w % 2  # H.264 needs even dimensions
    h = round(src.height * w / src.width / 2) * 2
    video = f"{out_base}-{w}.mp4"
    webm = f"{out_base}-{w}.webm"
    ffmpeg = [imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y",
              "-i", os.path.join(ROOT, path), "-vf", f"scale={w}:{h}:flags=lanczos", "-an",
              "-pix_fmt", "yuv420p"]
    subprocess.run(ffmpeg + [
        "-c:v", "libx264", "-crf", str(settings.get("video_crf", 26)), "-preset", "slow",
        "-movflags", "+faststart", os.path.join(ROOT, video),
    ], check=True)
    subprocess.run(ffmpeg + [
        "-c:v", "libvpx-vp9", "-crf", str(settings.get("webm_crf", 38)), "-b:v", "0", "-row-mt", "1",
        os.path.join(ROOT, webm),
    ], check=True)
    poster = f"{out_base}-{w}-poster.webp"
    src.seek(0)
    src.convert("RGB").resize((w, h), Image.LANCZOS).save(
        os.path.join(ROOT, poster), "WEBP", quality=settings["webp_quality"], method=6)
    return {"width": w, "height": h, "type": "video/mp4", "video": "/" + video, "webm": "/" + webm,
            "poster": "/" + poster, "src": "/" + path, "files": [video, webm, poster]}


def process(path, settings, cfg):
    out_base = slug(os.path.join(cfg["output_dir"], os.path.splitext(path)[0]))
    os.makedirs(os.path.dirname(os.path.join(ROOT, out_base)), exist_ok=True)
    with Image.open(os.path.join(ROOT, path)) as probe:
        animated = getattr(probe, "is_animated", False)
    if animated and settings.get("video", True) and imageio_ffmpeg:
        return encode_video(path, settings, out_base)
    if animated:
        if settings.get("video", True):
            print(f"  imageio-ffmpeg is not installed, so {path} becomes an animated WebP instead of an MP4")
        variants, mime = encode_animated(path, settings, out_base)
    else:
        variants, mime = encode_still(path, settings, out_base)
    top = variants[-1]
    fallback = next(v["fallback"] for v in variants if v["fallback"])
    return {
        "width": top["w"],
        "height": top["h"],
        "type": mime,
        "src": "/" + fallback,
        "webp": ", ".join(f"/{v['webp']} {v['w']}w" for v in variants),
        "files": [v["webp"] for v in variants] + ([fallback] if fallback != path else []),
    }


def outputs_exist(entry):
    return all(os.path.exists(os.path.join(ROOT, f)) for f in entry.get("files", []))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true", help="regenerate all variants")
    parser.add_argument("--all", action="store_true", help="also process images no source file references")
    parser.add_argument("--check", action="store_true", help="report out-of-date images and exit 1 if any")
    parser.add_argument("--clean", action="store_true", help="delete variants no longer in the manifest")
    args = parser.parse_args()

    cfg = load_config()
    manifest_path = os.path.join(ROOT, cfg["manifest"])
    try:
        with open(manifest_path) as fh:
            old = json.load(fh)
    except (OSError, ValueError):
        old = {}

    images = find_images(cfg)
    if not args.all:
        text = source_text(cfg)
        images = [p for p in images if is_referenced(p, text)]

    new, todo = {}, []
    for path in images:
        settings = rule_for(path, cfg)
        digest = file_hash(path, settings)
        prev = old.get("/" + path)
        if not args.force and prev and prev.get("hash") == digest and outputs_exist(prev):
            new["/" + path] = prev
        else:
            todo.append((path, settings, digest))

    removed = sorted(set(old) - {"/" + p for p in images})
    if args.check:
        for path, _, _ in todo:
            print(f"out of date: {path}")
        for key in removed:
            print(f"no longer referenced: {key}")
        sys.exit(1 if todo or removed else 0)

    for i, (path, settings, digest) in enumerate(todo, 1):
        print(f"[{i}/{len(todo)}] {path}", flush=True)
        entry = process(path, settings, cfg)
        entry["hash"] = digest
        new["/" + path] = entry

    with open(manifest_path, "w") as fh:
        json.dump(dict(sorted(new.items())), fh, indent=1, ensure_ascii=False)
        fh.write("\n")

    if args.clean:
        keep = {f for e in new.values() for f in e.get("files", [])}
        for dirpath, _, filenames in os.walk(os.path.join(ROOT, cfg["output_dir"])):
            for name in filenames:
                path = rel(os.path.join(dirpath, name))
                if path not in keep:
                    os.remove(os.path.join(ROOT, path))
                    print(f"removed {path}")

    print(f"{len(todo)} processed, {len(new) - len(todo)} up to date, {len(new)} in manifest")


if __name__ == "__main__":
    main()
