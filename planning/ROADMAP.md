# Publication Roadmap

## Target table of contents and readiness

Percentages estimate editorial readiness for a coherent introductory textbook chapter—not merely the amount of text present.

| Part | Ch. | Target chapter title | Est. complete | Existing strengths | Main work remaining |
|---|---:|---|---:|---|---|
| I | 1 | From Data to Information and Meaning | 65% | Distinctive motivating narrative; data-to-meaning examples | Tighten thesis and learning objectives; modernize examples; add recap/exercises |
| I | 2 | Data Types and Representations | 70% | Numerical/categorical data, sets, vectors | Clarify notation; add tables/data frames, missingness, and exercises |
| I | 3 | Vectors, Matrices, and Geometric Thinking | 55% | Matrix operations, norms, distance, angle | Complete dot products, projections, eigenthinking, optimization intuition, and Python lab |
| I | 4 | Probability and Statistical Thinking | 75% | Probability, Bayes, estimators, distributions, MLE | Remove duplicate estimator section; add descriptive statistics, sampling, uncertainty, and exercises |
| I | 5 | Information, Entropy, and Divergence | 70% | Shannon entropy, KL/JS divergence, LIT | Strengthen applications and thermodynamics caveats; add worked problems and citations |
| I | 6 | Data Preparation and Feature Engineering | 10% | Short framing plus strong notebook material | Integrate quality, missing data, scaling, encoding, selection, dimensionality reduction, leakage, and reproducible pipelines |
| II | 7 | Classification: From Neighbors to Neural Networks | 75% | kNN, linear classifiers, SVM, perceptron, kernels, multilayer networks | Separate algorithm intuition from derivations; update neural-network section; add decision trees, calibration, labs, and exercises |
| II | 8 | Multiclass and Structured Decisions | 5% | Chapter concept only | One-vs-rest/one-vs-one, softmax, trees, multilabel/ordinal decisions, error analysis, lab |
| II | 9 | Numeric Prediction and Regression | 5% | Chapter placeholder only | Linear regression, loss, regularization, nonlinear regression, uncertainty, diagnostics, lab |
| II | 10 | Clustering and Organization | 65% | Hierarchical clustering, k-means, EM | Repair/verify equations and figures; add density-based methods, model selection, scaling, evaluation, lab |
| III | 11 | Text and Human Language | 70% | Tokenization, weighting, similarity, Zipf, Naive Bayes | Add embeddings and transformer-era context without overwhelming an introduction; modern preprocessing and evaluation lab |
| III | 12 | Search and Information Retrieval | 75% | Indexing, matching, probabilistic ranking, BM25, PageRank, filtering | Update neural/semantic retrieval and hybrid search; correct legacy examples; add retrieval lab |
| III | 13 | Graphs and Structural Analysis | 5% | Topic identified; graph figures/references available | Graph representation, traversal, centrality, communities, link prediction, graph learning overview, lab |
| IV | 14 | Evaluation and Experimentation | 65% | Classification, ranking, numeric metrics, experiments, efficiency | Complete averaging and skew examples; add resampling, significance, uncertainty, fairness, reproducibility |
| IV | 15 | Generalization, Model Selection, and Fit | 10% | Epigraph and related notes | Bias–variance, overfitting, validation, cross-validation, regularization, learning curves, hyperparameter search |
| IV | 16 | Scaling, Deployment, and Responsible Use | 5% | Chapter concept only | Complexity, data/compute scale, pipelines, monitoring/drift, privacy/security, sustainability, responsible use |

## Recommended length

- Core prose target: 85,000–100,000 words.
- Current substantive core after conversion: roughly 52,000 words before supplements.
- Typical chapter target: 4,500–7,000 words, with the introductory and closing chapters shorter.
- Each chapter should end with a summary, key terms, conceptual questions, applied exercises, and one optional executable lab.

## Schedule to an end-of-year submission

| Window | Milestone | Deliverable |
|---|---|---|
| Jul–Aug 2026 | Consolidate and stabilize | Approve TOC; clean Chapters 1–5, 7, 10–12, and 14; resolve cross-references and figure provenance |
| Sep 2026 | Fill foundations and core model gaps | Complete Chapters 6, 8, 9, and 15; standardize labs/exercises |
| Oct 2026 | Complete scope | Draft Chapters 13 and 16; add modern updates, glossary, instructor notes, and accessibility text |
| Nov 2026 | External review | Freeze alpha manuscript; obtain 3–5 technical/pedagogical reviews; revise sample chapters and proposal |
| Dec 2026 | Submission and public beta | Submit proposal/manuscript package; tag a versioned web-book beta; retain publisher-specific production changes on a separate branch |

## Publisher package

Prepare a concise proposal, market/competition analysis, annotated TOC, author biography, course adoption plan, two polished sample chapters, expected word/figure count, schedule, and a stable preview URL. Present the open site as a companion/open-access edition whose license and relationship to the print edition will be negotiated explicitly; do not assume the final publisher license in the source repository.

