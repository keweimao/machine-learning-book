# Figure audit

Audit completed July 13, 2026 against the Quarto manuscript and the active
figure environments in `/Users/wk77/Documents/git/book/print`.

The original migration retained captions for many TikZ figures but dropped
their drawing bodies. Those diagrams have been rendered from the historical
LaTeX sources and restored as native Quarto figures. Figures that used image
files were checked against the copied assets and given usable captions,
identifiers, and cross-references where necessary.

| Chapter | Authored figures | Result |
|---|---:|---|
| 1. From Data to Information and Meaning | 5 | Restored five composite figures from nine original TikZ panels. |
| 2. Data Types and Representations | 7 | Restored all set and vector diagrams. |
| 3. Vectors, Matrices, and Geometric Thinking | 9 | Restored all vector-geometry diagrams. |
| 4. Probability and Statistical Thinking | 11 | Verified six file-based figures and restored five TikZ plots. Two paired figures use two image assets each. |
| 5. Information, Entropy, and Divergence | 5 | Verified one file-based figure and restored four TikZ plots. |
| 6. Data Preparation and Feature Engineering | 0 | No figures in the active legacy chapter. |
| 7. Classification | 20 | Restored all classification and neural-network diagrams. |
| 8. Multiclass and Structured Decisions | 0 | No figures in the active legacy chapter. |
| 9. Numeric Prediction and Regression | 0 | No figures in the active legacy chapter. |
| 10. Clustering and Organization | 15 | Restored all clustering diagrams. |
| 11. Text and Human Language | 7 | Restored all document-space, cosine, and Zipf diagrams. |
| 12. Search and Retrieval | 6 | Verified four file-based figures and reconstructed two postings figures from `print/tfigs`. |
| 13. Graphs and Structural Analysis | 0 | No figures in the active legacy chapter. |
| 14. Evaluation and Experimentation | 3 | Restored the precision-recall, ROC/AUC, and correlation plots. |
| 15. Generalization, Model Selection, and Fit | 0 | No figures in the active legacy chapter. |
| 16. Scaling, Deployment, and Responsible Use | 0 | No figures in the active legacy chapter. |

## Verification summary

- 88 authored figures are represented by 90 referenced image assets (two
  Chapter 4 figures are two-panel layouts).
- All 90 web image references resolve to non-empty assets.
- The legacy TikZ manifest contains 72 successful renders and zero failures.
- The complete HTML book renders without figure or citation warnings.
- The complete PDF book renders successfully using paired PDF versions of the
  generated SVG assets.
- No empty migrated figure containers remain.

## Rebuilding generated figures

```bash
node scripts/rebuild_chapter1_figures.mjs
python3 scripts/render_legacy_tikz.py 02 03 04 05 07 10 11 12 14
quarto render --to html
quarto render --to pdf
```

The TikZ renderer records provenance and status in
`planning/FIGURE_RENDER_MANIFEST.json`. Source references intentionally remain
pointed at extensionless generated assets: Quarto selects SVG for HTML/EPUB and
PDF for print according to `_quarto.yml`.

## Unresolved figures

None.
