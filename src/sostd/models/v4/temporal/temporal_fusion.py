from __future__ import annotations

import torch
import torch.nn as nn


class SpatioTemporalBlock(nn.Module):
    """
    Factorized spatial/temporal self-attention over DINOv2 tokens.

    Spatial attention mixes patch/register tokens within each frame.
    Temporal attention mixes the same token slot across frames.
    The full N-token representation is preserved.

    Input/output: (B, T, N, D)
    """

    def __init__(
        self,
        hidden_dim: int = 1024,
        num_heads: int = 16,
        dropout: float = 0.1,
        mlp_ratio: int = 4,
    ) -> None:
        super().__init__()
        if hidden_dim < 1 or num_heads < 1:
            raise ValueError("hidden_dim and num_heads must be positive.")
        if hidden_dim % num_heads:
            raise ValueError("hidden_dim must be divisible by num_heads.")
        if mlp_ratio < 1:
            raise ValueError("mlp_ratio must be positive.")
        if not 0.0 <= dropout < 1.0:
            raise ValueError("dropout must be in [0, 1).")

        self.hidden_dim = hidden_dim

        self.spatial_norm = nn.LayerNorm(hidden_dim)
        self.spatial_attention = nn.MultiheadAttention(
            hidden_dim, num_heads, dropout=dropout, batch_first=True
        )
        self.spatial_dropout = nn.Dropout(dropout)
        self.spatial_ffn_norm = nn.LayerNorm(hidden_dim)
        self.spatial_ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * mlp_ratio),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * mlp_ratio, hidden_dim),
            nn.Dropout(dropout),
        )

        self.temporal_norm = nn.LayerNorm(hidden_dim)
        self.temporal_attention = nn.MultiheadAttention(
            hidden_dim, num_heads, dropout=dropout, batch_first=True
        )
        self.temporal_dropout = nn.Dropout(dropout)
        self.temporal_ffn_norm = nn.LayerNorm(hidden_dim)
        self.temporal_ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * mlp_ratio),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * mlp_ratio, hidden_dim),
            nn.Dropout(dropout),
        )

    def forward(
        self,
        x: torch.Tensor,
        frame_mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        if x.ndim != 4:
            raise ValueError("x must have shape (B, T, N, D).")
        batch, frames, tokens, dim = x.shape
        if dim != self.hidden_dim:
            raise ValueError(f"Expected D={self.hidden_dim}, got {dim}.")

        # Spatial self-attention, independently for each frame.
        spatial = x.reshape(batch * frames, tokens, dim)
        normalized = self.spatial_norm(spatial)
        attended, _ = self.spatial_attention(
            normalized, normalized, normalized, need_weights=False
        )
        spatial = spatial + self.spatial_dropout(attended)
        spatial = spatial + self.spatial_ffn(self.spatial_ffn_norm(spatial))
        x = spatial.reshape(batch, frames, tokens, dim)

        # Temporal self-attention at each token slot.
        temporal = x.permute(0, 2, 1, 3).reshape(
            batch * tokens, frames, dim
        )
        temporal_padding_mask = None
        if frame_mask is not None:
            temporal_padding_mask = (
                frame_mask[:, None, :]
                .expand(batch, tokens, frames)
                .reshape(batch * tokens, frames)
            )

        normalized = self.temporal_norm(temporal)
        attended, _ = self.temporal_attention(
            normalized,
            normalized,
            normalized,
            key_padding_mask=temporal_padding_mask,
            need_weights=False,
        )
        temporal = temporal + self.temporal_dropout(attended)
        temporal = temporal + self.temporal_ffn(
            self.temporal_ffn_norm(temporal)
        )

        return temporal.reshape(batch, tokens, frames, dim).permute(
            0, 2, 1, 3
        )


class QueryCrossAttentionBlock(nn.Module):
    """Refine learned queries and let them retrieve from visual memory."""

    def __init__(
        self,
        hidden_dim: int,
        num_heads: int,
        dropout: float = 0.1,
        mlp_ratio: int = 4,
    ) -> None:
        super().__init__()
        self.query_self_norm = nn.LayerNorm(hidden_dim)
        self.query_self_attention = nn.MultiheadAttention(
            hidden_dim, num_heads, dropout=dropout, batch_first=True
        )
        self.query_self_dropout = nn.Dropout(dropout)

        self.query_norm = nn.LayerNorm(hidden_dim)
        self.memory_norm = nn.LayerNorm(hidden_dim)
        self.cross_attention = nn.MultiheadAttention(
            hidden_dim, num_heads, dropout=dropout, batch_first=True
        )
        self.cross_dropout = nn.Dropout(dropout)

        self.ffn_norm = nn.LayerNorm(hidden_dim)
        self.ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * mlp_ratio),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * mlp_ratio, hidden_dim),
            nn.Dropout(dropout),
        )

    def forward(
        self,
        queries: torch.Tensor,
        memory: torch.Tensor,
        memory_mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        q = self.query_self_norm(queries)
        attended, _ = self.query_self_attention(
            q, q, q, need_weights=False
        )
        queries = queries + self.query_self_dropout(attended)

        q = self.query_norm(queries)
        m = self.memory_norm(memory)
        attended, _ = self.cross_attention(
            q, m, m, key_padding_mask=memory_mask, need_weights=False
        )
        queries = queries + self.cross_dropout(attended)
        return queries + self.ffn(self.ffn_norm(queries))


class TemporalFusion(nn.Module):
    """
    Hierarchical visual fusion for OSCaR-Lite V4.

    Returns:
        frame_features:      (B, T, N, D)
        state_features:      (B, T, K_state, D)
        transition_features: (B, Q_transition, D)

    True in frame_mask means that a frame is padding.
    """

    def __init__(
        self,
        input_dim: int = 1024,
        hidden_dim: int = 1024,
        num_heads: int = 16,
        num_layers: int = 4,
        num_queries: int = 64,
        max_frames: int = 3,
        dropout: float = 0.1,
        mlp_ratio: int = 4,
        state_queries: int = 16,
        query_layers: int = 2,
    ) -> None:
        super().__init__()
        if input_dim < 1 or hidden_dim < 1:
            raise ValueError("input_dim and hidden_dim must be positive.")
        if num_heads < 1 or hidden_dim % num_heads:
            raise ValueError("hidden_dim must be divisible by num_heads.")
        if num_layers < 1 or query_layers < 1:
            raise ValueError("num_layers and query_layers must be positive.")
        if num_queries < 1 or state_queries < 1 or max_frames < 1:
            raise ValueError("Query counts and max_frames must be positive.")
        if not 0.0 <= dropout < 1.0:
            raise ValueError("dropout must be in [0, 1).")

        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.num_queries = num_queries
        self.state_queries_count = state_queries
        self.transition_queries_count = num_queries
        self.max_frames = max_frames

        self.input_projection = (
            nn.Identity()
            if input_dim == hidden_dim
            else nn.Linear(input_dim, hidden_dim)
        )
        self.frame_embeddings = nn.Parameter(
            torch.randn(1, max_frames, 1, hidden_dim) * 0.02
        )

        self.encoder_blocks = nn.ModuleList([
            SpatioTemporalBlock(hidden_dim, num_heads, dropout, mlp_ratio)
            for _ in range(num_layers)
        ])
        self.frame_output_norm = nn.LayerNorm(hidden_dim)

        self.state_queries = nn.Parameter(
            torch.randn(1, state_queries, hidden_dim) * 0.02
        )
        self.state_blocks = nn.ModuleList([
            QueryCrossAttentionBlock(
                hidden_dim, num_heads, dropout, mlp_ratio
            )
            for _ in range(query_layers)
        ])
        self.state_output_norm = nn.LayerNorm(hidden_dim)

        self.transition_queries = nn.Parameter(
            torch.randn(1, num_queries, hidden_dim) * 0.02
        )
        self.transition_blocks = nn.ModuleList([
            QueryCrossAttentionBlock(
                hidden_dim, num_heads, dropout, mlp_ratio
            )
            for _ in range(query_layers)
        ])
        self.transition_output_norm = nn.LayerNorm(hidden_dim)

    def forward(
        self,
        features: torch.Tensor,
        frame_mask: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        if not isinstance(features, torch.Tensor) or features.ndim != 4:
            raise ValueError("features must have shape (B, T, N, D).")
        if not features.is_floating_point():
            raise TypeError("features must be floating-point.")

        batch, frames, tokens, dim = features.shape
        if batch < 1 or frames < 1 or tokens < 1:
            raise ValueError("Batch, frame, and token dimensions must be positive.")
        if frames > self.max_frames:
            raise ValueError(f"Received {frames} frames; max is {self.max_frames}.")
        if dim != self.input_dim:
            raise ValueError(f"Expected input dimension {self.input_dim}, got {dim}.")

        if frame_mask is not None:
            if frame_mask.shape != (batch, frames):
                raise ValueError("frame_mask must have shape (B, T).")
            frame_mask = frame_mask.to(device=features.device, dtype=torch.bool)
            if frame_mask.all(dim=1).any():
                raise ValueError("Every sample must contain at least one valid frame.")

        parameter = next(self.parameters())
        x = features.to(device=parameter.device, dtype=parameter.dtype)
        x = self.input_projection(x)
        x = x + self.frame_embeddings[:, :frames].to(dtype=x.dtype)

        for block in self.encoder_blocks:
            x = block(x, frame_mask=frame_mask)
        frame_features = self.frame_output_norm(x)

        # Each frame gets its own K learned queries. The memory is frame-local,
        # but already contains temporal context from the factorized encoder.
        state_memory = frame_features.reshape(
            batch * frames, tokens, self.hidden_dim
        )
        state_queries = self.state_queries.expand(batch * frames, -1, -1)

        state_memory_mask = None
        if frame_mask is not None:
            state_memory_mask = (
                frame_mask.reshape(batch * frames, 1)
                .expand(batch * frames, tokens)
            )
            # Padded frame rows are not used for caption loss. Unmask one
            # harmless token to avoid all-masked attention producing NaNs.
            padded_rows = state_memory_mask.all(dim=1)
            if padded_rows.any():
                state_memory_mask = state_memory_mask.clone()
                state_memory_mask[padded_rows, 0] = False

        for block in self.state_blocks:
            state_queries = block(
                state_queries, state_memory, state_memory_mask
            )
        state_features = self.state_output_norm(state_queries).reshape(
            batch, frames, self.state_queries_count, self.hidden_dim
        )

        transition_memory = frame_features.reshape(
            batch, frames * tokens, self.hidden_dim
        )
        transition_memory_mask = None
        if frame_mask is not None:
            transition_memory_mask = (
                frame_mask.unsqueeze(-1)
                .expand(batch, frames, tokens)
                .reshape(batch, frames * tokens)
            )

        transition_queries = self.transition_queries.expand(batch, -1, -1)
        for block in self.transition_blocks:
            transition_queries = block(
                transition_queries,
                transition_memory,
                transition_memory_mask,
            )
        transition_features = self.transition_output_norm(transition_queries)

        return {
            "frame_features": frame_features,
            "state_features": state_features,
            "transition_features": transition_features,
        }

    def get_output_dim(self) -> int:
        return self.hidden_dim

    def get_num_queries(self) -> int:
        return self.transition_queries_count
