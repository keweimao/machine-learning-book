# Publication Roadmap

Related planning: see `TEACHING_MATERIALS_MAPPING.md` for the 2026 audit of
INFO300, INFO624, INFO629, INFO634, DSCI471, LEADS, and LEADING teaching sources,
including chapter mappings, conversion readiness, and transcript priorities.
See `TRANSCRIPT_TO_BOOK_ROADMAP.md` for the subsequent 76.5-hour transcript audit
and the current transcript-backed chapter production sequence.
See `PUBLISHER_STRATEGY.md` for publisher ranking, open-edition contract terms,
proposal positioning, sample-chapter choices, and the inquiry-to-publication plan.

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
| II | 9A | Convolutional Neural Networks: Learning Spatial Structure | 85% | Complete conceptual progression; worked kernel math; shapes, channels, pooling, parameter counts; matched three-lab sequence | Execute and benchmark Keras labs; incorporate student feedback; decide whether augmentation/transfer learning need an optional extension |
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

The transcript audit makes an end-of-year public beta feasible, but only with
strict scope control: one new neural chapter, reinforcement learning optional, and
architecture-specific/tool-specific detail kept in the Practice volume.

| Window | Milestone | Deliverable |
|---|---|---|
| Aug 10–23, 2026 | Architecture and transcript pilot | Chapter 9A is approved and the CNN chapter/labs are drafted with provenance; decide optional-RL status, clean the P44–P48 source sequence, and pilot the workflow on Chapter 5 |
| Aug 24–Sep 27 | Repair foundations | Complete transcript-backed revisions of Chapters 2–6; establish shared datasets, notation, code conventions, and Practice links |
| Sep 28–Nov 1 | Complete the model-learning core | Complete Chapters 7–9, proposed Chapter 9A, and Chapter 15; retain one canonical MLP lab and one end-to-end model-selection case |
| Nov 2–Dec 6 | Complete applications and evaluation | Complete Chapters 10–14 using the INFO300/DSCI471/ProfWKe source sequences; finish retrieval, graphs, evaluation, and modern representation updates |
| Dec 7–20 | Close the lifecycle and framing | Complete Chapter 16; revise Chapter 1 last; finish glossary, accessibility text, citations, figure provenance, and cross-references |
| Dec 21–31 | Alpha freeze and public beta | Execute/render all retained labs; technical and pedagogical review; tag a versioned web/PDF beta; prepare proposal, annotated TOC, sample chapters, and review packet |

If the schedule slips, preserve the completed introductory CNN sequence but defer
optional augmentation/transfer-learning, reinforcement-learning, RNN, and GAN
extensions before reducing the quality of the core chapters.

## Publisher package

Prepare a concise proposal, market/competition analysis, annotated TOC, author biography, course adoption plan, two polished sample chapters, expected word/figure count, schedule, and a stable preview URL. Present the open site as a companion/open-access edition whose license and relationship to the print edition will be negotiated explicitly; do not assume the final publisher license in the source repository.

Recommended sequence: qualify Cambridge first through a short list-positioning and
open-web-rights conversation; proceed to a full Cambridge proposal only if those
terms are viable. MIT Press is the preferred alternative, followed by CRC Press and
Springer Nature. The complete strategy and draft inquiry messages are in
`PUBLISHER_STRATEGY.md`.
