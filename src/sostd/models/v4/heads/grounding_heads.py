
from __future__ import annotations

import torch
import torch.nn as nn


class GroundingHead(nn.Module):
    """
    Clip-level classification head operating on temporal features.

    Input:
        (B, Q, D)

    Output:
        (B, num_classes)

    Temporal queries are mean-pooled before classification.
    """

    def __init__(
        self,
        input_dim: int = 1024,
        num_classes: int = 1,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if input_dim < 2:
            raise ValueError(
                "input_dim must be at least 2."
            )

        if num_classes < 1:
            raise ValueError(
                "num_classes must be positive."
            )

        if not 0.0 <= dropout < 1.0:
            raise ValueError(
                "dropout must be in [0, 1)."
            )

        self.input_dim = input_dim
        self.num_classes = num_classes

        hidden_dim = input_dim // 2

        self.norm = nn.LayerNorm(input_dim)

        self.classifier = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, num_classes),
        )

    def forward(
        self,
        features: torch.Tensor,
    ) -> torch.Tensor:
        """
        Args:
            features:
                Temporal features of shape (B, Q, D).

        Returns:
            Classification logits of shape (B, num_classes).
        """

        if not isinstance(features, torch.Tensor):
            raise TypeError(
                "features must be a torch.Tensor."
            )

        if features.ndim != 3:
            raise ValueError(
                "Expected features with shape (B, Q, D)."
            )

        if not features.is_floating_point():
            raise TypeError(
                "features must be floating-point."
            )

        batch_size, num_queries, feature_dim = features.shape

        if batch_size < 1 or num_queries < 1:
            raise ValueError(
                "Batch size and query count must be positive."
            )

        if feature_dim != self.input_dim:
            raise ValueError(
                f"Expected feature dimension {self.input_dim}, "
                f"received {feature_dim}."
            )

        # Aggregate information across learned temporal queries.
        pooled = features.mean(dim=1)

        # Keep the input compatible with the head's parameters.
        pooled = pooled.to(dtype=self.norm.weight.dtype)

        pooled = self.norm(pooled)

        return self.classifier(pooled)


class ObjectHead(GroundingHead):
    """Predict one object category for each video clip."""

    pass


class ActionHead(GroundingHead):
    """Optional action classifier retained for API compatibility."""

    pass
