# Development guide

This repository contains TRL’s public website and GitHub profile README. The website is a small static site: hand-written HTML, CSS, and JavaScript, with a Python script that generates the HTML pages.

## Requirements

- Git
- Python 3
- A modern browser for the local preview

There is no Node.js build, package installation, database, or server-side runtime.

## Build the website

Run commands from the repository root:

```bash
python3 tools/build.py
```

On Windows/Git Bash, if your Python installation uses `python` instead of `python3`, use:

```bash
python tools/build.py
```

The builder writes the generated HTML pages, `sitemap.xml`, `robots.txt`, `manifest.webmanifest`, and `.nojekyll` into the repository root. **Edit `tools/build.py` for generated website content, then rebuild.** Do not make a lasting change only in a generated HTML page; it will be overwritten by the next build. The `LEGAL_LAST_UPDATED` value is intentionally manual: update it only when the privacy or terms text itself changes. The sitemap omits page-level `lastmod` values rather than claiming every page changed on every build.

The public offer constants (prices, contact details, and the first-client offer) are near the top of `tools/build.py`. Do not change published prices or offer terms without Rashid’s approval. The “first 50 clients” offer is a total offer definition, not a count of places still available.

## Brand assets

`assets/img/favicon.svg` is the editable mark used by the site; `assets/img/icon-192.png` is its raster app-icon counterpart. `assets/img/og-image.svg` is the editable social-share artwork, while `assets/img/og-image.png` is the deployed 1200 × 630 image referenced by Open Graph and Twitter metadata. Keep each pair aligned when changing the brand. These image exports are intentionally checked in; the static site builder does not require an image-processing package.

## Preview locally

Start a simple local web server from the repository root:

```bash
python3 -m http.server 8080
```

If needed on Windows/Git Bash:

```bash
python -m http.server 8080
```

Open <http://localhost:8080/> in your browser. Stop the server with **Ctrl+C** in the terminal.

## Typical edit-and-check loop

1. Check that your Git working tree is clean or save any existing work safely.
2. Make a feature branch for a change.
3. Edit `tools/build.py` for generated site content, or edit the relevant source asset (such as `assets/css/style.css`, `assets/js/main.js`, or an image).
4. Rebuild the site with `python3 tools/build.py`.
5. Run `git diff --check` and review `git status --short` plus `git diff --stat`.
6. Preview the affected page locally. Check phone-width layout, links, images, headings, and the contact action.
7. Review every changed file before committing. Do not include customer data, passwords, API keys, payment screenshots, or other secrets.
8. After publishing, verify the live page on desktop and a real phone.

## Deployment

The recorded configuration is GitHub Pages serving the `main` branch from the repository root. Confirm the current setting under **Repository → Settings → Pages** before changing deployment instructions. A feature-branch commit is not a live-site update; the Pages source branch must receive the approved change before the public website changes.

## Important README distinction

`README.md` is the public TRL/GitHub profile README. Keep it client-facing and concise. This `DEVELOPMENT.md` is the collaborator setup guide; link to it rather than replacing the profile README with developer instructions.

## Client data and proof

The public `docs/LEAD-TRACKER-TEMPLATE.csv` is an empty header-only template. Copy it to the ignored `private-data/` folder before entering any real enquiry information. Never commit real leads, client notes, payment screenshots, or unapproved case-study details.

`docs/CASE-STUDY-TEMPLATE.md` is only a blank drafting aid. A real case study requires a delivered project, evidence for every result, and the client’s written permission for the final text, quote, name, logo, numbers, and screenshots.

For the file-by-file layout, see [docs/PROJECT-MAP.md](docs/PROJECT-MAP.md).
