A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# Site design (XAI design system)

The homepage (`/`) and the group page (`/xai-group/`) use the XAI group design system, with a light and a dark theme. The header button switches the theme and remembers the choice; without a choice the visitor's system setting is used.

- Layouts: `_layouts/xai-home.html` (homepage) and `_layouts/xai-group.html` (group page). The shared header and footer are in `_includes/xai/`.
- Styles: `_sass/xai/` (`_tokens.scss` holds every colour for both themes; `_legacy.scss` restyles the older archive, post and project pages).
- Homepage content:
  - hero text: front matter of `_pages/about.md`
  - featured book: `_data/book.yml`
  - "What I work on": `_data/research.yml`
  - talks: the newest talks of the current year; add `image:` (a file under `images/`) or `youtube:` (a video id) to a talk to show a thumbnail
  - selected papers: publications with `selected: true` and `topic: XAI`, `AAD` or `APPLIED` in their front matter
- Blog and detail pages: `_layouts/xai-blog.html` (blog overview with topic filters), `_layouts/xai-post.html` (blog posts) and `_layouts/xai-detail.html` (talks, publications and teaching). Optional front matter:
  - `related:` a list of `title`, `url` and `kind` (for example Paper, Blog, Talk, Project), shown as related links next to the post or talk
  - `header.cover:` the wide image at the top of a post (falls back to `header.teaser`)
  - on talks, `youtube:` embeds the recording and `image:` shows a slide or photo
- Group page content: front matter of `_pages/xai-group.md` (hero, mission/vision/culture, people, footer links); the full mission text is the page body. Projects come from `_projects/` and are placed on the timeline by their `year:` field.

# Images

Pages don't load the original images in `images/`, `img/` and `files/`. They load resized WebP versions from `images/optimized/`, which `scripts/optimize_images.py` generates. Every image that goes through the `img.html` include gets a responsive `<picture>` with `width`/`height` attributes and lazy loading. Animated GIFs become a muted, looping video that only plays while it is on screen.

**Adding an image**

1. Put the original in `images/` or `img/` (any size; keep the high-resolution file).
2. Reference it as usual: in front matter (`header.teaser`, `header.cover`, `image:`, a person's `image:` in `_data/people.yml`, …), or in a page with the include:
   ```liquid
   {% include img.html src="/images/my-figure.png" alt="What the figure shows" sizes="(max-width: 760px) 100vw, 680px" %}
   ```
   `sizes` is how wide the image is shown, so the browser can pick the smallest file that looks sharp. Add `loading="eager" fetchpriority="high"` only for the main image at the top of a page. On a line of its own in Markdown, wrap the include in `<p>…</p>`.
3. Generate the optimized versions and commit them together with the original:
   ```bash
   pip install -r scripts/requirements.txt
   python3 scripts/optimize_images.py
   git add images/optimized _data/image_variants.json
   ```

The script only processes images that some page, layout or data file refers to, and it skips images that haven't changed. `--check` reports images that still need processing, `--force` regenerates everything, and `--clean` removes files that are no longer needed. The widths to generate are set per folder in `scripts/image-sizes.yml` (for example avatars at 64–240px and logos at 64–600px). An image the script hasn't processed yet still shows, just without the optimization.

Pages that need formulas can set `mathjax: true` in their front matter; MathJax is not loaded anywhere else.

# Publications

Each file in `_publications/` can carry `authors`, `doi`, `paperurl`, `arxiv`, `pdf`, `venue_type` (journal, conference, chapter, book or preprint) and `abstract` in its front matter. The publication page shows them, and search engines and AI assistants read them (see below). To fill them in for new publications:

```bash
python3 scripts/enrich_publications.py                              # all publications with missing fields
python3 scripts/enrich_publications.py _publications/2026-...md     # just one
```

The script looks each paper up by title in Crossref, arXiv and OpenAlex and only accepts close title matches. It only adds fields that are missing, so anything you edit by hand stays as it is; `--force` looks everything up again. It also rebuilds the `citation` line from the author list. Your own name always appears as `author.name` from `_config.yml`, whatever name the publisher's record uses.

# Search engines and AI assistants

- Every page has a description, a canonical URL, Open Graph tags and schema.org structured data: a `Person` for you (profiles from the `author:` block in `_config.yml`, including `knows_about`, `dblp` and `wikidata` when filled in), plus `ScholarlyArticle` on publications and `BlogPosting` on posts. Publication pages also carry the `citation_*` tags Google Scholar reads.
- A page's description comes from `description:` in its front matter, else the abstract or excerpt.
- `robots.txt` allows all crawlers, including the AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended and others), and points to the sitemap. To opt one out, change its `Allow: /` to `Disallow: /`.
- `llms.txt` (a short overview for AI assistants) and `llms-full.txt` (every publication with its abstract) are generated from the site's data, so they update by themselves.
- Pages that shouldn't appear in search results can set `noindex: true` and `sitemap: false`.
- To verify the site with Google Search Console or Bing Webmaster Tools (Bing's index also feeds ChatGPT search and Copilot), put the verification code in `google_site_verification` or `bing_site_verification` in `_config.yml`.

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
