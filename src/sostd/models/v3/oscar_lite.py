
from __future__ import annotations

import torch
import torch.nn as nn

from src.sostd.models.encoders.dinov2_encoder import DINOv2Encoder
from src.sostd.models.temporal.temporal_fusion import TemporalFusion
from src.sostd.models.components.visual_resampler import VisualResampler
from src.sostd.models.components.visual_projection import VisualProjection
from src.sostd.models.language.flan_t5_decoder import FlanT5Decoder


class OSCaRLite(nn.Module):
    """
    Vision-language model for semantic object-state and
    state-transition captioning.

    V3 architecture:

        DINOv2-Large (1024)
            -> Temporal Fusion (1024)
            -> Visual Resampler (32 queries, 1024)
            -> Visual Projection (768)
            -> FLAN-T5-Base (768)

    Inputs:
        Raw RGB frames:       (B, T, C, H, W)
        Cached DINO features: (B, T, N, D)

    Outputs:
        Frame-level state captions.
        Video-level transition captions.
    """

    def __init__(
        self,
        encoder: nn.Module | None = None,
        temporal_fusion: nn.Module | None = None,
        visual_resampler: nn.Module | None = None,
        visual_projection: nn.Module | None = None,
        language_decoder: nn.Module | None = None,
        max_frames: int = 3,
        temporal_hidden_dim: int = 1024,
        temporal_num_heads: int = 16,
        temporal_num_layers: int = 4,
        num_queries: int = 32,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if max_frames < 1:
            raise ValueError("max_frames must be at least 1.")

        if temporal_hidden_dim < 1:
            raise ValueError("temporal_hidden_dim must be positive.")

        if temporal_num_heads < 1:
            raise ValueError("temporal_num_heads must be positive.")

        if temporal_hidden_dim % temporal_num_heads != 0:
            raise ValueError(
                "temporal_hidden_dim must be divisible by "
                "temporal_num_heads."
            )

        if temporal_num_layers < 1:
            raise ValueError("temporal_num_layers must be positive.")

        if num_queries < 1:
            raise ValueError("num_queries must be positive.")

        self.max_frames = max_frames

        # 1. Visual encoder
        self.encoder = (
            encoder
            if encoder is not None
            else DINOv2Encoder()
        )

        encoder_dim = self._get_encoder_dimension(self.encoder)

        # 2. Temporal fusion
        self.temporal_fusion = (
            temporal_fusion
            if temporal_fusion is not None
            else TemporalFusion(
                input_dim=encoder_dim,
                hidden_dim=temporal_hidden_dim,
                num_heads=temporal_num_heads,
                num_layers=temporal_num_layers,
                max_frames=max_frames,
                dropout=dropout,
            )
        )

        fusion_dim = self._get_temporal_output_dimension(
            self.temporal_fusion
        )

        if fusion_dim is None:
            fusion_dim = temporal_hidden_dim

        # 3. Visual resampler
        self.visual_resampler = (
            visual_resampler
            if visual_resampler is not None
            else VisualResampler(
                input_dim=fusion_dim,
                output_dim=fusion_dim,
                num_queries=num_queries,
                num_heads=temporal_num_heads,
                dropout=dropout,
            )
        )

        resampler_dim = self._get_resampler_output_dimension(
            self.visual_resampler
        )

        if resampler_dim is None:
            resampler_dim = fusion_dim

        # 4. Language decoder
        self.language_decoder = (
            language_decoder
            if language_decoder is not None
            else FlanT5Decoder(
                model_name="google/flan-t5-base",
            )
        )

        decoder_dim = self._get_decoder_dimension(
            self.language_decoder
        )

        # 5. Visual projection
        self.visual_projection = (
            visual_projection
            if visual_projection is not None
            else VisualProjection(
                input_dim=resampler_dim,
                output_dim=decoder_dim,
                dropout=dropout,
            )
        )

        self._validate_architecture(
            encoder_dim=encoder_dim,
            fusion_dim=fusion_dim,
            resampler_dim=resampler_dim,
            decoder_dim=decoder_dim,
        )

        self.visual_dim = decoder_dim

    # ---------------------------------------------------------
    # Dimension discovery
    # ---------------------------------------------------------

    @staticmethod
    def _get_encoder_dimension(encoder: nn.Module) -> int:
        """Discover the encoder output feature dimension."""

        dimension = getattr(encoder, "hidden_size", None)

        if dimension is None:
            dimension = getattr(encoder, "output_dim", None)

        if dimension is None:
            raise ValueError(
                "Cannot determine encoder output dimension. "
                "The encoder must expose hidden_size or output_dim."
            )

        return int(dimension)

    @staticmethod
    def _get_temporal_output_dimension(
        temporal_fusion: nn.Module,
    ) -> int | None:
        """Discover temporal fusion output dimension."""

        norm = getattr(temporal_fusion, "norm", None)

        if isinstance(norm, nn.LayerNorm):
            return int(norm.normalized_shape[-1])

        dimension = getattr(temporal_fusion, "output_dim", None)

        if dimension is not None:
            return int(dimension)

        return None

    @staticmethod
    def _get_resampler_output_dimension(
        resampler: nn.Module,
    ) -> int | None:
        """Discover resampler output dimension."""

        queries = getattr(resampler, "query_tokens", None)

        if isinstance(queries, torch.Tensor):
            return int(queries.shape[-1])

        dimension = getattr(resampler, "output_dim", None)

        if dimension is not None:
            return int(dimension)

        return None

    @staticmethod
    def _get_decoder_dimension(decoder: nn.Module) -> int:
        """Discover language decoder embedding dimension."""

        dimension = getattr(decoder, "hidden_dim", None)

        if dimension is None:
            raise ValueError(
                "Cannot determine language decoder dimension. "
                "Expected decoder.hidden_dim."
            )

        return int(dimension)

    # ---------------------------------------------------------
    # Architecture validation
    # ---------------------------------------------------------

    def _validate_architecture(
        self,
        encoder_dim: int,
        fusion_dim: int,
        resampler_dim: int,
        decoder_dim: int,
    ) -> None:
        """Validate dimensions between connected components."""

        fusion_input = getattr(
            self.temporal_fusion,
            "input_projection",
            None,
        )

        if isinstance(fusion_input, nn.Linear):
            if fusion_input.in_features != encoder_dim:
                raise ValueError(
                    "TemporalFusion input dimension mismatch: "
                    f"expected {encoder_dim}, "
                    f"got {fusion_input.in_features}."
                )

        resampler_input = getattr(
            self.visual_resampler,
            "input_projection",
            None,
        )

        if isinstance(resampler_input, nn.Linear):
            if resampler_input.in_features != fusion_dim:
                raise ValueError(
                    "VisualResampler input dimension mismatch: "
                    f"expected {fusion_dim}, "
                    f"got {resampler_input.in_features}."
                )

        elif isinstance(resampler_input, nn.Identity):
            if fusion_dim != resampler_dim:
                raise ValueError(
                    "Identity resampler projection requires matching "
                    "input and output dimensions."
                )

        projection_input = getattr(
            self.visual_projection,
            "input_dim",
            None,
        )

        projection_output = getattr(
            self.visual_projection,
            "output_dim",
            None,
        )

        if (
            projection_input is not None
            and projection_input != resampler_dim
        ):
            raise ValueError(
                "VisualProjection input dimension mismatch: "
                f"expected {resampler_dim}, got {projection_input}."
            )

        if (
            projection_output is not None
            and projection_output != decoder_dim
        ):
            raise ValueError(
                "VisualProjection output dimension mismatch: "
                f"expected {decoder_dim}, got {projection_output}."
            )

    # ---------------------------------------------------------
    # Visual encoding
    # ---------------------------------------------------------

    def encode_visual(self, frames: torch.Tensor) -> torch.Tensor:
        """
        Extract, temporally fuse and compress visual representations.

        Args:
            frames:
                Raw RGB images: (B, T, C, H, W)
                Cached features: (B, T, N, D)

        Returns:
            Projected visual tokens: (B, T, K, decoder_dim)
        """

        if not isinstance(frames, torch.Tensor):
            raise TypeError("frames must be a torch.Tensor.")

        if not frames.is_floating_point():
            raise TypeError("frames must be floating-point.")

        if frames.ndim == 4:
            # Precomputed DINOv2 features.
            batch_size, num_frames, num_tokens, input_dim = frames.shape

            if batch_size < 1:
                raise ValueError("Batch size must be at least 1.")

            if num_frames < 1 or num_frames > self.max_frames:
                raise ValueError(
                    f"Received {num_frames} frames; "
                    f"maximum supported is {self.max_frames}."
                )

            if num_tokens < 1:
                raise ValueError("At least one visual token is required.")

            expected_dim = self._get_encoder_dimension(self.encoder)

            if input_dim != expected_dim:
                raise ValueError(
                    f"Expected cached feature dimension "
                    f"{expected_dim}, got {input_dim}."
                )

            encoded = frames

        elif frames.ndim == 5:
            # Raw RGB frames.
            batch_size, num_frames, channels, height, width = frames.shape

            if batch_size < 1:
                raise ValueError("Batch size must be at least 1.")

            if num_frames < 1 or num_frames > self.max_frames:
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

            if encoded.shape[-1] != self._get_encoder_dimension(
                self.encoder
            ):
                raise ValueError(
                    "Encoder output feature dimension does not match "
                    "its declared hidden dimension."
                )

            encoded = encoded.reshape(
                batch_size,
                num_frames,
                encoded.shape[1],
                encoded.shape[2],
            )

        else:
            raise ValueError(
                "Expected frames shaped (B, T, C, H, W) "
                "or (B, T, N, D)."
            )

        fused = self.temporal_fusion(encoded)
        compressed = self.visual_resampler(fused)
        projected = self.visual_projection(compressed)

        if projected.ndim != 4:
            raise ValueError(
                "Visual pipeline must return embeddings shaped (B, T, K, D)."
            )

        if projected.shape[0] != batch_size:
            raise ValueError("Visual pipeline changed the batch dimension.")

        if projected.shape[1] != num_frames:
            raise ValueError("Visual pipeline changed the frame dimension.")

        if projected.shape[-1] != self.visual_dim:
            raise ValueError(
                f"Expected projected dimension {self.visual_dim}, "
                f"got {projected.shape[-1]}."
            )

        return projected

    # ---------------------------------------------------------
    # Training forward pass
    # ---------------------------------------------------------

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
            frames: (B, T, C, H, W) or cached (B, T, N, D).
            state_labels: (B, T, L_state), ignored tokens = -100.
            transition_labels: (B, L_transition).
            state_mask: Optional boolean tensor (B, T).

        Returns:
            state_output
            transition_output
            visual_embeddings
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

            if state_labels.shape[-1] < 1:
                raise ValueError("State labels must have a non-empty sequence.")

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
                flattened_visual_embeddings = visual_embeddings.reshape(
                    batch_size * num_frames,
                    num_tokens,
                    hidden_dim,
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

            if transition_labels.shape[-1] < 1:
                raise ValueError(
                    "Transition labels must have a non-empty sequence."
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

    # ---------------------------------------------------------
    # Generation
    # ---------------------------------------------------------

    @torch.no_grad()
    def generate(
        self,
        frames: torch.Tensor,
        max_state_tokens: int = 64,
        max_transition_tokens: int = 96,
        **generation_kwargs,
    ) -> dict[str, torch.Tensor]:
        """Generate frame-level state descriptions and transition captions."""

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
