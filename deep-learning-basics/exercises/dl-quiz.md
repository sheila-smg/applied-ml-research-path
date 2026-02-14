# Deep Learning Basics -- Self-Assessment

Short-answer questions covering the material from notebooks 01-03. Try to answer from memory before checking the notebooks.

---

### Linear Models & Neurons (Notebook 01)

**1.** Write out the forward pass of a single neuron with `d` input features. What are its learnable parameters?

**2.** What happens if you stack two linear layers (no activation) into a network? Does the model become more expressive? Why or why not?

**3.** Write the gradient of MSE loss with respect to the weight vector `W` for a linear model `y = XW + b`.

**4.** In notebook 01, gradient descent and the closed-form solution produce nearly identical weights. Under what conditions would you prefer one method over the other?

---

### Non-Linearity & MLPs (Notebook 02)

**5.** Why can't a linear model learn a circular decision boundary? What is the fundamental limitation?

**6.** What does ReLU do, and what is its derivative? Why is the derivative being zero for negative inputs not a fatal problem in practice?

**7.** In the MLP from notebook 02, the architecture is `2 -> 8 -> 1`. Write out the shapes of all weight matrices and bias vectors.

**8.** During backpropagation through a ReLU layer, what happens to the gradient for units where the pre-activation was negative?

**9.** The MLP achieves MSE ~0.001 while the linear model plateaus at ~0.25. What single architectural change explains the difference?

---

### CIFAR-10 Case Study (Notebook 03)

**10.** The MLP flattens a 32x32x3 image into a vector. How many input features does this produce? Why is this problematic for image data?

**11.** What two properties of convolutional layers give CNNs an advantage over MLPs on image data?

**12.** In notebook 03, both models show signs of overfitting after 5 epochs. What evidence in the training curves indicates overfitting? Name two techniques that could reduce it.

**13.** Why does `optimizer.zero_grad()` need to be called before each training step? What would happen if you skipped it?

**14.** What is the purpose of `model.eval()` and `torch.no_grad()` during evaluation? Are they doing the same thing?

---

### Connecting the Papers

**15.** The LeCun et al. (2015) paper describes deep learning as "representation learning". How does this concept show up concretely in the CNN from notebook 03?
