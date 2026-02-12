# Applied ML Research Path

Hands-on deep learning implementations built from first principles, progressing from a single neuron to convolutional networks on real data. Each notebook is self-contained and focuses on building intuition through code rather than using high-level abstractions.

## What's Inside

### Notebooks

| # | Notebook | What it covers |
|---|----------|----------------|
| 01 | [Linear Model & Neuron](week01-deep-learning-basics/notebooks/01_linear_model_and_neuron.ipynb) | A single neuron as linear regression. Closed-form vs gradient descent. Why stacking linear layers adds no expressiveness. |
| 02 | [Nonlinearity & MLP](week01-deep-learning-basics/notebooks/02_nonlinearity_mlp_training_intuition.ipynb) | Why ReLU matters. Manual backpropagation through a 2-layer MLP. Solving a non-linearly separable problem. |
| 03 | [CIFAR-10 Case Study](week01-deep-learning-basics/notebooks/03_case_study.ipynb) | End-to-end PyTorch pipeline. MLP baseline vs CNN on image classification. Training loops, evaluation, and comparison. |

### Paper Notes

Summaries and key takeaways from foundational papers. See [papers/paper-list.md](papers/paper-list.md) for the full list.

- [Deep Learning (LeCun, Bengio, Hinton 2015)](papers/lecun-bengio-hinton-2015.md)
- [Visualizing CNNs (Zeiler & Fergus 2014)](papers/zeiler-fergus-2014.md)
- [ResNets (He et al. 2016)](papers/resnet-2016.md)

### Other Resources

- [Self-assessment quiz](week01-deep-learning-basics/exercises/dl-quiz.md) — 15 questions to test understanding of the notebooks
- [Key concepts](notes/concepts.md) — definitions and intuitions for core deep learning terms

## Repository Structure

```
week01-deep-learning-basics/
    notebooks/        # Jupyter notebooks — core implementations
    src/              # Reusable Python modules
    exercises/        # Self-assessment questions
papers/               # Paper summaries with key contributions and limitations
notes/                # Conceptual definitions and term glossary
```

## Setup

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Datasets (e.g. CIFAR-10) are downloaded automatically by the notebooks via `torchvision.datasets`.

## Key Results

- **Notebook 01**: Gradient descent recovers true weights, matching the closed-form solution.
- **Notebook 02**: MLP with ReLU achieves loss ~0.001 on circular boundary vs ~0.248 for a linear model.
- **Notebook 03**: CNN reaches 70% validation accuracy on CIFAR-10 vs 49% for an MLP baseline (5 epochs each).
