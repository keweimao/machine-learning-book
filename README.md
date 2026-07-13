# Machine Learning: The Quest for Information and Meaning

This is the 2026 single-source edition of Weimao Ke's book project. The canonical source is Quarto Markdown (`.qmd`). The same chapter files render to a searchable web book, a LaTeX-backed print PDF, EPUB, and—when needed for a publisher—Word or raw LaTeX.

## Current state

- All substantive LaTeX chapters have been migrated without intentionally rewriting the author's prose.
- The substantial clustering chapter, previously disabled because of a LaTeX build error, is restored as Chapter 10.
- Original figures, data, code, tables, and BibTeX references are under `assets/` and `references.bib`.
- Curated KeenSee/Jupyter materials remain in the private historical archive and will be migrated selectively after rights and relevance review.
- Thin or missing chapters contain explicit development outlines. They are scaffolds, not claims that the prose has been written.

The present manuscript is approximately **55% complete overall**. Nine chapters have substantial drafts, one has a useful partial draft, and six require major development. Cross-reference migration and permissions review for third-party images remain editorial tasks.

The migrated project has been successfully rendered and checked as a 240-page PDF, a 16-chapter searchable HTML book, and an EPUB. Representative print pages and an image- and math-heavy web chapter were visually inspected; no broken local web images were found. These are working editorial builds, not a production-ready typeset edition: legacy cross-references and figure permissions still need review.

## Build

Install [Quarto](https://quarto.org/docs/get-started/) and use the existing MacTeX installation:

```bash
cd /Users/wk77/Documents/git/book/newbook26
quarto preview
quarto render --to html
quarto render --to pdf
quarto render --to epub
```

During this migration, a project-local Quarto 1.9.38 runtime was used because the system installer requires an administrator password.

## Authoring rule

Write prose, mathematics, citations, diagrams, exercises, and executable examples in `.qmd`. Use fenced `{python}`, `{mermaid}`, or `{dot}` cells where computation or a diagram adds real value. Do not maintain parallel LaTeX, Markdown, HTML, and notebook versions. Generated `_book/`, `.tex`, HTML, PDF, and EPUB files are outputs, not sources.

## What to do next

1. Review the target structure and completion estimates in `planning/ROADMAP.md`.
2. Perform a prose-level review of Chapters 1–5 before adding new material.
3. Develop Chapters 6, 8, 9, 13, 15, and 16 in that order of dependency.
4. Turn selected supplemental notebooks into short, reproducible end-of-chapter labs.
5. Replace or clear every figure whose reuse rights are uncertain.
6. Send an updated proposal, annotated table of contents, two sample chapters, and the web/PDF prototype to Cambridge and comparison publishers.
