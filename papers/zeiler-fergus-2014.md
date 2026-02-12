# Visualizing and Understanding Convolutional Networks (Zeiler & Fergus -- 2014)

**Reference:** https://arxiv.org/abs/1311.2901

## Summary

This paper introduces a visualisation technique based on deconvolutional networks (DeconvNets) to understand what intermediate layers in a CNN have learned. By projecting feature activations back to the input pixel space, the authors show that early layers learn low-level features (edges, textures) while deeper layers capture high-level semantic patterns (object parts, full objects). They use these visualisations to diagnose architectural choices in AlexNet and propose modifications that improve performance on ImageNet.

## Key Contributions

- Introduces **DeconvNet-based visualisation**: reverse-maps activations at any layer back to input space using transposed convolutions, unpooling (via switch variables), and rectification.
- Shows empirically that CNN features form a **hierarchy**: layer 1-2 learn edges and textures, layer 3 learns patterns, layers 4-5 learn object parts and full objects.
- Demonstrates that visualisation can guide **architecture design** — they identified problems in AlexNet's first-layer filters (too large, aliased) and fixed them.
- Provides **occlusion sensitivity analysis**: systematically occluding parts of the input reveals which regions the network relies on for its prediction.
- Shows that features learned on ImageNet **transfer** well to other datasets (Caltech-101, Caltech-256).

## Limitations

- DeconvNet visualisation is an approximation — it does not compute true gradients with respect to the input (unlike later gradient-based saliency methods).
- Analysis is limited to classification CNNs on ImageNet; unclear how findings generalise to other tasks or architectures.
- Predates modern interpretability methods (Grad-CAM, integrated gradients, attention visualisation).

## Connection to Notebooks

- **Notebook 03** builds the kind of CNN architecture the paper analyses — two convolutional layers with ReLU and pooling, followed by a classifier.
- The paper's core insight (hierarchical feature learning) explains *why* the CNN in notebook 03 outperforms the MLP: convolutions capture spatial patterns that a flat model cannot.
- Directly motivates a future saliency/interpretability notebook.
