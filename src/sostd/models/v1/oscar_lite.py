from __future__ import annotations

import torch
import torch.nn as nn

from src.sostd.models.encoders.dinov2_encoder import DINOv2Encoder
from src.sostd.models.temporal.temporal_fusion import TemporalFusion
from src.sostd.models.components.visual_resampler import VisualResampler
from src.sostd.models.components.visual_projection import VisualProjection
from src.sostd.models.language.flan_t5_decoder import FlanT5Decoder


class OSCaRLite(nn.Module):
    """Lightweight vision-language model for state and transition captioning."""

    def __init__(
        self,
        encoder: nn.Module | None = None,
        temporal_fusion: nn.Module | None = None,
        visual_resampler: nn.Module | None = None,
        visual_projection: nn.Module | None = None,
        language_decoder: nn.Module | None = None,
        max_frames: int = 3,
    ) -> None:
        super().__init__()

        if max_frames < 1:
            raise ValueError("max_frames must be at least 1.")

        self.encoder = encoder or DINOv2Encoder()
        self.temporal_fusion = temporal_fusion or TemporalFusion(
            input_dim=384,
            hidden_dim=256,
            max_frames=max_frames,
        )
        self.visual_resampler = visual_resampler or VisualResampler(
            input_dim=256,
            output_dim=256,
            num_queries=8,
        )
        self.visual_projection = visual_projection or VisualProjection(
            input_dim=256,
            output_dim=512,
        )
        self.language_decoder = language_decoder or FlanT5Decoder()

        self.max_frames = max_frames

    def encode_visual(self, frames: torch.Tensor) -> torch.Tensor:
        """
        Extract and fuse visual representations.

        Accepts either:
            - Raw images shaped (B, T, C, H, W).
            - Precomputed DINOv2 feature tokens shaped (B, T, N, D).

        Returns:
            Projected visual tokens shaped (B, T, K, 512).
        """
        if frames.ndim == 4:
            # Precomputed token tensors: (B, T, N, D) -> bypass DINOv2 encoder
            batch_size, num_frames, num_tokens, input_dim = frames.shape

            if batch_size < 1:
                raise ValueError("Batch size must be at least 1.")

            if num_frames < 1 or num_frames > self.max_frames:
                raise ValueError(
                    f"Received {num_frames} frames; "
                    f"maximum supported is {self.max_frames}."
                )

            encoded = frames

        elif frames.ndim == 5:
            # Raw images: (B, T, C, H, W)
            batch_size, num_frames, channels, height, width = frames.shape

            if batch_size < 1:
                raise ValueError("Batch size must be at least 1.")

            if num_frames < 1:
                raise ValueError("At least one frame is required.")

            if num_frames > self.max_frames:
                raise ValueError(
                    f"Received {num_frames} frames; "
                    f"maximum supported is {self.max_frames}."
                )

            if channels != 3 or height < 1 or width < 1:
                raise ValueError("Frames must be non-empty RGB images.")

            flattened_frames = frames.reshape(
                batch_size * num_frames,
                channels,
                height,
                width,
            )

            encoded = self.encoder(flattened_frames)

            if encoded.ndim != 3:
                raise ValueError(
                    "Encoder must return features shaped (B*T, N, D)."
                )

            if encoded.shape[0] != batch_size * num_frames:
                raise ValueError(
                    "Encoder output batch dimension does not match input."
                )

            encoded = encoded.reshape(
                batch_size,
                num_frames,
                encoded.shape[1],
                encoded.shape[2],
            )
        else:
            raise ValueError(
                "Expected frames with shape (B, T, C, H, W) or (B, T, N, D)."
            )

        fused = self.temporal_fusion(encoded)
        compressed = self.visual_resampler(fused)

        return self.visual_projection(compressed)

    def forward(
        self,
        frames: torch.Tensor,
        state_labels: torch.Tensor | None = None,
        transition_labels: torch.Tensor | None = None,
        state_mask: torch.Tensor | None = None,
    ) -> dict[str, object]:
        """
        Compute state-description and transition-caption outputs.

        Args:
            frames: (B, T, C, H, W) or precomputed (B, T, N, D)
            state_labels: (B, T, L_state), with ignored tokens set to -100.
            transition_labels: (B, L_transition)
            state_mask: Optional boolean tensor (B, T). True identifies
                frames with valid state descriptions.

        Returns:
            Dictionary containing:
                state_output: Decoder output, or None if no valid states.
                transition_output: Decoder output, or None if not requested.
                visual_embeddings: Projected visual tokens (B, T, K, D).
        """
        visual_embeddings = self.encode_visual(frames)

        batch_size, num_frames, num_tokens, hidden_dim = (
            visual_embeddings.shape
        )

        state_output = None
        transition_output = None

        if state_mask is not None and state_labels is None:
            raise ValueError(
                "state_mask cannot be provided without state_labels."
            )

        if state_labels is not None:
            if state_labels.ndim != 3:
                raise ValueError(
                    "state_labels must have shape (B, T, L)."
                )

            if state_labels.shape[:2] != (batch_size, num_frames):
                raise ValueError(
                    "State labels must match the frame batch dimensions."
                )

            flattened_state_labels = state_labels.reshape(
                batch_size * num_frames,
                state_labels.shape[-1],
            )

            valid_label_rows = (
                flattened_state_labels != -100
            ).any(dim=1)

            if state_mask is None:
                valid_state_mask = valid_label_rows
            else:
                if state_mask.shape != (batch_size, num_frames):
                    raise ValueError(
                        "state_mask must have shape (B, T)."
                    )

                valid_state_mask = state_mask.to(
                    device=state_labels.device,
                    dtype=torch.bool,
                ).reshape(-1)

                if torch.any(valid_state_mask & ~valid_label_rows):
                    raise ValueError(
                        "Valid state captions must contain at least "
                        "one non-masked token."
                    )

            if valid_state_mask.any():
                flattened_visual_embeddings = (
                    visual_embeddings.reshape(
                        batch_size * num_frames,
                        num_tokens,
                        hidden_dim,
                    )
                )

                selected_state_embeddings = (
                    flattened_visual_embeddings[
                        valid_state_mask.to(visual_embeddings.device)
                    ]
                )

                selected_state_labels = flattened_state_labels[
                    valid_state_mask
                ]

                state_output = self.language_decoder(
                    selected_state_embeddings,
                    labels=selected_state_labels,
                )

        if transition_labels is not None:
            if transition_labels.ndim != 2:
                raise ValueError(
                    "transition_labels must have shape (B, L)."
                )

            if transition_labels.shape[0] != batch_size:
                raise ValueError(
                    "Transition labels must match the input batch size."
                )

            if not torch.any(transition_labels != -100):
                raise ValueError(
                    "Transition labels must contain at least one "
                    "non-masked token."
                )

            transition_output = self.language_decoder(
                visual_embeddings,
                labels=transition_labels,
            )

        return {
            "state_output": state_output,
            "transition_output": transition_output,
            "visual_embeddings": visual_embeddings,
        }

    @torch.no_grad()
    def generate(
        self,
        frames: torch.Tensor,
        max_state_tokens: int = 64,
        max_transition_tokens: int = 96,
        **generation_kwargs,
    ) -> dict[str, torch.Tensor]:
        """Generate frame-level state descriptions and a transition caption."""

        if max_state_tokens < 1 or max_transition_tokens < 1:
            raise ValueError("Generation lengths must be positive.")

        visual_embeddings = self.encode_visual(frames)

        batch_size, num_frames, num_tokens, hidden_dim = (
            visual_embeddings.shape
        )

        state_embeddings = visual_embeddings.reshape(
            batch_size * num_frames,
            num_tokens,
            hidden_dim,
        )

        state_tokens = self.language_decoder.generate(
            state_embeddings,
            max_new_tokens=max_state_tokens,
            **generation_kwargs,
        )

        transition_tokens = self.language_decoder.generate(
            visual_embeddings,
            max_new_tokens=max_transition_tokens,
            **generation_kwargs,
        )

        state_tokens = state_tokens.reshape(
            batch_size,
            num_frames,
            -1,
        )

        return {
            "state_tokens": state_tokens,
            "transition_tokens": transition_tokens,
        }