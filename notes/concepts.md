# Key Concepts -- Deep Learning Fundamentals

Definitions and intuitions for terms used across the Week 01 notebooks and papers.

---

### Forward Pass
The computation that maps input `X` to output `y_hat` through the network's layers. For a single neuron: `z = Xw + b`. For an MLP: apply linear transformations interleaved with activations.

### Loss Function
A scalar that measures how far the model's predictions are from the targets. MSE for regression (`mean((y - y_hat)^2)`), cross-entropy for classification. Training minimises this value.

### Gradient Descent
Iterative optimisation: compute the gradient of the loss with respect to each parameter, then update parameters in the opposite direction of the gradient. `W = W - lr * dL/dW`.

### Learning Rate
Controls the step size of each gradient descent update. Too large: training diverges. Too small: training is slow. Typical starting values: 1e-3 for Adam, 1e-2 to 1e-1 for SGD.

### Backpropagation
Efficient algorithm for computing gradients in a computational graph by applying the chain rule layer by layer, from output to input. Requires storing intermediate activations (forward pass) to compute gradients (backward pass).

### Activation Function
A non-linear function applied after a linear transformation. Without it, any stack of linear layers collapses to a single linear mapping. Common choices: ReLU, sigmoid, tanh.

### ReLU (Rectified Linear Unit)
`ReLU(z) = max(0, z)`. Derivative is 1 for `z > 0`, 0 for `z < 0`. Simple, computationally cheap, and avoids the vanishing gradient problem for positive inputs. Most commonly used activation in modern networks.

### Vanishing Gradients
When gradients shrink exponentially as they propagate through many layers during backpropagation. Makes early layers learn very slowly. Caused by activations with small derivatives (sigmoid, tanh). Mitigated by ReLU, residual connections, and careful initialisation.

### Inductive Bias
Assumptions built into a model's architecture that constrain the space of solutions. An MLP has no spatial bias — it treats all input dimensions equally. A CNN has a strong spatial bias: local connectivity and weight sharing assume that nearby pixels are more related than distant ones.

### Convolutional Layer
Applies a small learnable filter (kernel) across spatial positions of the input. Two key properties: **local connectivity** (each output depends on a small input patch) and **weight sharing** (the same filter is applied everywhere). This dramatically reduces parameters compared to a fully connected layer.

### Pooling
Reduces spatial dimensions by summarising local patches (e.g. max-pooling takes the maximum value in each patch). Provides translation invariance and reduces computation in deeper layers.

### Overfitting
When a model fits the training data well but generalises poorly to unseen data. Symptoms: training loss decreases while validation loss increases. Common mitigations: dropout, data augmentation, early stopping, weight decay.

### Residual Connection (Skip Connection)
A shortcut that adds the input of a block to its output: `y = F(x) + x`. Allows gradients to flow directly through the skip path, enabling training of very deep networks (100+ layers). Introduced by He et al. (2016) in ResNets.

### Representation Learning
The idea that a model should learn its own feature representations from data rather than relying on hand-engineered features. Each layer in a deep network transforms the input into a progressively more abstract representation. Central thesis of LeCun, Bengio & Hinton (2015).
