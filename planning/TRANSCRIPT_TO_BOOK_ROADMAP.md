# Transcript-to-Book Mapping and Conversion Roadmap

Date of review: 2026-08-10

Status: planning only. No transcript text has been converted into manuscript prose.

Source root: `/Users/wk77/Documents/git/teach/Transcripts`

Related plans:

- `planning/TEACHING_MATERIALS_MAPPING.md`
- `planning/ROADMAP.md`
- `planning/PRACTICE_VOLUME_AUDIT.md`

## Executive conclusion

The newly gathered transcripts substantially change the book's source readiness.
The archive now contains the author's spoken explanations for most of the book's
mathematical foundations, classical classification, deep-learning progression,
text and retrieval sequence, PageRank, evaluation, clustering, language modeling,
embeddings, attention, reinforcement learning, and large-scale computing.

The transcript archive contains:

| Source | Files | Recorded time | Approx. words | Unique recordings |
|---|---:|---:|---:|---:|
| ProfWKe focused lectures | 45 | 22.5 hours | 165,695 | 42 |
| DSCI471 Spring 2026 | 20 | 26.6 hours | 168,203 | 20 |
| INFO300 Spring 2026 | 21 | 27.4 hours | 165,472 | 20 |
| **Total** | **86** | **76.5 hours** | **499,370** | **82** |

The focused ProfWKe recordings are generally the closest to book-ready because
they are concise, single-topic lectures in the author's voice. The live course
recordings are richer in explanation, worked examples, student questions, and
misconceptions, but require removal of logistics, incidental conversation, and
automatic-caption errors.

The primary recommendation remains to retain the existing 16-chapter spine and
add one core chapter, provisionally numbered **9A: Neural Networks and
Representation Learning**. The transcript evidence makes that chapter much more
feasible. Reinforcement learning should remain an optional advanced chapter or
Practice-volume extension for the first edition. Generative adversarial networks
should be a short optional box or web supplement, not a new core chapter.

## Canonical transcript identifiers

The downloaded filenames do not contain titles or dates. Use the following stable
IDs in planning and provenance records without renaming the originals yet:

- `P08`–`P52`: ProfWKe `captions (N).sbv`.
- `D00`: DSCI471 `DSCI 471-transcript.vtt`; `D01`–`D19`: the corresponding
  parenthesized file number.
- `I00`: INFO300 `INFO 300-transcript.vtt`; `I01`–`I20`: the corresponding
  parenthesized file number.

Four downloads are exact textual duplicates and should not be converted twice:

| Duplicate | Canonical copy | Treatment |
|---|---|---|
| `P14` | `P13` | Retain one provenance record; exclude duplicate from conversion |
| `P17` | `P16` | Retain one provenance record; exclude duplicate from conversion |
| `P51` | `P45` | Retain one provenance record; exclude duplicate from conversion |
| `I19` | `I18` | Retain one provenance record; exclude duplicate from conversion |

## Readiness interpretation for transcripts

| Mark | Meaning | Required work |
|---|---|---|
| **T-A** | Focused, coherent, author-delivered explanation with enough substance for a section | Clean captions; check math/facts; align terminology; add citations and original figures |
| **T-B** | Rich live lecture with substantial usable explanation | Segment by topic; remove logistics/chatter; repair ASR; reconcile with exact slides/notebook; rewrite for readers |
| **T-C** | Useful example, bridge, lab narration, or partial topic | Combine with written sources and new prose; do not treat as a complete section |
| **T-D** | Duplicate, student presentation, operational material, or out of core scope | Exclude or defer; preserve only a provenance pointer |

Transcripts are evidence of the author's teaching voice, not a verbatim manuscript.
Spoken repetition, class logistics, student-identifying remarks, and transcript
errors must not enter the public book.

## DSCI471 Spring 2026 sequence and source connections

The sequence below is supported by the 2026 syllabus, explicit week references in
the recordings, and topic matches to the course folders.

| ID | Inferred lecture | Matching teaching materials | Book use | Status |
|---|---|---|---|---|
| D00 | Week 1: course introduction, deep learning in data science, history and scope | `DSCI471/Week_01_Intro/lecture_w1_dl.qmd`; Week 1 intro slides | Ch. 1 motivation; Ch. 16 compute/history context | T-B |
| D01 | Week 1: environment, vectors/matrices/tensors, rank, dimension, shape, data representation | `Week_01_Intro/lab_01.qmd`; `Week_01_Lab/lab_w1_prep.ipynb`; Week 2 representation notes | Chs. 2–3; neural chapter prerequisites | T-B |
| D02 | Week 2: neural-network and deep-learning foundations survey | `Week2/Lecture/lecture_w2_foundations.qmd`; `DSCI471Week2.pptx` | Ch. 7 bridge; neural chapter | T-B |
| D03 | Week 2: visual network intuition, basic mathematics, activations, forward computation, code | `Week2/Lecture/lecture_w2_nn.qmd`; `Week2/Week2_Milad/Week2.ipynb` | Ch. 3 shapes; neural chapter; Practice lab | T-B; permission check for co-instructor files |
| D04 | Week 3: multilayer networks, loss, derivatives, optimization, housing/MNIST examples | `Week3/DSCI471-Week3.pptx`; `Multilayer Perceptrons.pptx`; Week 3 notebooks | Ch. 9 regression; neural chapter | T-B |
| D05 | Week 3 lab: end-to-end MLP/regression or MNIST workflow and troubleshooting | `Linear_Regression_TF.ipynb`; `Mnist_MLP_keras.ipynb`; `MLP_for_Mnist_Summary.docx` | Ch. 9 and neural Practice labs | T-B/C; resolve co-instructor authorship and arithmetic typo |
| D06 | Week 4: CNN introduction plus regularization, dropout, and training concerns | `Week4/d2l_chapter7/lecture_w4_cnn.md`; `DSCI471-CNN.pptx` | Neural chapter architecture overview; Ch. 15 regularization | T-B |
| D07 | Week 4 lab: visualizing convolution, kernels, pooling, and feature maps | Week 4 CNN notebooks and homework | Optional neural Practice lab | T-B; separate assignment from solution |
| D08 | Week 5: CNN continuation, architectures, image inputs, kernels, and layers | `Week5/DSCI471-CNN-Part2.pptx` | Optional neural architecture section | T-B |
| D09 | Week 5 lab: CNN on MNIST, channels, dimensions, outputs, and debugging | `Week4/DSCI471_HW2.ipynb`; Week 4–5 notebooks | Optional CNN lab and shape-error case study | T-B |
| D10 | Week 6 transition: CNN channels, house-price regression/validation, sequence data | `Week6/Sequence Model.pptx`; Week 3 regression notebooks; Week 6 notes | Ch. 9; Ch. 15; transition to Ch. 11 | T-B/C because it spans topics |
| D11 | Week 6: sequence prediction, tokenization, vocabulary, language-model probability, RNN introduction | `Week6/lecture/lecture_w6_rnn.md` | Ch. 11; neural chapter | T-B |
| D12 | Week 7: vanilla RNN, hidden state, sequence mapping, and training mechanics | Week 6–7 RNN notes; `lab_rnn_lm_note.md` | Neural chapter optional section; Ch. 11 context | T-B |
| D13 | Week 7: LSTM, gates, memory, and long-range dependencies | `Week7/Lecture_DL_chapter10/lecture_w7_modern_rnn_v2.md`; LSTM handout | Optional neural section and Practice exercise | T-B |
| D14 | Week 8 transition: GRU and comparison with LSTM; attention preview | Week 7 modern-RNN notes | Optional neural section; attention bridge | T-B/C |
| D15 | Week 8: reinforcement learning, agents, states, actions, rewards, policies, and learning | `Week8_RL/rl_taxi.md`; `rl_taxi.ipynb`; RL exercise notebooks | Optional RL chapter/Practice | T-B, paired with T-A focused lecture P23 |
| D16 | Week 9: word representations, word2vec-style objectives, context, geometry, and analogy | `Week9/lecture_d2l_chapter15/lecture_w9_embedding_v2.md`; Week 9 notebooks | Ch. 11; neural chapter | T-B |
| D17 | Week 9: GANs, generator/discriminator training, embedding continuation, attention bridge | `lecture_w9_gan_v2.md`; `Generative Deep Learning(3).pptx`; Week 9 notebooks | Optional generative-model box; Ch. 11/neural bridge | T-B/C |
| D18 | Week 10: attention, Q/K/V, positional encoding, encoder–decoder, transformers, implications | `Week10/lecture_d2l_chapter11/lecture_w10_transformer_long.md` | Neural chapter; Chs. 11–12; Ch. 16 implications | T-B |
| D19 | Final student presentations | Project materials | Instructor recap only, if any; do not use student presentation content | T-D |

### DSCI471 editorial implications

- D01–D05 provide the missing spoken bridge from vectors and shapes to regression,
  MLPs, loss, and optimization. This supports a gentler transition than the current
  Chapter 7 jump to multilayer networks.
- D06–D14 contain more architecture depth than the core book needs. Use CNN/RNN/
  LSTM/GRU as examples of inductive bias and data structure; move full derivations
  and framework walkthroughs to Practice.
- D16–D18 provide the best modern representation-learning progression in the
  archive. Reconcile them with the D2L-derived written notes and create original
  examples, diagrams, and citations.
- D17's GAN material is valuable but not structurally necessary. A concise
  discriminative-versus-generative box is sufficient for the first edition.

## INFO300 Spring 2026 sequence and source connections

| ID | Inferred lecture | Matching teaching materials | Book use | Status |
|---|---|---|---|---|
| I00 | Week 1: information retrieval scope, search, information processing, and modern language models | `Week1/IRS01-Introduction-v4.pptx` | Chs. 1 and 12 | T-B |
| I01 | Week 1 lab/continuation: document–term matrix, inverted index, and Elastic representation | Week 1 Elastic slides/lab; Week 2 bag-of-words deck | Chs. 11–12 and Practice | T-B |
| I02 | Week 2: Boolean retrieval, inverted indexing, and Elastic query implementation | `Week2/IRS02-BagWords-v4.pptx`; Elastic documentation exercises | Ch. 12; Practice | T-B |
| I03 | Week 2 lab: analyzers, normalization, mappings, field types, and indexing choices | Week 2 notes and Elastic exercises | Ch. 6 text preparation; Ch. 12 Practice | T-B |
| I04 | Week 3: vector-space retrieval, term weighting, and representation | `Week3/IRS03-VectorSpace-v6.pptx` | Chs. 3, 11, and 12 | T-B |
| I05 | Week 3 continuation: vectors, similarity, document/query comparison, analyzer effects | Week 3 vector-space decks | Ch. 3 geometry; Chs. 11–12 | T-B |
| I06 | Week 4: probabilistic retrieval foundations | `Week4/IRS04-Probabilistic-v6.pptx` | Ch. 4; Ch. 12 | T-B |
| I07 | Week 4 continuation: probability estimation and probabilistic ranking | Week 4 annotated/probabilistic decks | Ch. 4; Ch. 12 | T-B |
| I08 | Week 5: binary independence model, relevance probability, BM25 components, saturation and length normalization | Week 4–5 probabilistic and scoring materials | Ch. 12; Ch. 14 examples | T-B |
| I09 | Week 5: Shannon entropy, uncertainty, IDF, distributions, and divergence | Week 5 scoring material; book's existing information chapter | Ch. 5; Chs. 11–12 | T-B, reinforced by focused P44–P48 |
| I10 | Week 6 transition: custom scoring/similarity in Elastic and web-search challenges | Week 5 scoring slides; `Week6/IRS06-LinkAnalysis-v2.5.pptx` | Ch. 12 and Practice | T-B |
| I11 | Week 6: web graphs, link/citation analysis, anchor text, random walks, and PageRank intuition | `Week6/IRS06-LinkAnalysis-v2.5.pptx` | Chs. 12–13 | T-B |
| I12 | Week 7 transition: PageRank calculation, convergence, and feature-based scoring/ranking | Link-analysis deck; Week 7 exercise | Chs. 12–13; Practice | T-B |
| I13 | Week 7 lab: importing real data into Elastic, mappings, multi-field scoring, and ranking experiments | Week 7 exercise and Elastic files | Ch. 12 Practice; Ch. 14 experiment setup | T-B |
| I14 | Week 8: evaluation foundations, relevance, system comparison, precision, recall, averaging | `Week7/IRS07-Evaluation-v4.pptx` | Ch. 14 | T-B, reinforced by focused P21 |
| I15 | Week 8 continuation: ranked evaluation/DCG-style reasoning and clustering introduction | Evaluation deck; `Week8/IRS09-Clustering-v2.pptx` | Chs. 10 and 14 | T-B |
| I16 | Week 9: HAC, k-means, cluster evaluation/purity, then language-model introduction | Clustering deck; Week 9 language-model slides | Chs. 10–12 | T-B; segment into separate source units |
| I17 | Week 9: language-model retrieval, query likelihood, zero probabilities, and smoothing | `Week9/IRS9_LM3.pptx` and related decks | Chs. 11–12 | T-B; inherited slides require primary-source reconstruction |
| I18 | Week 10: relevance feedback, representation learning, word embeddings, token context, and modern language models | `Week8/IRS89-RelevanceFeedback.pptx`; `Week9/IR2LLMs_Ke.md`; LM decks | Neural chapter; Chs. 11–12 | T-B |
| I19 | Exact duplicate of I18 | Same as I18 | None | T-D |
| I20 | Final synthesis: computing history, information systems, search, AI transition, and future perspective | Final vision lecture; related ProfWKe P50 | Chs. 1 and 16 | T-B/C |

### INFO300 editorial implications

- I04–I12 create a continuous mathematical story from vectors through probability,
  entropy, ranking, web graphs, and PageRank. That story can strengthen
  cross-chapter transitions rather than producing isolated lecture-derived blocks.
- I14–I15 plus P21 are sufficient to reconstruct the retrieval-evaluation portion
  of Chapter 14 in the author's voice.
- I16 must be split: clustering belongs in Chapter 10; language modeling belongs
  in Chapters 11–12.
- I17–I18 contain valuable spoken explanations, but their matching slides include
  inherited material. Use the transcript to identify the author's framing, then
  rebuild equations, examples, citations, and figures from primary sources.
- I13 is especially useful as a Practice lab source, but product-specific Elastic
  commands should be isolated from the durable theory.

## ProfWKe focused-lecture inventory

The focused recordings are grouped below by their best book use. Every unique
recording is accounted for; duplicate IDs are listed separately.

### Mathematical and conceptual foundations

| IDs | Inferred topic | Related materials | Primary destination | Status |
|---|---|---|---|---|
| P09 | Data types, variables, values, and distributions | INFO634 foundation exercises; LEADS data R Markdown | Chs. 2 and 4 | T-A |
| P15 | Data analytics/mining process from problem to data and modeling | INFO634/LEADS workflow materials | Chs. 1, 6, and 15 | T-A |
| P18 | Sets, intersections/unions, vectors, similarity, and distance | Current Chs. 2–3; INFO624 vector exercises | Chs. 2–3 | T-A |
| P20 | Data-mining overview within data science and knowledge discovery | INFO634 introductory materials | Ch. 1 | T-A/B |
| P25 | Python data types and application-level representations | Existing Practice Python materials | Practice toolkit; Ch. 2 cross-reference | T-A for Practice |
| P50 | Long view of computing, information, learning, and modern AI/LLMs | I20 and D00 | Chs. 1 and 16 | T-A/B |

### Probability, information, and term weighting

| IDs | Inferred topic | Related materials | Primary destination | Status |
|---|---|---|---|---|
| P08 | Joint/conditional probability and Naive Bayes | Ch. 4 draft; INFO629/INFO300 probability decks | Ch. 4; Chs. 7 and 11 applications | T-A |
| P12 | Discrete and continuous probability distributions | Ch. 4 draft | Ch. 4 | T-A |
| P44 | From information theory to term weighting and divergence | Ch. 5; INFO300 I09 | Chs. 5, 11, and 12 | T-A |
| P45 | IDF heuristic and document-frequency intuition | INFO300 term-weighting slides | Chs. 5, 11, and 12 | T-A |
| P46 | IDF probabilistic interpretation | INFO300 probabilistic retrieval material | Chs. 5 and 12 | T-A |
| P47 | Motivation and intuition behind Least Information Theory | Existing Ch. 5 LIT section and original research | Ch. 5 | T-A, subject to research citation check |
| P48 | Information-theoretic view of IDF, entropy, and probability | Ch. 5; INFO300 I09 | Chs. 5, 11, and 12 | T-A |

P44–P48 are a distinctive authored sequence and should be treated as a coherent
source collection, not five unrelated excerpts. A carefully edited sequence could
become one of the book's signature contributions while avoiding repeated IDF
explanations across Chapters 5, 11, and 12.

### Data preparation, outliers, classification, and neural models

| IDs | Inferred topic | Related materials | Primary destination | Status |
|---|---|---|---|---|
| P10 | Taxonomy of supervised, unsupervised, statistical, proximity, density, and clustering-based outlier detection | INFO634 `12Outlier.ppt`; Practice outlier lab | Chs. 6 and 10 | T-A |
| P32 | Applied outlier example using distribution, regression, residual/error, and data context | INFO634 outlier material | Ch. 6; Chs. 9–10 | T-A |
| P16 | Linear classification, boundaries, positive/negative cases, and geometry | Ch. 7; INFO629 advanced/basic classification decks | Ch. 7 | T-A |
| P26 | Probabilistic text classification and Naive Bayes spam example | Chs. 4, 7, and 11 | Ch. 11 application; Ch. 7 cross-reference | T-A |
| P27 | Binary classification, feature space, distance, and linear decision functions | Ch. 7 | Ch. 7 | T-A |
| P29 | Nonlinear classification, hidden layers, weights, functions, and neural models | INFO629 advanced-model deck; DSCI471 D02–D05 | Ch. 7 bridge; neural chapter | T-A |

The focused classification sequence is strong, but it does not replace missing
original coverage of decision trees, multiclass decomposition, multilabel/ordinal
decisions, calibration, or ensembles.

### Text, search, evaluation, and modern language models

| IDs | Inferred topic | Related materials | Primary destination | Status |
|---|---|---|---|---|
| P13 | Text as data, terms, documents, document–term representation, and weighting | INFO300 Week 2; Ch. 11 | Ch. 11 | T-A |
| P21 | Full retrieval-evaluation lecture: relevance, precision, recall, ranked results, and system comparison | INFO300 evaluation deck; I14–I15 | Ch. 14 | T-A |
| P37 | Information retrieval and large language models: structure, meaning, models, applications, and limits | `INFO300/Week9/IR2LLMs_Ke.md`; DSCI471 Week 10 | Chs. 11, 12, and 16 | T-A/B |
| P39 | Exploratory analysis/language modeling with Shakespeare plays | `INFO300/Week9/Shake_LM/Shakespeare_LM.ipynb` and `.md` | Ch. 11 Practice | T-A for lab narration |
| P41 | Search-engine index construction and scoring improvement exercise | INFO300 Elastic labs | Ch. 12 Practice | T-A/B; isolate product-specific commands |
| P52 | Introduction to information retrieval and search | INFO300 Week 1 introduction | Ch. 12 | T-A |

### Reinforcement-learning and game-bot sequence

| IDs | Inferred topic | Related materials | Primary destination | Status |
|---|---|---|---|---|
| P11 | Tic-tac-toe project part 1: game representation/interface foundation | `INFO629/tic/`; DSCI471 Week 8 RL exercises | Optional RL Practice | T-A/B |
| P35 | Project part 2: game logic, winner/reset behavior, and state handling | Same game files | Optional RL Practice | T-A/B |
| P38 | Project part 3: first/random bot and action logic | Same game files | Optional RL Practice | T-A/B |
| P22 | Project part 4: state/action values and learning game behavior | Same game files | Optional RL Practice | T-A/B |
| P23 | Conceptual reinforcement-learning lecture: agent, state, action, reward, policy/value, exploration | `INFO629/Week9/rl_taxi.md`; DSCI471 D15 | Optional RL chapter | T-A |

The canonical pedagogical sequence is P23 for concepts, then P11 → P35 → P38 →
P22 for the game-building project. The Taxi tutorial is a shorter alternative lab.
Do not publish both labs at full length in the core path; offer one as the primary
activity and one as an optional extension.

### Scale, data tools, and supplemental computing practice

| IDs | Inferred topic | Related materials | Primary destination | Status |
|---|---|---|---|---|
| P19 | Python/Jupyter setup | Existing Practice setup materials | Practice toolkit | T-A/B; update environment |
| P24 | Stacks, queues, and deques | General programming materials | Defer from ML core | T-D/C |
| P28 | NoSQL/MongoDB concepts | INFO629 Python/data references | Optional data-engineering Practice | T-C |
| P30 | JSON representation and Python processing | Existing Practice JSON/data materials | Practice toolkit | T-A/B |
| P31 | Relational databases and SQL | Existing SQLite/SQL Practice labs | Practice toolkit | T-A/B |
| P33 | Command-line data management and text processing, part 1 | LEADING2023 command-line lesson | Practice toolkit; Ch. 6 lab | T-A/B |
| P34 | Python text-file processing | Existing Python file-processing lab | Practice toolkit | T-A |
| P36 | MongoDB/JSON worked example | MongoDB course files | Optional Practice | T-C |
| P40 | Spark hands-on exercise | LEADS2018 Spark R Markdown | Ch. 16 Practice | T-A/B; modernize APIs |
| P42 | Large-scale data-intensive computing, Hadoop/Spark concepts | LEADS/INFO659 scale materials | Ch. 16 | T-A/B |
| P43 | APIs and JSON using a public-service example | Python/API materials | Optional Practice toolkit | T-A/B; replace unstable API |
| P49 | Command-line exercise, part 2 | LEADING2023 command-line materials | Practice toolkit | T-A/B |

These sources should not expand the theory book into a programming/database manual.
Retain a compact Practice toolkit and point to only those tools required by book
labs. P40, P42, and P50 are the most relevant to Chapter 16.

### Focused-lecture duplicates

- P14 duplicates P13.
- P17 duplicates P16.
- P51 duplicates P45.

## Revised chapter-by-chapter source map

The coverage rating describes transcript support, not overall chapter completion.

| Ch. | Transcript support | What the transcripts can add or improve | Coverage after transcript discovery | Important remaining gaps |
|---:|---|---|---|---|
| 1 | D00, I00, I20, P15, P20, P50 | Stronger motivation; history from data/information systems to ML; human and technological context | **Strong enrichment** | Final thesis and examples should be written after all later chapters stabilize |
| 2 | D01, P09, P18, P25 | Data types, values, sets, vectors, tensor rank/shape, novice misconceptions | **Strong** | Tables/data frames, measurement semantics, missingness cross-reference, polished exercises |
| 3 | D01–D04, I04–I05, P18, P27 | Vector/matrix shape, dot-product intuition, similarity, linear functions, decision geometry, optimization bridge | **Strong for basics** | Projections, eigenthinking, careful transpose explanation, original diagrams, restrained calculus |
| 4 | I06–I09, P08, P12, P26, P44, P48 | Joint/conditional probability, distributions, estimation, Bayesian reasoning, uncertainty, applications | **Very strong** | Sampling uncertainty/confidence intervals and removal of duplicated estimator prose |
| 5 | I09, P44–P48 | A coherent authored path through entropy, divergence, IDF, and LIT motivation | **Very strong/signature** | Research citations, mathematical verification, separation of general theory from retrieval applications |
| 6 | I03, P10, P15, P32, P33–P34 | Data process, text normalization, outlier taxonomy and examples, practical cleaning workflow | **Moderate** | Missing values, categorical encoding, leakage, reproducible pipelines, feature selection/dimensionality reduction still require fresh prose |
| 7 | D02–D05, P08, P16, P26–P29 | Linear/nonlinear boundaries, probabilistic classification, perceptron-to-MLP bridge, worked examples | **Strong** | Decision trees, calibration, consistent model comparison, clearer separation from Ch. 8 and neural chapter |
| 8 | D03–D05 and D10 for softmax/output shapes; P16/P27 classification context | Better multiclass motivation, output representation, loss/shape explanation | **Partial** | One-vs-rest/one-vs-one, trees/rules, multilabel, ordinal decisions, calibration, multiclass error analysis |
| 9 | D04–D05, D10, P32 | Housing-price example, linear regression workflow, loss, validation, residual/outlier connection | **Moderate/stronger than before** | Framework-light derivation, regularization, uncertainty, diagnostics, nonlinear regression |
| 9A | D02–D18, P29, P37 | Full introductory neural progression: tensors, layers, activations, forward/loss/backprop intuition, training, regularization, architectures, embeddings, attention | **Very strong** | Ruthless scope control, original figures, D2L/source attribution, one canonical lab |
| 10 | I15–I16, P10, P32 | HAC, k-means, evaluation/purity, cluster use cases, outlier connection | **Strong for existing methods** | Density methods/DBSCAN, scalability, stability/model selection, repaired equations/figures |
| 11 | D11–D18, I16–I18, P13, P26, P37, P39, P44–P48 | Tokenization, probability, text classification, embeddings, contextual meaning, sequence models, attention/transformers | **Very strong** | Avoid overbreadth; create one progression from symbolic counts to learned representations; modern evaluation lab |
| 12 | I00–I18, P37, P41, P45–P46, P52 | Complete retrieval progression: indexing, vector/probabilistic scoring, BM25, PageRank bridge, feedback, language-model and semantic retrieval | **Very strong** | Hybrid retrieval/recommendation synthesis, durable tool-neutral lab, primary-source citations for inherited slides |
| 13 | I10–I12, P42 for network/scale context | Web as graph, links/citations, random walks, PageRank intuition and calculation | **Strong for PageRank** | General graph traversal, centralities beyond PageRank, communities, roles, link prediction, graph learning |
| 14 | I13–I15, P21 | Relevance judgments, precision/recall, averaging, ranked metrics, experimental comparison, practical evaluation setup | **Very strong for IR evaluation** | Bootstrap/significance, uncertainty, fairness/subgroup evaluation, regression and clustering integration |
| 15 | D04–D10, P15, P29 | Under/overfitting, validation behavior, regularization/dropout, training diagnostics, data/model workflow | **Moderate** | Bias–variance synthesis, CV, learning curves, leakage-safe tuning, bagging/boosting/stacking still rely on slides/new prose |
| 16 | D00, D18, I20, P37, P40, P42, P50 | Compute/history, distributed processing, AI/LLM implications, scale, limits, and human perspective | **Moderate/strong for framing** | Deployment, monitoring/drift, privacy/security, fairness, energy accounting, reproducible production pipelines |
| Optional RL | D15, P11/P22/P23/P35/P38, written Taxi/game materials | Complete conceptual introduction plus two possible hands-on arcs | **Very strong** | Choose one primary lab; add evaluation/safety context; keep optional for schedule control |

## Scope and depth decisions

### Include in the core theory volume

- Shape-aware vectors/matrices and a gentle optimization bridge.
- Probability, information, and the authored entropy–IDF–LIT sequence.
- Data preparation, outliers, and leakage-aware pipelines.
- Classical classification, multiclass decisions, regression, clustering, and
  generalization/model selection.
- An introductory neural/representation-learning chapter.
- A clean progression from term counts to embeddings and attention.
- Classical, probabilistic, semantic, and hybrid retrieval.
- Graph foundations and PageRank, with a concise graph-learning outlook.
- Evaluation across classification, regression, clustering, and ranking.
- Scale, deployment lifecycle, and responsible use.

### Include briefly or as optional boxes

- CNNs as locality/weight-sharing examples.
- RNN/LSTM/GRU as sequence-model history and architectural bias.
- GANs as a discriminative-versus-generative case study.
- Product-specific Elastic examples.
- Spark as a scale/distribution case study.

### Put in the Practice volume or defer

- Full TensorFlow/Keras walkthroughs and architecture-specific troubleshooting.
- Full Tic-tac-toe and Taxi RL projects; choose one primary and one optional.
- General Python, command line, SQL, JSON, API, and MongoDB instruction beyond the
  minimum toolkit needed for labs.
- Generic AI search/CSP and student presentation material.

## Optimized chapter-production sequence

This is an authoring sequence, not a proposed reading order. It resolves
dependencies and creates reusable examples before later chapters need them.

### Stage 0 — transcript curation and architecture lock

1. Approve Chapter 9A and optional-RL status.
2. Create a machine-readable provenance manifest keyed by the canonical IDs above.
3. For each selected recording, preserve raw captions and create a cleaned working
   transcript with timestamps, speaker labels, topic boundaries, slide/notebook
   match, and redaction notes.
4. Remove exact duplicates and exclude D19 student presentations.
5. Establish one shared tabular case, one text/search corpus, and one graph case for
   reuse across chapters.

### Stage 1 — repair foundations in dependency order

#### Chapter 2 — Data Types and Representations

- Use D01, P09, and P18 to improve values, types, sets, vectors, rank, dimension,
  and shape.
- Add a compact “shape before computation” convention used throughout the book.
- Add concept checks based on the student questions/misconceptions in D01.
- Keep data cleaning and missingness in Chapter 6.

#### Chapter 3 — Vectors, Matrices, and Geometric Thinking

- Use D01–D04, I04–I05, and P18/P27 for dot products, similarity, matrix shape,
  linear functions, and classification geometry.
- Add a plain-language transpose example distinguishing orientation from geometric
  location—the issue already raised by student feedback.
- Write projections and eigenthinking fresh; do not force deep-learning calculus
  into this chapter.

#### Chapter 4 — Probability and Statistical Thinking

- Build the main explanation from P08 and P12, enriched by I06–I09.
- Use P26 as a later application, not as the primary probability introduction.
- Consolidate duplicated estimator sections and add sampling uncertainty.

#### Chapter 5 — Information, Entropy, and Divergence

- Treat P44–P48 as one coherent authored source sequence.
- Present general entropy/divergence first, then IDF as a worked application, then
  LIT as the book's distinctive advanced perspective.
- Keep term-weighting implementation in Chapters 11–12 through cross-references.

#### Chapter 6 — Data Preparation and Feature Engineering

- Use P15 for workflow framing, I03/P33/P34 for text normalization, and P10/P32
  for outliers.
- Write missing data, categorical encoding, scaling, leakage, feature selection,
  dimensionality reduction, and reproducible pipelines as new integrated prose.
- Finish one reusable preprocessing pipeline before drafting model chapters.

### Stage 2 — complete the predictive-model core

#### Chapter 7 — Classification

- Rebuild the linear/nonlinear progression with P16, P27, P29, P08/P26, and
  D02–D04.
- End at perceptron intuition and point forward to Chapter 9A.
- Add a consistent comparison case across kNN, Naive Bayes, linear models, SVM,
  and a shallow network.

#### Chapter 8 — Multiclass and Structured Decisions

- Use D03–D05 for output units, score/probability distinction, softmax, and shape.
- Write one-vs-rest/one-vs-one, tree/rule, multilabel, ordinal, and calibration
  sections from the existing slide map plus new original prose.
- Do not relocate generalization/ensemble material here; cross-reference Ch. 15.

#### Chapter 9 — Numeric Prediction and Regression

- Use D04–D05 and D10 for the housing-price narrative, loss, fitting, validation,
  and debugging; use P32 for residual/outlier interpretation.
- Begin with a framework-light derivation and add uncertainty/diagnostics before
  showing a library implementation.

#### Chapter 9A — Neural Networks and Representation Learning

- Use D02–D05 for layers, activations, loss, forward computation, and backprop
  intuition; D06–D14 for a short architecture survey; D16–D18 for embeddings and
  attention; P29 for a concise authored nonlinear-classification bridge.
- Limit the core chapter to one MLP example and one representation example.
- Move CNN/RNN/GAN details to optional boxes/Practice.
- End with embeddings/attention as the bridge to Chapters 11–12.

**August 17 implementation decision:** CNN now has a dedicated, concise core
chapter plus a matched MLP/concepts/CNN practice sequence. D06–D10 supplied the
authorial flow. This satisfies the planned architecture example without requiring
the eventual representation-learning chapter to repeat convolution mechanics.
RNN/GAN details remain optional, and embeddings/attention should still be placed
where they best support the language and retrieval chapters.

#### Chapter 15 — Generalization, Model Selection, and Fit

- Draft this immediately after the predictive-model chapters even though it
  appears later in the book.
- Use D04–D10 for regularization, dropout, validation, and training diagnostics.
- Combine those explanations with the INFO629 ensemble deck for bias–variance,
  bagging, boosting, and stacking; write CV/tuning/leakage sections anew.

### Stage 3 — complete organization, language, retrieval, graphs, and evaluation

#### Chapter 10 — Clustering and Organization

- Use I15–I16 for a cleaner HAC/k-means/evaluation narrative and P10/P32 for the
  anomaly connection.
- Add DBSCAN/density methods and stability/model-selection guidance from new
  sources; do not duplicate the recovered notebook.

#### Chapter 11 — Text and Human Language

- Use P13/P26 for counts and probabilistic classification, I16–I18 and D11–D18
  for language models, embeddings, sequence context, and attention, and P39 for a
  Practice case.
- Organize the chapter as representations becoming progressively richer: tokens →
  weighted counts → probabilities → embeddings → contextual representations.
- Keep transformer architecture concise and refer back to Chapter 9A.

#### Chapter 12 — Search and Retrieval

- Use I00–I18/P52 for the complete retrieval sequence and P41/I13 for Practice.
- Preserve one mathematical line: inverted index → vector scoring → probabilistic
  ranking/BM25 → feedback → language-model retrieval → semantic/hybrid retrieval.
- Place PageRank's full graph explanation in Chapter 13 and cross-reference it.

#### Chapter 13 — Graphs and Structural Analysis

- Use I10–I12 for web graphs, random walks, and PageRank, matched to the Week 6
  link-analysis deck.
- Add original sections for traversal, broader centrality, communities/roles, link
  prediction, and graph learning.
- Redraw all graph figures and use one small graph consistently.

#### Chapter 14 — Evaluation and Experimentation

- Use P21 as the clean backbone and I14–I15 for class explanation, examples, and
  misconceptions.
- Integrate classification, regression, clustering, and ranking metrics rather
  than treating retrieval evaluation as the whole chapter.
- Add resampling, significance, uncertainty, subgroup/fairness evaluation, and
  reproducible reporting as new material.

### Stage 4 — lifecycle, framing, and optional extension

#### Chapter 16 — Scaling, Deployment, and Responsible Use

- Use P42/P40 for scale and distributed computation, P50/I20/D00 for historical
  perspective, and P37/D18 for modern model limits and implications.
- Write deployment, monitoring/drift, privacy/security, fairness, sustainability,
  and human oversight from current primary sources.
- Keep Spark commands in Practice; keep the theory tool-neutral.

#### Chapter 1 — From Data to Information and Meaning

- Revise last so it accurately previews the final book.
- Draw selectively from D00, I00, I20, P15, P20, and P50.
- Preserve the original data-to-meaning thesis rather than replacing it with a
  history of deep learning.

#### Optional reinforcement-learning extension

- Use P23 as the conceptual backbone and D15 for classroom explanation.
- Choose either the Taxi tutorial or the Tic-tac-toe sequence as the main lab.
- Add a short evaluation, reward-design, exploration, and safety discussion.

## Per-transcript conversion workflow

For each selected transcript:

1. Register source ID, raw filename, duration, course/channel, likely date/week,
   authorship, matching slides/notebooks, and target chapter in the ledger.
2. Segment by substantive topic and discard logistics, unrelated conversation,
   student-identifying content, and repeated lecture recap.
3. Repair automatic-caption errors while preserving timestamp links to the raw
   source. Flag uncertain mathematical terms rather than guessing.
4. Compare the cleaned segment with the matching slides/notebook. Record which
   equations, examples, figures, and code are original, adapted, or externally
   sourced.
5. Produce a short source brief: learning objective, explanatory arc, examples,
   misconceptions, reusable quotations/ideas, and missing evidence.
6. Draft book prose from the source brief—not by lightly editing the transcript.
7. Re-derive equations, recreate examples, redraw figures, and build citations.
8. Add a Practice activity only when it reinforces the chapter objective and does
   not duplicate an existing lab.
9. Review technical correctness, pedagogy, rights/provenance, accessibility, and
   HTML/PDF rendering.

## Immediate decisions before conversion

1. Approve Chapter 9A: **Neural Networks and Representation Learning**.
2. Confirm reinforcement learning as optional for the first edition.
3. Confirm Python-first labs and a compact, separate computing toolkit.
4. Choose the canonical reusable tabular, text/search, and graph datasets.
5. Confirm authorship/permission for co-instructor materials used alongside DSCI471
   transcripts.
6. Approve the authoring sequence above, beginning with Chapters 2–6 and deferring
   the final Chapter 1 revision until the scope is stable.

Once these decisions are approved, the recommended pilot is Chapter 5 rather than
the earlier Chapter 6 proposal. P44–P48 form a cohesive, distinctive, author-owned
sequence that can establish the transcript-cleaning, provenance, mathematical
verification, cross-reference, and theory-to-practice workflow on a chapter that
already has substantial manuscript content. Chapter 6 should follow immediately as
the first major gap-filling chapter.
