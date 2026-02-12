# Deep Residual Learning for Image Recognition (He et al. -- 2016)

**Reference:** https://arxiv.org/abs/1512.03385

## Summary

This paper addresses the **degradation problem**: as networks get deeper, training accuracy saturates and then degrades — not from overfitting, but from optimisation difficulty. The authors propose residual learning, where each block learns a residual function `F(x) = H(x) - x` rather than the full mapping `H(x)`. The output becomes `y = F(x) + x` (a skip connection). This reformulation makes it easier for the optimiser to learn identity mappings when needed, enabling training of networks with 100+ layers. ResNets won the 2015 ImageNet competition with 152 layers and 3.57% top-5 error.

## Key Contributions

- Identifies the **degradation problem**: deeper plain networks perform worse than shallower ones, even on training data, due to optimisation difficulty.
- Introduces **residual blocks** with skip (shortcut) connections: `y = F(x) + x`. The network only needs to learn the residual `F(x)`.
- Demonstrates that skip connections ease gradient flow during backpropagation, mitigating **vanishing gradients** in very deep networks.
- Achieves state-of-the-art results on ImageNet (2015) with 152 layers — far deeper than any prior architecture.
- Shows that the residual framework generalises to other tasks: object detection (COCO) and localisation.

## Limitations

- The paper focuses on image classification; the architectural insights apply broadly, but the specific designs are vision-oriented.
- Does not fully explain *why* residual learning works from a theoretical perspective (later work connects it to ensemble behaviour and loss landscape smoothing).
- Batch normalisation is used throughout but its interaction with residual connections is not deeply analysed.

## Connection to Notebooks

- **Notebook 01** covers the vanishing gradient problem conceptually — ResNets are the architectural solution to this problem at scale.
- **Notebook 02** shows that non-linearity enables expressiveness; ResNets show that with skip connections, you can stack many more non-linear layers without losing trainability.
- **Notebook 03** uses a 2-layer CNN; ResNets demonstrate what happens when you scale to 100+ layers with the right architectural choices.
