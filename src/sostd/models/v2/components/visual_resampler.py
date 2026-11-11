
from __future__ import annotations

import torch
import torch.nn as nn


class VisualResampler(nn.Module):
    """
    Compress spatial visual tokens using learned query tokens.

    Each frame is independently resampled.

    Input:
        (B, T, N, input_dim)

    Output:
        (B, T, num_queries, output_dim)
    """

    def __init__(
        self,
        input_dim: int = 512,
        output_dim: int = 512,
        num_queries: int = 16,
        num_heads: int = 8,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if input_dim < 1 or output_dim < 1:
            raise ValueError("Feature dimensions must be positive.")

        if num_queries < 1:
            raise ValueError("num_queries must be positive.")

        if num_heads < 1 or output_dim % num_heads != 0:
            raise ValueError(
                "output_dim must be divisible by num_heads."
            )

        if not 0.0 <= dropout < 1.0:
            raise ValueError("dropout must be in [0, 1).")

        self.input_dim = input_dim
        self.output_dim = output_dim
        self.num_queries = num_queries

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

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        """
        Resample visual tokens independently for each frame.

        Args:
            features: (B, T, N, input_dim)

        Returns:
            Resampled features: (B, T, K, output_dim)
        """

        if features.ndim != 4:
            raise ValueError(
                "Expected features with shape (B, T, N, D)."
            )

        if not features.is_floating_point():
            raise TypeError("Features must be floating-point tensors.")

        batch_size, num_frames, num_tokens, feature_dim = features.shape

        if batch_size < 1:
            raise ValueError("Batch size must be positive.")

        if num_frames < 1:
            raise ValueError("At least one frame is required.")

        if num_tokens < 1:
            raise ValueError("At least one visual token is required.")

        if feature_dim != self.input_dim:
            raise ValueError(
                f"Expected input dimension {self.input_dim}, "
                f"got {feature_dim}."
            )

        # Project visual features into the resampler dimension.
        projected = self.input_projection(features)

        projected = projected.reshape(
            batch_size * num_frames,
            num_tokens,
            self.output_dim,
        )

        # Expand learned queries independently for each frame.
        queries = self.query_tokens.expand(
            batch_size,
            num_frames,
            -1,
            -1,
        ).reshape(
            batch_size * num_frames,
            self.num_queries,
            self.output_dim,
        )

        # Cross-attention: learned queries retrieve relevant visual tokens.
        attended, _ = self.cross_attention(
            query=queries,
            key=projected,
            value=projected,
            need_weights=False,
        )

        output = self.norm1(queries + attended)

        # Position-wise feed-forward refinement.
        output = self.norm2(
            output + self.feed_forward(output)
        )

        return output.reshape(
            batch_size,
            num_frames,
            self.num_queries,
            self.output_dim,
        )
