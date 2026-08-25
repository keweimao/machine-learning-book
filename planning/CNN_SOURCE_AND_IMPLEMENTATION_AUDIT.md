# CNN source and implementation audit

Completed August 17 and updated August 25, 2026. This audit records how the CNN
theory chapter and practice sequence were reconstructed from the author's DSCI 471 teaching archive.
It is an editorial provenance record, not a claim that archived teaching files
can be republished verbatim.

## Implemented book structure

- `chapters/09a-convolutional-neural-networks.qmd` is a new core chapter placed
  after regression and before clustering.
- `practice/09a-convolutional-neural-networks.qmd` is one continuous practicum:
  MLP baseline, visible CNN mechanics, matched CNN comparison, and learned
  activation analysis for handwritten 1s and 7s.
- `practice/notebooks/cnn-mnist-practicum.ipynb` is an executed convenience copy
  for students; the QMD remains canonical.
- `scripts/generate_cnn_practicum_assets.py` reproduces the published models,
  metrics, and original figures in `assets/figures/chapter09a/practicum/`.

## Author lecture sequence

The Spring 2026 DSCI 471 recordings provide the main pedagogical narrative.

| Transcript | Contribution retained in the new writing |
|---|---|
| D04–D05 | MLP/MNIST baseline, loss, validation, and training workflow |
| D06 | Transition from flattening $28\times28$ images to preserving spatial neighborhoods; CNN motivation |
| D07 | Grid data, grayscale/RGB channels, tensors, delayed flattening, convolutional feature extraction |
| D08 | Kernel-as-lens intuition, convolution/pooling sequence, and hierarchy from short strokes to larger patterns |
| D09 | Crucial distinction among channels, filters, and layers; one filter produces one output channel |
| D10 | Input/output channel continuation and dimensional reasoning |

The new chapter keeps this conceptual flow but removes lecture repetition,
corrects transcript recognition errors (for example, MNIST and 784), and supplies
verified equations and compact examples.

## Slides and handouts reviewed

The following source presentations were rendered and visually inspected:

- `DSCI471/Week3/DSCI471-Week3.pptx`
- `DSCI471/Week4/DSCI471-CNN.pptx`
- `DSCI471/Week5/DSCI471-CNN.pptx`
- `DSCI471/Week5/DSCI471-CNN-Part2.pptx`

The following student-facing PDFs were rendered page by page and inspected:

- `notebooks/DSCI471/Week3_Notebook/lab_mnist_mlp.pdf`
- `notebooks/DSCI471/Week4_Notebook/lab_cnn_concepts.pdf`
- `notebooks/DSCI471/Week4_Notebook/lab_mnist_cnn.pdf`

The PDFs confirm the intended Jason sequence: MLP baseline, conceptual CNN work,
then CNN on the same MNIST task. `Week5_Notebook/CNN_Visualized.ipynb` supplied
the final return to learned kernels and the explicit 1-versus-7 comparison.

## Editorial and rights decisions

- `Week4/d2l_chapter7/lecture_w4_cnn.md` is detailed but closely follows *Dive
  into Deep Learning*. It was used as a topic checklist, not converted into book
  prose. The new chapter cites the D2L book and uses newly written explanations,
  equations, examples, and an original architecture diagram.
- D2L logos, screenshots, Waldo images, publisher figures, and copied architecture
  illustrations were not imported.
- Files under directories labeled `Milad` or otherwise associated with a
  co-instructor were not copied. They were treated only as discovery pointers.
  Publication use would require authorship confirmation and permission.
- Student submissions and solution-only homework files were excluded.
- The parameter comparison was redesigned. The source MLP and CNN examples had
  materially different capacities; the published pair uses 109,386 and 105,866
  parameters, respectively, so the comparison better isolates architecture.
- The text distinguishes strict convolution from the cross-correlation operation
  implemented by common deep-learning layers.
- Claims that pooling creates full invariance were softened to the defensible
  statement that it can reduce sensitivity to small positional changes.

## Source hashes for the canonical lab seeds

| Source | SHA-256 |
|---|---|
| `Week3_Notebook/lab_mnist_mlp.ipynb` | `a6a77f8157c47b8efe51cded6d48b9bfc14f97f39b707dee0bcbb4ec66c23544` |
| `Week4_Notebook/lab_cnn_concepts.ipynb` | `44ad44dbdc721b638cc3760d84558c93422f3b97c73db82e250548ba3618d009` |
| `Week4_Notebook/lab_mnist_cnn.ipynb` | `e0406b8b1c1e359ed8907f39766c20087750a16663c77523220cf27fd99249de` |
| `Week5_Notebook/CNN_Visualized.ipynb` | `3bb1c45b22aae677a1c477ef27a7a94f93720a4b4052f88b4c9b9dda602da1e0` |
| `Week4/d2l_chapter7/lecture_w4_cnn.md` | `e973a3b94543dd14332522e5924170953395b845c588df1e92e05125c90a6ca8` |

## Executed reference experiment

The August 25 full-data run used one seeded 54,000/6,000/10,000 split, Adam,
batch size 128, and early stopping on validation loss. The 109,386-parameter MLP
reached 97.56% test accuracy (244 errors); the 105,866-parameter CNN reached
98.75% (125 errors). Both training curves and selected feature maps are retained
as original book assets. These values are representative results, not guarantees.

## Remaining editorial work

1. Ask Jason and the second student to annotate points of confusion, especially
   channel/filter/layer distinctions and output-shape calculations.
2. Decide after student feedback whether residual networks, data augmentation,
   and transfer learning deserve one optional advanced lab or only cross-references.
3. Revisit chapter length after the broader neural/representation chapter plan is
   finalized; avoid duplicating the existing Chapter 7 backpropagation derivation.
