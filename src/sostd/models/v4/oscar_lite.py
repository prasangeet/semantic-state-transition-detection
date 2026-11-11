from __future__ import annotations

from typing import Any

import torch
import torch.nn as nn
import torch.nn.functional as F

from src.sostd.models.v4.encoders.dinov2_encoder import DINOv2Encoder
from src.sostd.models.v4.temporal.temporal_fusion import TemporalFusion
from src.sostd.models.v4.components.visual_projection import VisualProjection
from src.sostd.models.v4.language.flan_t5_decoder import FlanT5Decoder
from src.sostd.models.v4.heads.grounding_heads import ObjectHead, ActionHead


class OSCaRLite(nn.Module):
    """
    OSCaR-Lite V4: Hierarchical Spatiotemporal Semantic Captioner.

    DINOv2 token features are processed by factorized spatial/temporal
    attention. A frame-local query decoder produces multiple visual tokens
    for each state caption. A separate video-level query decoder produces
    visual tokens for the transition caption.

    The language model remains FLAN-T5-base. Its visual input is supplied
    through inputs_embeds by FlanT5Decoder.

    Expected cached input: (B, T, N, encoder_dim)
    Expected raw input:    (B, T, C, H, W)
    """

    def __init__(
        self,
        encoder: nn.Module | None = None,
        temporal_fusion: nn.Module | None = None,
        visual_projection: nn.Module | None = None,
        language_decoder: nn.Module | None = None,
        object_head: nn.Module | None = None,
        action_head: nn.Module | None = None,
        max_frames: int = 3,
        temporal_hidden_dim: int = 1024,
        temporal_num_heads: int = 16,
        temporal_num_layers: int = 4,
        num_queries: int = 64,
        state_queries: int = 16,
        query_layers: int = 2,
        object_num_classes: int | None = None,
        action_num_classes: int | None = None,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if max_frames < 1:
            raise ValueError("max_frames must be positive.")
        if temporal_hidden_dim < 1:
            raise ValueError("temporal_hidden_dim must be positive.")
        if temporal_num_heads < 1 or temporal_hidden_dim % temporal_num_heads:
            raise ValueError("temporal_hidden_dim must be divisible by temporal_num_heads.")
        if temporal_num_layers < 1 or query_layers < 1:
            raise ValueError("Layer counts must be positive.")
        if num_queries < 1 or state_queries < 1:
            raise ValueError("Query counts must be positive.")
        if not 0.0 <= dropout < 1.0:
            raise ValueError("dropout must be in [0, 1).")
        if object_num_classes is not None and object_num_classes < 1:
            raise ValueError("object_num_classes must be positive.")
        if action_num_classes is not None and action_num_classes < 1:
            raise ValueError("action_num_classes must be positive.")

        self.max_frames = int(max_frames)
        self.temporal_hidden_dim = int(temporal_hidden_dim)
        self.num_queries = int(num_queries)
        self.state_queries = int(state_queries)

        self.encoder = encoder if encoder is not None else DINOv2Encoder()
        self.encoder_dim = self._get_encoder_dimension(self.encoder)

        self.temporal_fusion = (
            temporal_fusion
            if temporal_fusion is not None
            else TemporalFusion(
                input_dim=self.encoder_dim,
                hidden_dim=temporal_hidden_dim,
                num_heads=temporal_num_heads,
                num_layers=temporal_num_layers,
                num_queries=num_queries,
                state_queries=state_queries,
                max_frames=max_frames,
                query_layers=query_layers,
                dropout=dropout,
            )
        )

        self.language_decoder = (
            language_decoder
            if language_decoder is not None
            else FlanT5Decoder(
                model_name="google/flan-t5-base",
                freeze_backbone=True,
            )
        )
        self.decoder_dim = self._get_decoder_dimension(self.language_decoder)

        # State and transition features share the same hidden dimension, so
        # one projection maps both into FLAN-T5's d_model.
        self.visual_projection = (
            visual_projection
            if visual_projection is not None
            else VisualProjection(
                input_dim=temporal_hidden_dim,
                output_dim=self.decoder_dim,
                dropout=dropout,
            )
        )

        self.object_head = (
            object_head
            if object_head is not None
            else (
                ObjectHead(
                    input_dim=temporal_hidden_dim,
                    num_classes=object_num_classes,
                    dropout=dropout,
                )
                if object_num_classes is not None
                else None
            )
        )

        self.action_head = (
            action_head
            if action_head is not None
            else (
                ActionHead(
                    input_dim=temporal_hidden_dim,
                    num_classes=action_num_classes,
                    dropout=dropout,
                )
                if action_num_classes is not None
                else None
            )
        )

        self._validate_architecture()
        self.visual_dim = self.decoder_dim

    @staticmethod
    def _get_encoder_dimension(encoder: nn.Module) -> int:
        dimension = getattr(encoder, "hidden_size", None)
        if dimension is None:
            dimension = getattr(encoder, "output_dim", None)
        if dimension is None:
            raise ValueError("Encoder must expose hidden_size or output_dim.")
        dimension = int(dimension)
        if dimension < 1:
            raise ValueError("Encoder dimension must be positive.")
        return dimension

    @staticmethod
    def _get_decoder_dimension(decoder: nn.Module) -> int:
        dimension = getattr(decoder, "hidden_dim", None)
        if dimension is None:
            raise ValueError("Decoder must expose hidden_dim.")
        dimension = int(dimension)
        if dimension < 1:
            raise ValueError("Decoder dimension must be positive.")
        return dimension

    def _validate_architecture(self) -> None:
        if self.encoder_dim != self.temporal_hidden_dim:
            raise ValueError(
                "TemporalFusion output and VisualProjection input dimensions "
                "must match encoder_dim/temporal_hidden_dim; got "
                f"{self.encoder_dim} and {self.temporal_hidden_dim}."
            )

        fusion_input = getattr(self.temporal_fusion, "input_dim", None)
        fusion_hidden = getattr(self.temporal_fusion, "hidden_dim", None)
        if fusion_input is not None and fusion_input != self.encoder_dim:
            raise ValueError("TemporalFusion input dimension mismatch.")
        if fusion_hidden is not None and fusion_hidden != self.temporal_hidden_dim:
            raise ValueError("TemporalFusion hidden dimension mismatch.")

        projection_input = getattr(self.visual_projection, "input_dim", None)
        projection_output = getattr(self.visual_projection, "output_dim", None)
        if projection_input is not None and projection_input != self.temporal_hidden_dim:
            raise ValueError("VisualProjection input dimension mismatch.")
        if projection_output is not None and projection_output != self.decoder_dim:
            raise ValueError("VisualProjection output dimension mismatch.")

    def _validate_frame_mask(
        self,
        frame_mask: torch.Tensor | None,
        batch_size: int,
        num_frames: int,
        device: torch.device,
    ) -> torch.Tensor | None:
        if frame_mask is None:
            return None
        if not isinstance(frame_mask, torch.Tensor):
            raise TypeError("frame_mask must be a torch.Tensor.")
        if frame_mask.shape != (batch_size, num_frames):
            raise ValueError("frame_mask must have shape (B, T).")
        frame_mask = frame_mask.to(device=device, dtype=torch.bool)
        if frame_mask.all(dim=1).any():
            raise ValueError("Every sample must contain at least one valid frame.")
        return frame_mask

    def encode_visual(
        self,
        frames: torch.Tensor,
        frame_mask: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        if not isinstance(frames, torch.Tensor):
            raise TypeError("frames must be a torch.Tensor.")
        if not frames.is_floating_point():
            raise TypeError("frames must be floating-point.")
        if frames.ndim not in (4, 5):
            raise ValueError(
                "Expected cached (B,T,N,D) or raw RGB (B,T,C,H,W) frames."
            )

        batch_size, num_frames = frames.shape[:2]
        if batch_size < 1:
            raise ValueError("Batch size must be positive.")
        if not 1 <= num_frames <= self.max_frames:
            raise ValueError(
                f"Received {num_frames} frames; maximum is {self.max_frames}."
            )
        frame_mask = self._validate_frame_mask(
            frame_mask, batch_size, num_frames, frames.device
        )

        if frames.ndim == 4:
            _, _, num_tokens, feature_dim = frames.shape
            if num_tokens < 1:
                raise ValueError("At least one visual token is required.")
            if feature_dim != self.encoder_dim:
                raise ValueError(
                    f"Expected cached feature dimension {self.encoder_dim}, "
                    f"got {feature_dim}."
                )
            encoded = frames
        else:
            _, _, channels, height, width = frames.shape
            if channels != 3 or height < 1 or width < 1:
                raise ValueError("Frames must be non-empty RGB images.")
            flattened = frames.reshape(
                batch_size * num_frames, channels, height, width
            )
            encoded = self.encoder(flattened)
            if not isinstance(encoded, torch.Tensor) or encoded.ndim != 3:
                raise ValueError("Encoder must return (B*T, N, D).")
            if encoded.shape[0] != batch_size * num_frames:
                raise ValueError("Encoder output batch dimension mismatch.")
            if encoded.shape[1] < 1 or encoded.shape[-1] != self.encoder_dim:
                raise ValueError("Encoder output token/feature dimension mismatch.")
            encoded = encoded.reshape(
                batch_size, num_frames, encoded.shape[1], encoded.shape[2]
            )

        if not encoded.is_floating_point():
            raise TypeError("Encoded features must be floating-point.")

        fused = self.temporal_fusion(encoded, frame_mask=frame_mask)
        required = {"frame_features", "state_features", "transition_features"}
        if not isinstance(fused, dict) or not required.issubset(fused):
            raise TypeError(
                "TemporalFusion must return frame_features, state_features, "
                "and transition_features."
            )

        frame_features = fused["frame_features"]
        state_features = fused["state_features"]
        transition_features = fused["transition_features"]

        expected_state = (
            batch_size, num_frames, self.state_queries, self.temporal_hidden_dim
        )
        expected_transition = (
            batch_size, self.num_queries, self.temporal_hidden_dim
        )
        if state_features.shape != expected_state:
            raise RuntimeError(
                f"Unexpected state feature shape {tuple(state_features.shape)}; "
                f"expected {expected_state}."
            )
        if transition_features.shape != expected_transition:
            raise RuntimeError(
                f"Unexpected transition feature shape "
                f"{tuple(transition_features.shape)}; expected {expected_transition}."
            )
        if frame_features.shape[:3] != encoded.shape[:3]:
            raise RuntimeError("TemporalFusion changed the frame/token dimensions.")

        state_embeddings = self.visual_projection(state_features)
        transition_embeddings = self.visual_projection(transition_features)

        return {
            "frame_features": frame_features,
            "state_features": state_features,
            "state_embeddings": state_embeddings,
            "transition_embeddings": transition_embeddings,
            "temporal_features": transition_features,
        }

    def forward(
        self,
        frames: torch.Tensor,
        state_labels: torch.Tensor | None = None,
        transition_labels: torch.Tensor | None = None,
        object_labels: torch.Tensor | None = None,
        action_labels: torch.Tensor | None = None,
        state_mask: torch.Tensor | None = None,
        frame_mask: torch.Tensor | None = None,
    ) -> dict[str, Any]:
        visual = self.encode_visual(frames, frame_mask=frame_mask)
        state_embeddings = visual["state_embeddings"]
        transition_embeddings = visual["transition_embeddings"]
        temporal_features = visual["temporal_features"]

        batch_size, num_frames, state_query_count, decoder_dim = (
            state_embeddings.shape
        )
        state_output = None
        transition_output = None
        object_logits = None
        action_logits = None
        object_loss = None
        action_loss = None

        if state_mask is not None and state_labels is None:
            raise ValueError("state_mask requires state_labels.")

        if state_labels is not None:
            if state_labels.ndim != 3:
                raise ValueError("state_labels must have shape (B, T, L).")
            if state_labels.shape[:2] != (batch_size, num_frames):
                raise ValueError("State labels must match batch/frame dimensions.")
            if state_labels.shape[-1] < 1:
                raise ValueError("State label sequences cannot be empty.")

            flat_labels = state_labels.reshape(batch_size * num_frames, -1)
            valid_rows = (flat_labels != -100).any(dim=1)

            if state_mask is None:
                valid_mask = valid_rows
            else:
                if state_mask.shape != (batch_size, num_frames):
                    raise ValueError("state_mask must have shape (B, T).")
                valid_mask = state_mask.to(
                    device=state_labels.device, dtype=torch.bool
                ).reshape(-1)
                if torch.any(valid_mask & ~valid_rows):
                    raise ValueError(
                        "Valid state captions must contain non-masked tokens."
                    )

            if frame_mask is not None:
                valid_frames = ~frame_mask.to(
                    device=state_labels.device, dtype=torch.bool
                ).reshape(-1)
                if torch.any(valid_mask & ~valid_frames):
                    raise ValueError("Padded frames cannot have valid state labels.")

            if valid_mask.any():
                flat_embeddings = state_embeddings.reshape(
                    batch_size * num_frames, state_query_count, decoder_dim
                )
                selected = valid_mask.to(device=flat_embeddings.device)
                state_output = self.language_decoder(
                    flat_embeddings[selected],
                    labels=flat_labels[valid_mask],
                )

        if transition_labels is not None:
            if transition_labels.ndim != 2:
                raise ValueError("transition_labels must have shape (B, L).")
            if transition_labels.shape[0] != batch_size:
                raise ValueError("Transition labels must match batch size.")
            if transition_labels.shape[-1] < 1:
                raise ValueError("Transition labels cannot be empty.")
            if not (transition_labels != -100).any(dim=1).all():
                raise ValueError("Every sample needs a valid transition label.")

            transition_output = self.language_decoder(
                transition_embeddings,
                labels=transition_labels,
            )

        if object_labels is not None:
            if self.object_head is None:
                raise ValueError("Object labels supplied but ObjectHead is disabled.")
            if object_labels.shape != (batch_size,):
                raise ValueError("object_labels must have shape (B,).")

        if self.object_head is not None:
            object_logits = self.object_head(temporal_features)
            if object_labels is not None:
                object_loss = F.cross_entropy(
                    object_logits,
                    object_labels.to(
                        device=object_logits.device, dtype=torch.long
                    ),
                    ignore_index=-100,
                )

        if action_labels is not None:
            if self.action_head is None:
                raise ValueError("Action labels supplied but ActionHead is disabled.")
            if action_labels.shape != (batch_size,):
                raise ValueError("action_labels must have shape (B,).")

        if self.action_head is not None:
            action_logits = self.action_head(temporal_features)
            if action_labels is not None:
                action_loss = F.cross_entropy(
                    action_logits,
                    action_labels.to(
                        device=action_logits.device, dtype=torch.long
                    ),
                    ignore_index=-100,
                )

        return {
            "state_output": state_output,
            "transition_output": transition_output,
            "object_logits": object_logits,
            "action_logits": action_logits,
            "object_loss": object_loss,
            "action_loss": action_loss,
            "state_embeddings": state_embeddings,
            "transition_embeddings": transition_embeddings,
            "frame_features": visual["frame_features"],
            "state_features": visual["state_features"],
            "temporal_features": temporal_features,
        }

    @torch.no_grad()
    def generate(
        self,
        frames: torch.Tensor,
        max_state_tokens: int = 96,
        max_transition_tokens: int = 160,
        frame_mask: torch.Tensor | None = None,
        **generation_kwargs: Any,
    ) -> dict[str, torch.Tensor]:
        if max_state_tokens < 1 or max_transition_tokens < 1:
            raise ValueError("Generation lengths must be positive.")

        visual = self.encode_visual(frames, frame_mask=frame_mask)
        state_embeddings = visual["state_embeddings"]
        transition_embeddings = visual["transition_embeddings"]

        batch_size, num_frames, query_count, hidden_dim = state_embeddings.shape
        flat_state_embeddings = state_embeddings.reshape(
            batch_size * num_frames, query_count, hidden_dim
        )
        state_tokens = self.language_decoder.generate(
            flat_state_embeddings,
            max_new_tokens=max_state_tokens,
            **generation_kwargs,
        )
        transition_tokens = self.language_decoder.generate(
            transition_embeddings,
            max_new_tokens=max_transition_tokens,
            **generation_kwargs,
        )
        state_tokens = state_tokens.reshape(batch_size, num_frames, -1)

        result = {
            "state_tokens": state_tokens,
            "transition_tokens": transition_tokens,
        }
        if frame_mask is not None:
            result["frame_mask"] = frame_mask.to(
                device=state_tokens.device, dtype=torch.bool
            )
        return result
