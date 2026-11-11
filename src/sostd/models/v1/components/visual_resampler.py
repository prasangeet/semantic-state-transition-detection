
from __future__ import annotations

import torch
import torch.nn as nn


class VisualResampler(nn.Module):
    """Compress visual tokens into a fixed number of learned queries."""

    def __init__(
        self,
        input_dim: int = 256,
        output_dim: int = 256,
        num_queries: int = 8,
        num_heads: int = 4,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if input_dim < 1 or output_dim < 1:
            raise ValueError("Feature dimensions must be positive.")

        if num_queries < 1:
            raise ValueError("num_queries must be at least 1.")

        if num_heads < 1 or output_dim % num_heads != 0:
            raise ValueError(
                "output_dim must be divisible by num_heads."
            )

        if not 0.0 <= dropout < 1.0:
            raise ValueError("dropout must be in [0, 1).")

        self.input_projection = (
            nn.Linear(input_dim, output_dim)
            if input_dim != output_dim
            else nn.Identity()
        )

        self.query_tokens = nn.Parameter(
            torch.randn(1, 1, num_queries, output_dim) * 0.02
        )

        self.cross_attention = nn.MultiheadAttention(
            embed_dim=output_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True,
        )

        self.norm1 = nn.LayerNorm(output_dim)

        self.feed_forward = nn.Sequential(
            nn.Linear(output_dim, output_dim * 4),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(output_dim * 4, output_dim),
            nn.Dropout(dropout),
        )

        self.norm2 = nn.LayerNorm(output_dim)

        self.num_queries = num_queries

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        """
        Args:
            features: (B, T, N, input_dim)

        Returns:
            Resampled features: (B, T, K, output_dim)
        """

        if features.ndim != 4:
            raise ValueError(
                "Expected features with shape (B, T, N, D)."
            )

        if features.shape[-1] != (
            self.input_projection.in_features
            if isinstance(self.input_projection, nn.Linear)
            else self.query_tokens.shape[-1]
        ):
            raise ValueError("Unexpected input feature dimension.")

        batch_size, num_frames, num_tokens, _ = features.shape

        if num_frames < 1:
            raise ValueError("At least one frame is required.")

        if num_tokens < 1:
            raise ValueError("At least one visual token is required.")

        projected = self.input_projection(features)

        projected = projected.reshape(
            batch_size * num_frames,
            num_tokens,
            -1,
        )

        queries = self.query_tokens.expand(
            batch_size,
            num_frames,
            -1,
            -1,
        ).reshape(
            batch_size * num_frames,
            self.num_queries,
            -1,
        )

        attended, _ = self.cross_attention(
            query=queries,
            key=projected,
            value=projected,
            need_weights=False,
        )

        output = self.norm1(queries + attended)
        output = self.norm2(output + self.feed_forward(output))

        return output.reshape(
            batch_size,
            num_frames,
            self.num_queries,
            -1,
        )
