# Deep Learning (LeCun, Bengio, Hinton -- 2015)

**Reference:** https://www.nature.com/articles/nature14539

## Summary

A landmark review paper that surveys the core ideas behind deep learning: representation learning through multiple levels of abstraction. The authors trace the evolution from shallow models to deep architectures, covering backpropagation, convolutional networks, recurrent networks, and distributed representations. They argue that deep learning's key advantage is its ability to automatically discover the representations needed for detection or classification, rather than relying on hand-engineered features.

## Key Contributions

- Frames deep learning as **representation learning** — each layer transforms the previous representation into a slightly more abstract one.
- Provides a clear explanation of **backpropagation** and why it enables efficient gradient computation in deep networks.
- Describes how **convolutional networks** exploit spatial structure through local receptive fields, shared weights, and pooling.
- Surveys **recurrent networks** and LSTMs for sequence modelling.
- Argues that **unsupervised learning** (e.g. autoencoders, GANs) will become increasingly important for learning from unlabelled data.

## Limitations

- Written in 2015 — predates transformers, modern self-supervised learning, and large-scale pretraining.
- Limited discussion of optimisation challenges (batch normalisation, learning rate schedules, architecture search).
- Overly optimistic about unsupervised pretraining, which was largely overtaken by supervised and self-supervised methods.

## Connection to Notebooks

- **Notebook 01** implements the core computation described in the paper: a neuron as `z = Xw + b`, trained via gradient descent.
- **Notebook 02** demonstrates the paper's central argument: non-linear activations are what make deep networks more expressive than shallow ones.
- **Notebook 03** builds a CNN following the convolutional architecture principles the paper describes (local connectivity, weight sharing, pooling).
