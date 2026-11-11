
from __future__ import annotations

import torch
import torch.nn as nn


class LossFactory:
    """Factory for supported PyTorch loss functions."""

    @staticmethod
    def create(
        name: str = "cross_entropy",
        **kwargs,
    ) -> nn.Module:
        losses = {
            "cross_entropy": nn.CrossEntropyLoss,
            "bce": nn.BCEWithLogitsLoss,
            "mse": nn.MSELoss,
            "l1": nn.L1Loss,
            "smooth_l1": nn.SmoothL1Loss,
        }

        if name not in losses:
            raise ValueError(
                f"Unsupported loss: {name}. "
                f"Available: {list(losses.keys())}"
            )

        return losses[name](**kwargs)


def compute_class_weights(
    labels: torch.Tensor,
    num_classes: int,
    ignore_index: int = -100,
) -> torch.Tensor:
    """
    Calculate normalized inverse-frequency class weights.

    Args:
        labels:
            Integer class labels. Ignored labels are excluded.
        num_classes:
            Total number of classes.
        ignore_index:
            Label value to exclude from class counts.

    Returns:
        Float tensor of shape (num_classes,).
        Classes absent from the supplied labels receive weight 0.
    """
    if not isinstance(labels, torch.Tensor):
        raise TypeError("labels must be a torch.Tensor.")

    if labels.numel() == 0:
        raise ValueError("labels cannot be empty.")

    if num_classes < 1:
        raise ValueError("num_classes must be positive.")

    if labels.is_floating_point() or labels.is_complex():
        raise TypeError("labels must contain integer class indices.")

    labels = labels.long().reshape(-1)

    valid_labels = labels[labels != ignore_index]

    if valid_labels.numel() == 0:
        raise ValueError(
            "No valid labels available to compute class weights."
        )

    if torch.any(valid_labels < 0) or torch.any(
        valid_labels >= num_classes
    ):
        raise ValueError(
            "Labels must be in the range "
            f"[0, {num_classes - 1}], excluding ignore_index."
        )

    counts = torch.bincount(
        valid_labels,
        minlength=num_classes,
    ).to(dtype=torch.float32)

    weights = torch.zeros_like(counts)

    present_classes = counts > 0
    weights[present_classes] = 1.0 / counts[present_classes]

    # Normalize over classes that occur in the supplied labels.
    weights[present_classes] /= weights[present_classes].mean()

    return weights
