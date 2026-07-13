# Migration and Provenance

## Authority rules

1. `print/chapters/*.tex` (2024 filesystem copies; compiled manuscript dated 2023) is the authority for narrative chapters.
2. `apps/keensee/pdp/content/**/*.ipynb` (mostly 2020) is the authority for web-era executable lessons, demonstrations, assignments, and later pedagogical expansions.
3. `print/chapters/gfm`, `markdown`, and `notebook` are mechanical conversion derivatives and were not treated as independent writing.
4. Generated KeenSee HTML, duplicate underscore/hyphen HTML routes, notebook checkpoints, and bundled Jupyter Book documentation were excluded.
5. Original material remains unchanged in `print/` and `/Users/wk77/Documents/Business/2026/apps/keensee/pdp/content`; `oldbook_organized` is the curated preservation copy.

## Chapter mapping

| New source | Primary original source |
|---|---|
| `index.qmd` | `print/chapters/about.tex` |
| `01-data-to-meaning.qmd` | `print/chapters/datainfo.tex` |
| `02-data-representations.qmd` | `print/chapters/numbers.tex` |
| `03-vectors-matrices-geometry.qmd` | `print/chapters/matrix.tex` |
| `04-probability-statistics.qmd` | `print/chapters/probability.tex`; `stats.tex` was only a placeholder |
| `05-information-entropy.qmd` | `print/chapters/info.tex` |
| `06-data-preparation.qmd` | `print/chapters/prep.tex`; KeenSee preprocessing notebooks are supplemental source material |
| `07-classification.qmd` | `print/chapters/binary.tex` |
| `08-multiclass.qmd` | `print/chapters/choices.tex` |
| `09-numeric-prediction.qmd` | `print/chapters/numeric.tex` |
| `10-clustering.qmd` | `print/chapters/organization.tex` (previously disabled in `main.tex`) |
| `11-text-language.qmd` | `print/chapters/text.tex` |
| `12-search-retrieval.qmd` | `print/chapters/search.tex` |
| `13-structural-analysis.qmd` | `print/chapters/graph.tex` |
| `14-evaluation.qmd` | `print/chapters/eval.tex` |
| `15-generalization.qmd` | `print/chapters/fitting.tex` plus `print/notes/classify.md` for future integration |
| `16-scaling.qmd` | `print/chapters/scale.tex` |

## Conversion cautions

- Prose and equations were converted mechanically with Pandoc 3.8.3 through Quarto 1.9.38, then minimally normalized for asset paths and identifiers.
- Legacy LaTeX cross-references were preserved as links where automatic conversion was uncertain. They require a dedicated editorial pass to become native Quarto `@fig-`, `@tbl-`, `@eq-`, and `@sec-` references.
- EPS figures referenced by core chapters were rendered to PNG for HTML compatibility; original EPS files remain beside them for print provenance.
- Some photographs and copied teaching examples may require permission, replacement, or clearer attribution before any public release.

