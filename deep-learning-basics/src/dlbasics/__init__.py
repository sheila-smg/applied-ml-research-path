"""
Shared utilities for the deep learning basics notebooks.
"""

import random
import numpy as np
import matplotlib.pyplot as plt


def set_seed(seed: int = 42):
    """Set random seeds for Python, NumPy, and PyTorch for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass


def plot_history(history: dict, title_prefix: str = ""):
    """Plot training/validation loss and accuracy curves from a history dict."""
    epochs = list(range(1, len(history["train_loss"]) + 1))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.plot(epochs, history["train_loss"], label="train")
    ax1.plot(epochs, history["val_loss"], label="val")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Loss")
    ax1.set_title(f"{title_prefix} loss".strip())
    ax1.set_xticks(epochs)
    ax1.legend()

    ax2.plot(epochs, history["train_acc"], label="train")
    ax2.plot(epochs, history["val_acc"], label="val")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Accuracy")
    ax2.set_title(f"{title_prefix} accuracy".strip())
    ax2.set_xticks(epochs)
    ax2.legend()

    plt.tight_layout()
    plt.show()
