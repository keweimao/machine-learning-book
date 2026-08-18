# Teaching-Materials-to-Book Mapping

Date of review: 2026-08-10

Transcript update: 2026-08-10. The later audit of 76.5 hours of ProfWKe,
DSCI471, and INFO300 recordings is documented in
`planning/TRANSCRIPT_TO_BOOK_ROADMAP.md`. Where the two plans differ, the
transcript-backed plan is the current source-readiness authority.

Teaching-source paths are relative to `/Users/wk77/Documents/git/teach`; book paths
are relative to `/Users/wk77/Documents/git/machine-learning-book`. In each
course-specific assessment, shorter paths inherit that course directory.

This is a planning document. It identifies teaching material that can support the
book, but it does not authorize copying course files into the manuscript. Each
selected source still needs a provenance, permissions, citation, and figure-rights
check during conversion.

## Executive recommendation

The teaching archive can materially accelerate the book. Its strongest use is not
to import whole courses, but to fill six thin core chapters, modernize three mature
chapters, and supply a small number of high-value labs.

The recommended scope is:

1. Keep the existing 16-chapter spine.
2. Add one core chapter, **Neural Networks and Representation Learning**, after
   Chapter 9. This prevents Chapter 7 from becoming an abrupt survey from kNN all
   the way to multilayer networks and gives tensors, training, embeddings, and
   attention a teachable progression.
3. Add **Sequential Decision Making and Reinforcement Learning** only as an
   optional advanced chapter or Practice volume extension. The source is unusually
   complete, but reinforcement learning is not required to repair the main book.
4. Treat anomaly detection as a section spanning Chapters 6 and 10 rather than a
   separate chapter. Defer generic AI search, constraint satisfaction, and most
   association-rule material unless the intended scope broadens from introductory
   machine learning to general AI/data mining.
5. Use transcripts to recover the author's explanations and examples. Do not turn
   sparse or borrowed slides into prose mechanically.

The transcripts change the recommended sequence. Begin with a Chapter 5 pilot
using the focused information/IDF/LIT lecture sequence, then repair Chapters 2–6
in dependency order. Complete Chapters 7–9, the proposed neural chapter, and
Chapter 15 as one model-learning wave. Chapters 10–14 follow, then Chapter 16 and
the final revision of Chapter 1. Chapters 11–12 have unusually rich transcript
support but still require the most careful attribution and modernization review.

## Readiness scale

| Mark | Meaning | Conversion implication |
|---|---|---|
| **A — Ready to adapt** | Substantive editable prose or a coherent notebook exists and appears close to the author's teaching voice. | Convert after provenance, citation, execution, and editorial checks. |
| **B — Strong source** | Substantial content exists, but it is slide-shaped, dated, partly borrowed, in another language/framework, or needs narrative reconstruction. | Use as a source outline; transcript or fresh prose is strongly preferred. |
| **C — Seed only** | A useful outline, example, or code fragment exists, but it cannot support a complete section by itself. | Gather transcript/notes or combine with new research and writing. |
| **D — Defer/exclude** | Duplicated, out of scope, student-owned, operational/private, or too provenance-sensitive for direct use. | Do not import; retain only as a discovery pointer when appropriate. |

“Ready” never means “publish verbatim.” It means there is enough material to begin
an efficient, source-traceable rewrite.

## Chapter-by-chapter mapping

The current completion estimates come from `planning/ROADMAP.md` and should be
re-estimated after each conversion wave.

| Ch. | Current need | Best teaching sources | Proposed contribution | Readiness | Still needed |
|---:|---|---|---|---|---|
| 1 | 65%; learning objectives, modern examples, recap | `DSCI471/Week_01_Intro/lecture_w1_dl.qmd`; selected motivating examples in `INFO629/Week5/Week5.pptx` | A short modern bridge from symbolic programs to learning from data; examples of ML/DL applications | B | Preserve the book's distinctive data-to-meaning thesis; write new objectives/recap; verify all application claims and images |
| 2 | 70%; tables/data frames, missingness, exercises | `INFO634/Spring2021/Week2/A1_solution_ke_comments.ipynb`; `INFO659/LEADS2018/R-Way2CrunchData.Rmd`; `DSCI471/Week2/Lecture/lecture_w2_nn.qmd` | Worked data types, tabular operations, vectors/tensors, shapes, broadcasting, and representation exercises | A/B | Split instructor solution from student exercise; standardize examples in Python; add missing-data treatment in Ch. 6 rather than duplicating it |
| 3 | 55%; dot products, projections, eigenthinking, optimization | `DSCI471/Week2/Lecture/lecture_w2_nn.qmd`; `DSCI471/Week2/Lecture/lecture_w2_foundations.qmd`; `INFO629/Week4/detailed_notes.md`; LEADS matrix examples | Shape-aware vector/matrix computation, dot product, reshaping, linear-model geometry, and light optimization intuition | B | Fresh introductory prose on projections/eigenvectors; small diagrams; clean broken citation placeholders; avoid introducing backprop before the geometry is secure |
| 4 | 75%; descriptive statistics, sampling, uncertainty, exercises | `INFO634/Spring2021/Week2/A1_solution_ke_comments.ipynb`; `INFO629/Week6/Week6_1_ProbabilityIT.pptx`; INFO300 probabilistic-model slides | Descriptive statistics, correlation, distributions, worked probability/classification examples | A/B | Reconcile repeated estimator sections; add sampling distributions/confidence intervals from original notes or a newly written source; check inherited slide provenance |
| 5 | 70%; applications and worked problems | `INFO629/Week6/Week6_1_ProbabilityIT.pptx`; `INFO629/Week6/Probabilisties.pptx`; information-theory segments in INFO300/629 language-model material | Entropy/information gain examples and connections to trees, language modeling, and uncertainty | B | Preserve the book's original LIT framing; derive new worked problems; source thermodynamics claims carefully |
| 6 | 10%; nearly all substantive content | `INFO634/Author/03Preprocessing.ppt`; `INFO659/LEADS2018/R-Way2CrunchData.Rmd`; `INFO659/LEADS2018/R-DataClustering.Rmd`; `INFO634/Spring2020/Week4/12Outlier.ppt`; `LEADING2023/202306_cmd/regex.md`; focused transcripts P10/P15/P32–P34; existing Practice preprocessing/outlier labs | Quality and provenance, cleaning, scaling, encoding, feature construction, text cleaning, outliers, and reproducible preprocessing | B | The focused transcripts now supply outlier and workflow narration; INFO634 preprocessing narration is still missing. Write missingness and leakage/pipeline prose anew. Modernize APIs and replace publisher-derived figures |
| 7 | 75%; trees, calibration, updated neural transition | `INFO629/Week5/Week5_MoreModels.pptx`; `INFO629/Week6/Week6_2_BasicClassification.pptx`; `INFO629/Week6/INFO659-Week7-AdvancedModels.pptx`; `DSCI471/Week2/Lecture/lecture_w2_foundations.qmd`; DSCI471 D02–D05 and focused P16/P26–P29 transcripts | Decision boundaries, Naive Bayes/tree comparison, nonlinear SVM, perceptron, and a concise bridge to neural networks | B/A | Move detailed multilayer training into the proposed new chapter; add probability calibration and a coherent model-selection example; trees still need original narration |
| 8 | 5%; full chapter | `INFO629/Week6/Week6_2_BasicClassification.pptx`; `INFO629/Week5/Week5_MoreModels.pptx`; `INFO629/Week6/INFO659-Week7-EnsembleLearning.pptx`; DSCI471 softmax examples | One-vs-rest/one-vs-one, softmax intuition, decision trees/rules, random forests and multiclass evaluation | B | Original prose for multilabel and ordinal targets; calibration/error-analysis examples; a small multiclass lab; clarify whether ensembles live here or primarily in Ch. 15 |
| 9 | 5%; full chapter | `DSCI471/Week3/Week3_Milad/Linear_Regression_TF.ipynb`; DSCI471 D04–D05/D10 transcripts; focused P32; regression portions of `INFO659/LEADS2018/R-Spark.Rmd` | Linear regression, loss/fitting, tensor shapes, validation, residual/outlier interpretation, and a starter computational example | B | Week 3 transcripts now supply narration, but some code is co-instructor-authored. Write uncertainty, diagnostics, and regularization; use a simple NumPy/sklearn lab before TensorFlow |
| 10 | 65%; density methods, model selection, evaluation | `INFO300/Week8/IRS09-Clustering-v2.pptx`; `INFO629/Week8/Clustering-v3.pptx`; `INFO659/LEADS2018/R-DataClustering.Rmd`; INFO634 clustering notebook; INFO634 outlier deck | Cluster evaluation, initialization sensitivity, HAC/k-means comparison, Scatter/Gather use case, and anomaly connection | B | Existing recovered clustering notebook is already substantially duplicated—do not import it again. Add DBSCAN/density methods and modern validation guidance with fresh sources |
| 11 | 70%; embeddings, modern preprocessing, transformer context | DSCI471 D11–D18 and focused P13/P26/P37/P39 transcripts; `DSCI471/Week6/lecture/lecture_w6_rnn.md`; `DSCI471/Week7/Lecture_DL_chapter10/lecture_w7_modern_rnn_v2.md`; `DSCI471/Week9/lecture_d2l_chapter15/lecture_w9_embedding_v2.md`; `LEADING2023/202306_cmd/regex.md` | Tokenization/vocabulary, subwords, embedding geometry, contextual representations, sequence models, attention, and text-cleaning lab | B/A | The transcripts now supply the author's narrative, but the notes visibly draw on D2L and external figures. Rebuild citations/figures and keep RNN/LSTM details optional so the introduction remains proportionate |
| 12 | 75%; semantic/hybrid retrieval and recommendation | INFO300 I00–I18 and focused P37/P41/P52 transcripts; `INFO300/Week8/IRS89-RelevanceFeedback.pptx`; `INFO300/Week9/IRS9_LM3.pptx`; `INFO300/Week9/IR2LLMs_Ke.md`; link-analysis deck | Rocchio/relevance feedback, language-model retrieval, PageRank bridge, embeddings/semantic retrieval, hybrid search, and a cautious LLM-era update | B/A | The transcripts now supply narration, but many IR slides are inherited/borrowed. Add an original semantic/hybrid retrieval lab and gather author-owned recommender notes rather than importing guest slides |
| 13 | 5%; full chapter | INFO300 I10–I12 transcripts; `INFO300/Week6/IRS06-LinkAnalysis-v2.5.pptx`; `INFO634/Spring2020/Week8/networks.ppt`; `INFO629/Week2/Week2_Part2.pptx` | Graph representation, paths, degree distributions, random walks, PageRank, clustering coefficient, and network models | B | INFO300 now supplies strong PageRank narration. INFO634 networks narration is still missing. Write communities, structural roles, link prediction, and graph-learning overview; redraw every figure |
| 14 | 65%; resampling, significance, uncertainty, fairness | INFO300 I14–I15 and focused P21 transcripts; `INFO300/Week7/IRS07-Evaluation-v4.pptx`; clustering-evaluation materials | Test collections, relevance judgments, precision/recall/F, ranked metrics, DCG/NDCG, clustering metrics, and A/B testing | A/B | The evaluation narrative is now strong. Add cross-validation linkage, bootstrap/significance tests, confidence intervals, subgroup/fairness evaluation, and reproducible reporting from original prose |
| 15 | 10%; nearly all substantive content | DSCI471 D04–D10 transcripts; `INFO629/Week6/INFO659-Week7-EnsembleLearning.pptx`; DSCI471 generalization/regularization and MLP/MNIST materials | Bias–variance, under/overfitting, bagging, boosting, stacking, regularization, callbacks/early stopping, and learning curves | B | DSCI471 supplies regularization/validation narration; the ensemble deck still lacks a transcript. Add CV and leakage-safe tuning; use new figures and a single end-to-end model-selection case |
| 16 | 5%; full chapter | `INFO659/LEADS2018/R-Spark.Rmd`; `INFO300/Week9/IR2LLMs_Ke.md`; DSCI471 introductory hardware/scale notes | Distributed-workflow example, changing compute scale, reproducible execution, LLM risks, human oversight, and responsible use | C/B | Spark APIs are dated. Deployment, drift, privacy, security, energy, and monitoring need current original sources. Gather any deployment/MLOps/ethics lectures before drafting |

## Recommended new core chapter

**Implementation update (August 17, 2026):** the CNN portion is now implemented
as `chapters/09a-convolutional-neural-networks.qmd` with a three-lab matched
practice sequence. Treat the broader sections below as a remaining
representation-learning plan; do not duplicate the completed convolution,
pooling, channel, shape, or MNIST material.

### Neural Networks and Representation Learning

Place this chapter after Numeric Prediction and Regression and before Clustering.
Renumber subsequent chapters only after the table of contents is approved.

This chapter solves two structural problems: Chapter 7 currently jumps too quickly
from classical classification to multilayer networks, while Chapters 11–12 need a
shared foundation for embeddings and attention. It also gives students a place to
learn tensor shape and training mechanics without overloading the matrix chapter.

| Proposed section | Primary source | Readiness | Editorial treatment |
|---|---|---|---|
| From a perceptron to a multilayer network | `INFO629/Week6/INFO659-Week7-AdvancedModels.pptx`; `DSCI471/Week2/Lecture/lecture_w2_foundations.qmd` | B | Begin with one small classification example and connect explicitly to Ch. 7 |
| Tensors, shapes, and batches | `DSCI471/Week2/Lecture/lecture_w2_nn.qmd` | B | Use plain vector/matrix notation first; add a shape table and common-error box |
| Forward computation, activations, and loss | DSCI471 Week 2 notes and MLP notebooks | B | One hand-computed network before framework code |
| Learning by gradient descent and backpropagation | DSCI471 Week 2 foundations and MLP material | B | Explain computational responsibility/chain rule conceptually; defer full derivation |
| Generalization and regularization | DSCI471 Week 2; INFO629 ensemble/bias–variance deck | B | Cross-reference Ch. 15 rather than duplicating model-selection treatment |
| Convolution and sequence models: why architecture matters | `DSCI471/Week4/d2l_chapter7/lecture_w4_cnn.md`; Week 6–7 RNN notes | B | Short overview in core text; detailed CNN/RNN content belongs in boxes or Practice |
| Embeddings and attention | DSCI471 Weeks 9–10 notes | B | Build the bridge to Chs. 11–12; avoid turning the chapter into an LLM survey |
| Lab: an MLP from data to evaluation | `DSCI471/Week3/Week3_Milad/Mnist_MLP_keras.ipynb`; Week 2 notebook | B | Confirm co-instructor permission; simplify and modernize; provide a framework-light alternative |

The DSCI471 source files contain placeholder citation syntax and external/D2L-derived
images. They are strong intellectual scaffolds, not clean manuscript source. During
conversion, reconstruct the bibliography, redraw diagrams, and separate the author's
original explanation from adapted textbook structure.

## Optional advanced extension

### Sequential Decision Making and Reinforcement Learning

`INFO629/Week9/rl_taxi.md` and `INFO629/Week9/rl_taxi.ipynb` form the most complete
standalone new topic in the archive: roughly 4,000 words plus a coherent executable
Q-learning tutorial. Mark this **A — Ready to adapt** after execution and dependency
review.

Recommended sections are agent/environment/reward, states and actions, policies and
value functions, exploration versus exploitation, the Q-learning update, and the
Taxi case study. For the 2026 publication schedule, place this in the Practice volume
or label it an optional advanced chapter. Promoting it to the core manuscript would
also require broader coverage of Markov decision processes, evaluation, safety, and
modern deep RL.

The current Practice volume already contains a recovered reinforcement-learning
extension. Compare provenance and content before adding anything; retain the richer
canonical source rather than creating a duplicate.

## High-value section additions that do not need new chapters

| Addition | Recommended home | Source | Decision |
|---|---|---|---|
| Outliers and anomaly detection | Ch. 6 for detection/cleaning; Ch. 10 for density/cluster perspective | INFO634 `12Outlier.ppt`; existing Practice outlier lab | Add, but rewrite and redraw because the legacy deck may be publisher-derived |
| Decision trees and rule learners | Ch. 8 | INFO629 `Week6_2_BasicClassification.pptx` | Add; an INFO629 transcript or newly written worked example is still needed |
| Bagging, boosting, and stacking | Ch. 15, with a short Ch. 8 cross-reference | INFO629 `INFO659-Week7-EnsembleLearning.pptx` | Add; strong authored structure, limited prose |
| Relevance feedback and Rocchio | Ch. 12 | INFO300 `IRS89-RelevanceFeedback.pptx` | Add; one worked vector-space example and a Practice exercise |
| Language-model retrieval | Ch. 12 | INFO300 `IRS9_LM3.pptx` and related decks | Add selectively; explicitly borrowed source requires fresh derivation and citations |
| Web graphs and PageRank | Ch. 13, cross-referenced from Ch. 12 | INFO300 link-analysis deck; INFO634 networks deck | Add; redraw diagrams and keep PageRank derivation in one chapter only |
| Ranking evaluation and test collections | Ch. 14 | INFO300 evaluation deck | Add; highly aligned and immediately useful once rewritten |
| Text embeddings and subwords | Ch. 11 | DSCI471 Week 9 notes | Add; rebuild citations and figures |
| Attention and transformers | New neural chapter introduction, then Chs. 11–12 applications | DSCI471 Week 10 notes; INFO300 `IR2LLMs_Ke.md` | Add at introductory depth; avoid repeated transformer tutorials |
| Regex/text cleaning | Ch. 6 lab and Ch. 11 cross-reference | LEADING2023 regex tutorial | Add as a short Practice activity, not a theory section |
| Distributed data workflow | Ch. 16 Practice activity | LEADS2018 Spark R Markdown | Use only as a conceptual skeleton; modernize technology and APIs |

## Material to defer from the core book

- INFO629 search, constraint-satisfaction, and case-based-reasoning materials belong
  to a general artificial-intelligence course. They can become a later companion,
  but they do not efficiently close the current manuscript gaps.
- Association-rule and “trend” decks may fit a broader data-mining book, but adding
  them now would compete with higher-priority regression, generalization, graph, and
  deployment chapters. Keep the existing Practice lab as an optional enrichment.
- Student final projects are topic signals only. Do not import prose, slides, code,
  media, or figures without explicit student permission and a documented license.
- Guest-lecturer and co-instructor material—including files labeled with another
  instructor's name—needs authorship confirmation before adaptation.
- Operational class notes and configuration files are not manuscript sources. One
  INFO300 note contains credential-like deployment information; exclude it from all
  imports and audit it separately before making any teaching archive public.

## Course-by-course source assessment

### INFO300 — strongest for retrieval, graphs, and evaluation

Use the 2024 course versions as canonical unless a file-level comparison identifies
a newer authored revision. Strong sources are:

- `Week6/IRS06-LinkAnalysis-v2.5.pptx`: web graphs, citation relationships,
  random walks, PageRank, and teleportation. **B** for Chs. 12–13.
- `Week7/IRS07-Evaluation-v4.pptx`: relevance, test collections, precision/recall,
  ranked metrics, DCG/NDCG, and A/B testing. **B** for Ch. 14.
- `Week8/IRS89-RelevanceFeedback.pptx`: Rocchio and probabilistic relevance
  feedback. **B** for Ch. 12.
- `Week8/IRS09-Clustering-v2.pptx`: HAC, k-means, and cluster evaluation. **B**,
  but substantially overlaps Ch. 10 and INFO629; use only missing examples.
- `Week9/IR2LLMs_Ke.md`: a 2024 editable narrative spanning traditional IR,
  language models, embeddings, attention, LLM applications, hallucination, safety,
  and human–AI collaboration. **B**, because claims and references need careful
  fact-checking and it is broader than one section.
- `Week9/IRS9_LM3.pptx`: language-model retrieval and smoothing. **B**, but the
  deck states that it borrows from named IR researchers; reconstruct from primary
  sources rather than converting slides directly.

The weekly `week*_notes.md` files are schedules/teaching plans and embedded
PowerPoint notes are mostly slide numbers. The separate Spring 2026 INFO300
transcripts now provide the missing lecture narration for Weeks 1–10; see the
transcript roadmap for exact matches.

### INFO624 — older IR archive and exercise reservoir

The lecture decks largely duplicate or precede INFO300. Default to INFO300 for
theory, then use INFO624 only for unique worked examples or assignments:

- `Week3/Assignment/math-assignment.tex` and vector exercises can support Chs. 2–3.
- `Week6/Assignment/Exercise.md` and `Week7/Exercise.md` can support retrieval and
  evaluation practice.
- Vector-space, probabilistic retrieval, link-analysis, evaluation, feedback, and
  clustering decks are superseded unless file comparison proves unique content.

This course is primarily **C** for new theory and **B** for selected exercises.

### INFO629 — strongest for trees, ensembles, and reinforcement learning

- `Week5/Week5_MoreModels.pptx`: metrics, random forests, SVM, and Naive Bayes.
  **B** for Chs. 7–8 and 14.
- `Week6/Week6_2_BasicClassification.pptx`: 1R, decision trees, and Naive Bayes.
  **B** and the best outline for Ch. 8's tree/rule section.
- `Week6/INFO659-Week7-AdvancedModels.pptx`: nonlinear SVM, perceptron, and neural
  networks. **B** for Ch. 7 and the proposed neural chapter.
- `Week6/INFO659-Week7-EnsembleLearning.pptx`: bias/variance, bagging, rotation
  forests, boosting, and stacking. **B** and the best structure for Ch. 15.
- `Week7/NN_Overview.pptx`: a concise bridge from perceptron to transformer,
  residual connections, normalization, and dropout. **C/B**; useful as a checklist,
  not enough narrative by itself.
- `Week9/rl_taxi.md` plus `rl_taxi.ipynb`: complete Q-learning tutorial. **A** for
  an optional advanced chapter/lab.
- `Week4/detailed_notes.md`: readable prose on continuous constraints/linear
  programming and case-based reasoning. **C** for Ch. 3 optimization or a future AI
  extension; not central enough to drive a core section.

Week 1–2 notes are lecture plans, not transcripts. Search/CSP notebooks are good
demos but should remain outside the core ML roadmap. Exclude student projects from
conversion.

### INFO634 — strongest for preprocessing, outliers, and worked foundations

- `Author/03Preprocessing.ppt`: broad preprocessing outline. **B**, with a high
  likelihood of publisher/textbook-derived content; use topic coverage, not wording
  or art.
- `Spring2020/Week4/12Outlier.ppt`: statistical, proximity, density/LOF,
  clustering-based, one-class, contextual, collective, and high-dimensional
  outliers. **B** for Chs. 6 and 10, subject to a full provenance rewrite.
- `Spring2020/Week8/networks.ppt`: network types, degree distributions, clustering
  coefficient, random graphs, scale-free networks, and preferential attachment.
  **B** for Ch. 13, again as an outline rather than copy-ready content.
- `Spring2021/Week2/A1_solution_ke_comments.ipynb`: worked statistics, Iris,
  correlation, similarity, and distance. **A/B** for Chs. 2–4 and Practice. Publish
  a clean student exercise separately from any instructor solution.
- `Spring2021/Week4/assignment_2(3)/assignment_2_final.ipynb` and the INFO634
  clustering notebook are essentially duplicates of material already recovered in
  the Practice volume. **D** for re-import; retain the existing canonical copies.

Prefer Spring 2021 files over Spring 2020 when both are equivalent, but preserve an
older file when it contains unique authored annotations.

### DSCI471 — strongest for a modern neural/representation-learning sequence

The editable 2026 lecture notes provide the clearest modern progression:

- Week 2 foundations and neural-network QMD: tensors, MLPs, activations, forward
  computation, backpropagation, regularization, and shapes. **B**.
- Week 4 CNN Markdown: convolution, locality/weight sharing, padding, stride,
  channels, pooling, and LeNet. **B**; detailed enough for optional boxes/labs.
- Week 6 RNN Markdown: sequence modeling, tokenization/vocabulary, language models,
  perplexity, smoothing, RNNs, BPTT, and clipping. **B**.
- Week 7 modern RNN Markdown: LSTM/GRU gates, equations, memory, and limitations.
  **B**, best kept optional in an introductory book.
- Week 9 embedding Markdown: word2vec, GloVe, fastText, BPE, geometry, evaluation,
  and contextual embeddings. **B** for Ch. 11.
- Week 10 transformer Markdown: Q/K/V attention, masking, multihead attention,
  positional encoding, encoder/decoder models, and foundation-model context. **B**
  for the proposed neural chapter and Chs. 11–12.

Important conversion constraints:

- Week 2 foundations contains unresolved placeholder citation markers.
- Multiple notes closely follow D2L organization and use D2L/external graphics.
  Rebuild citations and produce original figures and examples.
- Files under directories or filenames bearing a co-instructor's name require
  permission/credit confirmation before publication.
- `Week3/Week3_Milad/Linear_Regression_TF.ipynb` has little explanatory text, but
  DSCI471 D04–D05 now supply related lecture/lab narration. It remains subject to
  co-instructor authorship review.
- The MNIST MLP, CNN homework, sequence, embedding, and BERT notebooks are useful
  lab seeds. Prefer one curated lab per major concept rather than importing every
  framework variant.
- `LSTM_Summary_Application.docx` is a strong two-page exercise on shapes,
  parameters, and sequence input. `Week3/MLP_for_Mnist_Summary.docx` is similarly
  useful, but contains inconsistent parameter-total arithmetic that must be fixed.
  `Hyper_parameters_Game.docx` is only a brainstorm and is not content-ready.

### LEADS and LEADING — strongest for compact applied labs

- `INFO659/LEADS2018/R-Way2CrunchData.Rmd`: data loading, sampling, descriptive
  statistics, plotting, vectors/matrices, and joins. **B** for early Practice labs;
  convert to Python or intentionally retain R as an optional track.
- `INFO659/LEADS2018/R-DataClustering.Rmd`: compact end-to-end work across Iris,
  k-means, HAC, Naive Bayes, trees, SVM, evaluation, and tuning. **B** and an
  excellent capstone-lab skeleton for Chs. 6–10 and 14–15.
- `INFO659/LEADS2018/R-Spark.Rmd`: Spark setup, SQL/data operations, regression,
  and clustering. **C/B** for Ch. 16 because the API and setup are dated.
- `LEADING2023/202306_cmd/regex.md`: **B** for a short Ch. 6/11 text-cleaning lab.
- Command-line lesson plans, schedules, and program documents are too thin or
  operational to become book sections.

## Transcript availability and remaining requests

The transcript audit found 86 caption files containing approximately 499,000 words
and 76.5 hours of recording. After four exact duplicates, 82 unique recordings
remain:

| Source | Unique recordings | Strongest book contribution |
|---|---:|---|
| ProfWKe focused lectures | 42 | Probability, outliers, classification, information/IDF/LIT, evaluation, retrieval/LLMs, reinforcement learning, and scale |
| DSCI471 Spring 2026 | 20 | Vectors/tensors, regression/MLPs, CNN/RNN sequence, embeddings, GANs, attention, and transformers |
| INFO300 Spring 2026 | 20 | Indexing, vector/probabilistic retrieval, entropy/IDF, PageRank, evaluation, clustering, language-model retrieval, and relevance feedback |

See `planning/TRANSCRIPT_TO_BOOK_ROADMAP.md` for canonical transcript IDs,
duplicate handling, lecture-by-lecture matches, chapter coverage, and the optimized
conversion sequence.

The transcripts satisfy the earlier requests for DSCI471 Weeks 2–10 and INFO300
Weeks 1–10. The following source requests remain valuable:

| Priority | Missing source | Why it still matters | Target |
|---:|---|---|---|
| 1 | INFO634 preprocessing lecture transcript or original authored notes | Chapter 6 still lacks a complete narrative for missing data, encoding, feature selection, and pipelines | Ch. 6 |
| 1 | INFO629 trees and ensemble lecture transcripts | Focused classification recordings do not fully cover trees, multiclass decisions, bias–variance, bagging, boosting, or stacking | Chs. 8 and 15 |
| 2 | Deployment/MLOps, drift, privacy, security, fairness, and sustainability lectures or notes | Scale/history recordings do not complete the production/responsibility lifecycle | Ch. 16 |
| 2 | Original graph/community/link-prediction teaching material | INFO300 transcripts strongly cover PageRank but not the rest of structural analysis | Ch. 13 |
| 3 | Source lists, original figures, and reading annotations for DSCI471/INFO300 | Needed to replace D2L-derived and inherited slide structures with publication-safe sources | Neural chapter; Chs. 11–14 |

For any additional recording, retain the raw timestamped transcript, exact
slides/notebook, assignment/solution, reading list, authorship note, and board/live
code artifacts. Raw transcripts should remain unchanged; create a separate cleaned
working version during conversion.

## Feasible conversion roadmap

### Phase 0 — source control, provenance, and scope lock (2–4 working days)

- Approve the proposed neural chapter and decide whether RL remains optional.
- Choose one code baseline for core labs. Recommendation: Python with NumPy,
  pandas, scikit-learn, and only selective Keras/PyTorch examples.
- Decide whether R/Spark examples are optional language tracks or conceptual source
  only. For schedule control, use them as source material and publish Python-first.
- Build a source ledger with author, course/date, original/adapted status, external
  readings, figures, permissions, target section, and conversion status.
- Quarantine credential-bearing operational notes and exclude student work.

### Wave 1 — repair the core learning sequence (4–6 weeks)

1. **Chapter 6:** preprocessing, quality, encoding, outliers, leakage, pipeline lab.
2. **Chapter 8:** multiclass strategies, softmax, trees/rules, calibration.
3. **Chapter 9:** linear regression, loss, regularization, diagnostics, starter lab.
4. **Chapter 15:** bias–variance, CV, learning curves, tuning, ensembles.

These chapters should share one tabular dataset where practical. Reusing a coherent
case reduces cognitive load and makes leakage, model choice, and evaluation visibly
connected.

### Wave 2 — add the neural bridge and modern representations (3–5 weeks)

1. Draft the new neural chapter at introductory depth.
2. Update Ch. 11 with embeddings/subwords and a short sequence-model context.
3. Update Ch. 12 with relevance feedback, language-model retrieval, semantic and
   hybrid retrieval.
4. Add one MLP lab and one embedding/retrieval lab; keep CNN/RNN/transformer labs
   optional.

This wave should begin only after DSCI471 citations, external graphics, and
co-instructor authorship are resolved.

### Wave 3 — graphs, evaluation, and deployment (3–5 weeks)

1. Draft Ch. 13 around one graph vocabulary and one PageRank example.
2. Complete Ch. 14's ranked metrics, uncertainty, significance, and fairness.
3. Draft Ch. 16 using a modern, tool-neutral lifecycle: scale, reproducibility,
   deployment, drift, privacy/security, energy, and human oversight.
4. Modernize the Spark concept as an optional Practice activity rather than tying
   the theory chapter to a fragile environment.

### Wave 4 — integration and optional extensions (2–3 weeks)

- Adapt the RL tutorial if schedule permits.
- Add cross-references from theory sections to the selected Practice activities.
- Remove duplicated labs and framework variants.
- Execute every retained notebook in a clean environment; record dependencies and
  fixed random seeds where appropriate.
- Run technical, pedagogical, accessibility, citation, figure-rights, and PDF/web
  render reviews before manuscript freeze.

## Conversion definition of done

A teaching source becomes a book section only when all of the following are true:

- The section has a clear learning objective and prerequisite link.
- Prose is rewritten for a reader who was not present in the lecture.
- Definitions, notation, and terminology match the rest of the book.
- Claims have durable citations; placeholder citations are gone.
- Every borrowed/adapted component is recorded in the source ledger.
- Figures are original, licensed, or redrawn with source attribution and alt text.
- Examples are correct by hand or by an accompanying test/notebook.
- Code runs from a clean environment and avoids obsolete APIs.
- Instructor solutions are separated from public student-facing exercises.
- The section ends with a concise theory-to-practice link.
- The HTML and PDF outputs both render correctly.

## Decisions needed before conversion

1. Approve or reject the new **Neural Networks and Representation Learning** core
   chapter. Recommendation: approve.
2. Decide whether reinforcement learning is an optional web/Practice extension or
   a numbered core chapter. Recommendation: optional extension for the first
   publication.
3. Decide whether to publish only Python labs or retain selected R labs.
   Recommendation: Python-first, with R sources used to reconstruct examples.
4. Confirm authorship/permission for co-instructor and guest-lecture files.
5. Build source packages for the transcripts already gathered and pursue the
   remaining INFO634/INFO629 and deployment/graph sources listed above.
6. Decide whether anomaly detection receives a named Ch. 6 section and Ch. 10
   cross-reference. Recommendation: yes.

## Immediate next action after plan approval

Create a conversion ledger and start with a single pilot: **Chapter 5, Information,
Entropy, and Divergence**. The P44–P48 focused recordings form a coherent authored
sequence and Chapter 5 already has enough manuscript structure to test transcript
cleaning, provenance, mathematical verification, cross-references, and publication
rendering without simultaneously inventing an entire chapter. Follow immediately
with Chapter 6 as the first major gap-filling conversion.
