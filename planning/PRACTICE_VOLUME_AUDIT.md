# Practice and Projects companion-volume audit

Completed July 20, 2026. The canonical recovery source is
`/Users/wk77/Documents/git/book/oldbook_organized/web-source`. Files published
under KeenSee were compared against this source; the selected materials are
predominantly byte-identical. Rendered HTML, notebook checkpoints, empty test
notebooks, and duplicate prose-only chapter conversions were not imported as
separate activities.

## Editorial architecture

The book now uses two complementary reading paths:

1. **Volume I: concepts and theory** retains the continuous conceptual
   narrative.
2. **Practice and Projects: A Companion Volume** appears before the references
   and follows the same sixteen-chapter sequence.

Each substantive second- or third-level theory section ends with a collapsible
*Put it into practice* link. The destination either identifies recovered work
or states exactly what activity still needs to be written. Practice chapters
link back to their corresponding theory chapters.

## Recovery result

- 25 unique notebooks were selected, copied in their original `.ipynb` form,
  and converted to `.qmd`.
- 13 required data files and 24 referenced instructional figures were copied.
- 126 substantive theory sections have matching practice destinations.
- 114 theory sections point to one or more recovered starting points.
- 12 sections have explicit development scaffolds because no responsible match
  was found.
- The later corrected `assignment_2_final.ipynb` was selected instead of the
  earlier `_v1` draft.
- Historical code is visible but disabled during publication builds. This
  prevents obsolete dependencies from breaking the book while preserving the
  material for modernization and execution testing.

Exact source paths and SHA-256 hashes are recorded in
`practice/PROVENANCE.json`.

## Theory/practice alignment

“Mapped” means that at least one recovered activity provides a useful starting
point. It does not mean that the activity is already complete, current, or
exclusive to that section; several substantial notebooks intentionally support
multiple concepts.

| Theory chapter | Sections | Mapped | Explicit scaffolds | Strongest recovered material |
|---|---:|---:|---:|---|
| 1. Data to meaning | 2 | 2 | 0 | Project framing and generalizability prompts |
| 2. Data representations | 6 | 6 | 0 | Python types, structures, and assignment |
| 3. Vectors and matrices | 9 | 8 | 1 | Vector/cosine assignment |
| 4. Probability | 13 | 13 | 0 | Probability and linearity notebook |
| 5. Information and entropy | 9 | 7 | 2 | Rank-frequency and text-learning assignment |
| 6. Data preparation | 6 | 6 | 0 | Preprocessing and outlier labs |
| 7. Classification | 10 | 9 | 1 | Linear classification and integrated assignment |
| 8. Multiclass decisions | 6 | 6 | 0 | Existing classification assignments, pending multiclass refinement |
| 9. Numeric prediction | 6 | 6 | 0 | Outlier/regression material and pattern assignment |
| 10. Clustering | 11 | 11 | 0 | Yelp text-vectorization and k-means lab |
| 11. Text and language | 10 | 9 | 1 | Two vectorization activities and integrated assignment |
| 12. Search and retrieval | 8 | 8 | 0 | SQLite activities plus recovered ranking questions/exercise |
| 13. Graph analysis | 6 | 0 | 6 | No sufficiently aligned historical activity found |
| 14. Evaluation | 11 | 10 | 1 | Model/pattern evaluation and association-rule metrics |
| 15. Generalization | 6 | 6 | 0 | Existing modeling assignment and project design |
| 16. Scaling and responsible use | 7 | 7 | 0 | Project framework and reinforcement-learning extension |

## Recovered activity groups

- **Optional computational toolkit:** setup, Python primer, input/output,
  branching, randomness, repetition, files, data types, and data structures.
- **Foundations:** vector/cosine construction and probability/linearity.
- **Data work:** preprocessing, outlier analysis, and three historical graded
  data assignments.
- **Models:** classification, text clustering, text vectorization, and an
  integrated learning assignment.
- **Storage and retrieval:** SQLite, SQLite with Python, and a retrieval
  assignment.
- **Evaluation and extensions:** association rules, a data-mining project, and
  a reinforcement-learning extension.

## Highest-priority missing or weak activities

1. **Graph analysis:** add a coherent NetworkX lab covering representation,
   traversal, centrality, communities, and link prediction. This is the only
   theory chapter with no strong recovered match.
2. **Multiclass learning:** build a purpose-written lab for one-vs-rest,
   one-vs-one, softmax, multilabel outcomes, calibration, and class-wise error
   analysis. Current mappings are adjacent binary-classification work.
3. **Regression:** create an end-to-end regression notebook with fitting,
   residuals, regularization, nonlinear alternatives, and uncertainty.
4. **Neural networks:** modernize the older linearity material into a small
   NumPy or scikit-learn multilayer-network experiment.
5. **Information measures:** add direct numerical exercises for entropy, KL,
   Jensen–Shannon divergence, IDF, and Least Information Theory.
6. **Hierarchical and probabilistic clustering:** the recovered clustering lab
   is strongest for text vectorization and k-means; add HAC and EM comparisons.
7. **Generalization and experimentation:** add cross-validation, learning
   curves, leakage detection, hyperparameter selection, and uncertainty-aware
   comparison in a single reproducible workflow.
8. **Scaling and responsible use:** add monitoring/drift, privacy, energy, and
   human-oversight case studies rather than relying only on project prompts.

## Maintenance commands

The recovery is reproducible and should only be rerun when the historical
selection or conversion rules change:

```bash
python3 scripts/recover_practice_volume.py
python3 scripts/link_theory_to_practice.py
quarto render --to html
quarto render --to pdf
```

For ordinary editing, revise the QMD files directly. The source notebooks are
preservation copies, not a second canonical writing format.

## Validation completed

- The full 61-source-file HTML book renders without Quarto warnings or errors.
- All 43 companion-volume web pages were opened in a browser; no broken images
  were found, and representative theory-to-practice and practice-to-theory
  links resolved to the intended section anchors.
- The combined print build renders as a 648-page letter-size PDF without
  Quarto warnings or errors. Representative part openings, recovered code
  pages, mapped activities, and development scaffolds were visually checked.
