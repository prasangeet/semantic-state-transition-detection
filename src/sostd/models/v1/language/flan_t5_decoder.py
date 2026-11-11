
from __future__ import annotations

import torch
import torch.nn as nn
from transformers import T5ForConditionalGeneration


class FlanT5Decoder(nn.Module):
    """Generate language descriptions conditioned on visual embeddings."""

    MODEL_NAME = "google/flan-t5-small"

    def __init__(
        self,
        model_name: str = MODEL_NAME,
        freeze_backbone: bool = True,
        model: nn.Module | None = None,
    ) -> None:
        super().__init__()

        self.backbone = (
            model
            if model is not None
            else T5ForConditionalGeneration.from_pretrained(model_name)
        )

        self.hidden_dim = self.backbone.config.d_model
        self.freeze_backbone = freeze_backbone

        if freeze_backbone:
            self.backbone.requires_grad_(False)
            self.backbone.eval()

    def train(self, mode: bool = True):
        super().train(mode)

        if self.freeze_backbone:
            self.backbone.eval()

        return self

    def _prepare_visual_inputs(
        self,
        visual_embeddings: torch.Tensor,
        attention_mask: torch.Tensor | None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Accept either:
            (B, T, K, D): temporal visual tokens
            (B, S, D): flattened visual sequence

        Return:
            embeddings: (B, S, D)
            attention_mask: (B, S)
        """

        if visual_embeddings.ndim == 4:
            batch_size, num_frames, num_tokens, hidden_dim = (
                visual_embeddings.shape
            )

            if num_frames < 1 or num_tokens < 1:
                raise ValueError(
                    "Visual embeddings must contain frames and tokens."
                )

            embeddings = visual_embeddings.reshape(
                batch_size,
                num_frames * num_tokens,
                hidden_dim,
            )

            if attention_mask is not None:
                if attention_mask.shape == (
                    batch_size,
                    num_frames,
                    num_tokens,
                ):
                    attention_mask = attention_mask.reshape(
                        batch_size,
                        num_frames * num_tokens,
                    )
                elif attention_mask.shape != (
                    batch_size,
                    num_frames * num_tokens,
                ):
                    raise ValueError(
                        "Attention mask must match the visual sequence."
                    )

        elif visual_embeddings.ndim == 3:
            batch_size, sequence_length, hidden_dim = (
                visual_embeddings.shape
            )

            if sequence_length < 1:
                raise ValueError(
                    "Visual embeddings must contain at least one token."
                )

            embeddings = visual_embeddings

            if attention_mask is not None and attention_mask.shape != (
                batch_size,
                sequence_length,
            ):
                raise ValueError(
                    "Attention mask must match the visual sequence."
                )

        else:
            raise ValueError(
                "Expected visual embeddings with shape (B, T, K, D) "
                "or (B, S, D)."
            )

        if hidden_dim != self.hidden_dim:
            raise ValueError(
                f"Expected embedding dimension {self.hidden_dim}, "
                f"got {hidden_dim}."
            )

        if attention_mask is None:
            attention_mask = torch.ones(
                embeddings.shape[:2],
                dtype=torch.long,
                device=embeddings.device,
            )

        return embeddings, attention_mask

    def forward(
        self,
        visual_embeddings: torch.Tensor,
        labels: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
    ):
        """
        Teacher-forced training.

        T5 executes in FP32 even when the surrounding model uses AMP.
        Gradients still propagate through T5 to visual_embeddings.
        """

        if labels.ndim != 2:
            raise ValueError("Labels must have shape (B, L).")

        embeddings, attention_mask = self._prepare_visual_inputs(
            visual_embeddings,
            attention_mask,
        )

        if labels.shape[0] != embeddings.shape[0]:
            raise ValueError(
                "Visual embeddings and labels must have matching "
                "batch dimensions."
            )

        with torch.autocast(
            device_type=embeddings.device.type,
            enabled=False,
        ):
            embeddings = embeddings.float()

            return self.backbone(
                inputs_embeds=embeddings,
                attention_mask=attention_mask,
                labels=labels,
                return_dict=True,
            )

    @torch.no_grad()
    def generate(
        self,
        visual_embeddings: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
        max_new_tokens: int = 64,
        **generation_kwargs,
    ) -> torch.Tensor:
        """Autoregressively generate a description from visual embeddings."""

        if max_new_tokens < 1:
            raise ValueError("max_new_tokens must be at least 1.")

        embeddings, attention_mask = self._prepare_visual_inputs(
            visual_embeddings,
            attention_mask,
        )

        with torch.autocast(
            device_type=embeddings.device.type,
            enabled=False,
        ):
            return self.backbone.generate(
                inputs_embeds=embeddings.float(),
                attention_mask=attention_mask,
                max_new_tokens=max_new_tokens,
                **generation_kwargs,
            )
