# Machine Learning: The Quest for Information and Meaning

This is the 2026 single-source edition of Weimao Ke's book project. The canonical source is Quarto Markdown (`.qmd`). The same chapter files render to a searchable web book, a LaTeX-backed print PDF, EPUB, and—when needed for a publisher—Word or raw LaTeX.

## Current state

- All substantive LaTeX chapters have been migrated without intentionally rewriting the author's prose.
- The substantial clustering chapter, previously disabled because of a LaTeX build error, is restored as Chapter 10.
- Original figures, data, code, tables, and BibTeX references are under `assets/` and `references.bib`.
- A second, substantial **Practice and Projects** volume follows the theory chapters. It contains sixteen aligned practice chapters, recovered labs and assignments, original notebooks, required datasets, and explicit scaffolds for missing activities.
- Thin or missing chapters contain explicit development outlines. They are scaffolds, not claims that the prose has been written.

The present manuscript is approximately **55% complete overall**. Nine chapters have substantial drafts, one has a useful partial draft, and six require major development. Cross-reference migration and permissions review for third-party images remain editorial tasks.

The migrated project has been successfully rendered as a searchable HTML book and a LaTeX-backed PDF. Volume I contains sixteen theory chapters; the companion practice volume adds aligned activities and recovered notebooks without interrupting the conceptual narrative. These are working editorial builds, not a production-ready typeset edition: recovered code still needs dependency modernization and figure permissions still need review.

See `planning/PRACTICE_VOLUME_AUDIT.md` for the theory/practice alignment,
provenance policy, and remaining activity-development priorities.

## Build

Install [Quarto](https://quarto.org/docs/get-started/) and use the existing MacTeX installation:

```bash
cd /Users/wk77/Documents/git/machine-learning-book
quarto preview
quarto render --to html
quarto render --to pdf
quarto render --to epub
```

During this migration, a project-local Quarto 1.9.38 runtime was used because the system installer requires an administrator password.

## Ongoing workflow

The `main` branch contains the canonical source. The `gh-pages` branch contains generated publication files and is managed automatically by Quarto; do not edit it directly.

Start a writing session by updating the local checkout and opening the live preview:

```bash
cd /Users/wk77/Documents/git/machine-learning-book
git pull --ff-only
quarto preview
```

Stop the preview with `Ctrl-C`. Before committing, render every publication format and review the change list:

```bash
quarto render
git status
git diff
```

Commit and push the source changes:

```bash
git add -A
git status
git commit -m "Describe the chapter or editorial update"
git push
```

A push to `main` triggers `.github/workflows/publish.yml`, which renders the book and updates GitHub Pages. Monitor or diagnose the deployment with:

```bash
gh run list --limit 5
gh run watch
gh run view --log-failed
```

The public edition is available at <https://keweimao.github.io/machine-learning-book/>. To request a deployment without changing content, run the **Publish Quarto Book** workflow from the GitHub Actions page or use:

```bash
gh workflow run publish.yml
gh run watch
```

If the `gh-pages` publication configuration ever needs to be reinitialized, use:

```bash
quarto publish gh-pages --no-browser
```

Generated `_book/`, `.quarto/`, and `site_libs/` directories are ignored on `main`. PDF, EPUB, HTML, and `site_libs/` belong in the generated `gh-pages` publication, not in source commits.

## Authoring rule

Write prose, mathematics, citations, diagrams, exercises, and executable examples in `.qmd`. Use fenced `{python}`, `{mermaid}`, or `{dot}` cells where computation or a diagram adds real value. Do not maintain parallel LaTeX, Markdown, HTML, and notebook versions. Generated `_book/`, `.tex`, HTML, PDF, and EPUB files are outputs, not sources.

## What to do next

1. Review the target structure and completion estimates in `planning/ROADMAP.md`.
2. Perform a prose-level review of Chapters 1–5 before adding new material.
3. Develop Chapters 6, 8, 9, 13, 15, and 16 in that order of dependency.
4. Modernize and test the recovered labs, then replace the explicit practice scaffolds in priority order.
5. Replace or clear every figure whose reuse rights are uncertain.
6. Send an updated proposal, annotated table of contents, two sample chapters, and the web/PDF prototype to Cambridge and comparison publishers.
