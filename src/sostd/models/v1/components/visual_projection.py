
from __future__ import annotations

import torch
import torch.nn as nn


class VisualProjection(nn.Module):
    """Project visual features into the language model embedding space."""

    def __init__(
        self,
        input_dim: int = 256,
        output_dim: int = 512,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if input_dim < 1 or output_dim < 1:
            raise ValueError("Feature dimensions must be positive.")

        if not 0.0 <= dropout < 1.0:
            raise ValueError("dropout must be in [0, 1).")

        self.input_dim = input_dim
        self.output_dim = output_dim

        self.norm = nn.LayerNorm(input_dim)
        self.projection = nn.Linear(input_dim, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        """
        Args:
            features: (B, T, K, input_dim)

        Returns:
            Projected features: (B, T, K, output_dim)
        """

        if features.ndim != 4:
            raise ValueError(
                "Expected features with shape (B, T, K, D)."
            )

        if features.shape[-1] != self.input_dim:
            raise ValueError(
                f"Expected input dimension {self.input_dim}, "
                f"got {features.shape[-1]}."
            )

        if features.shape[1] < 1:
            raise ValueError("At least one frame is required.")

        if features.shape[2] < 1:
            raise ValueError("At least one visual token is required.")

        features = self.norm(features)
        features = self.projection(features)
        return self.dropout(features)
