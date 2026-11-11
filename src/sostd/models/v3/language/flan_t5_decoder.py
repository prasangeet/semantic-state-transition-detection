
from __future__ import annotations

from typing import Any

import torch
import torch.nn as nn
from transformers import T5ForConditionalGeneration


class FlanT5Decoder(nn.Module):
    """
    Language decoder conditioned on visual embeddings.

    Supports:
        - FLAN-T5-Small
        - FLAN-T5-Base
        - Fully frozen backbone
        - Selective fine-tuning of final encoder/decoder blocks

    Input visual embeddings:
        (B, T, K, D): temporal visual tokens
        (B, S, D): flattened visual sequence

    Visual embeddings must match the T5 d_model dimension.

    Default:
        google/flan-t5-base
        Frozen backbone
    """

    MODEL_VARIANTS = {
        "small": "google/flan-t5-small",
        "base": "google/flan-t5-base",
    }

    MODEL_NAME = MODEL_VARIANTS["base"]

    def __init__(
        self,
        model_name: str = MODEL_NAME,
        freeze_backbone: bool = True,
        unfreeze_last_n_layers: int = 0,
        model: nn.Module | None = None,
    ) -> None:
        super().__init__()

        if unfreeze_last_n_layers < 0:
            raise ValueError(
                "unfreeze_last_n_layers must be non-negative."
            )

        if not freeze_backbone and unfreeze_last_n_layers > 0:
            raise ValueError(
                "freeze_backbone=False cannot be combined with "
                "unfreeze_last_n_layers > 0. Use freeze_backbone=False "
                "for full fine-tuning, or freeze_backbone=True for "
                "selective fine-tuning."
            )

        self.backbone = (
            model
            if model is not None
            else T5ForConditionalGeneration.from_pretrained(
                model_name
            )
        )

        self.hidden_dim = self.backbone.config.d_model
        self.freeze_backbone = freeze_backbone
        self.unfreeze_last_n_layers = unfreeze_last_n_layers

        self._configure_trainable_parameters()

    def _configure_trainable_parameters(self) -> None:
        """
        Configure trainable T5 parameters.

        If freeze_backbone=True and unfreeze_last_n_layers=0,
        the entire T5 backbone remains frozen.

        If unfreeze_last_n_layers > 0, the final N encoder
        and decoder blocks are trainable, even when
        freeze_backbone=True.

        Embeddings and all other parameters remain frozen.
        """

        self.backbone.requires_grad_(False)

        if self.unfreeze_last_n_layers == 0:
            if not self.freeze_backbone:
                self.backbone.requires_grad_(True)
            return

        encoder_blocks = self.backbone.encoder.block
        decoder_blocks = self.backbone.decoder.block

        if self.unfreeze_last_n_layers > len(encoder_blocks):
            raise ValueError(
                "unfreeze_last_n_layers exceeds the number "
                "of encoder blocks."
            )

        if self.unfreeze_last_n_layers > len(decoder_blocks):
            raise ValueError(
                "unfreeze_last_n_layers exceeds the number "
                "of decoder blocks."
            )

        for block in encoder_blocks[-self.unfreeze_last_n_layers:]:
            block.requires_grad_(True)

        for block in decoder_blocks[-self.unfreeze_last_n_layers:]:
            block.requires_grad_(True)

    def train(self, mode: bool = True) -> FlanT5Decoder:
        """
        Respect frozen/trainable parameter configuration.

        Frozen backbone modules remain in evaluation mode.
        Trainable blocks follow the requested training mode.
        """

        super().train(mode)

        if self.freeze_backbone:
            self.backbone.eval()

            if self.unfreeze_last_n_layers > 0:
                for block in self.backbone.encoder.block[
                    -self.unfreeze_last_n_layers:
                ]:
                    block.train(mode)

                for block in self.backbone.decoder.block[
                    -self.unfreeze_last_n_layers:
                ]:
                    block.train(mode)

        return self

    def get_trainable_parameters(self) -> int:
        """Return the number of trainable parameters."""

        return sum(
            parameter.numel()
            for parameter in self.parameters()
            if parameter.requires_grad
        )

    def get_total_parameters(self) -> int:
        """Return the total number of parameters."""

        return sum(
            parameter.numel()
            for parameter in self.parameters()
        )

    def _prepare_visual_inputs(
        self,
        visual_embeddings: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Validate and flatten visual embeddings.

        Returns:
            embeddings: (B, S, D)
            attention_mask: (B, S)
        """

        if not isinstance(visual_embeddings, torch.Tensor):
            raise TypeError(
                "visual_embeddings must be a torch.Tensor."
            )

        if visual_embeddings.ndim == 4:
            batch_size, num_frames, num_tokens, hidden_dim = (
                visual_embeddings.shape
            )

            if batch_size < 1:
                raise ValueError(
                    "Batch size must be positive."
                )

            if num_frames < 1 or num_tokens < 1:
                raise ValueError(
                    "Visual embeddings must contain at least "
                    "one frame and one token."
                )

            embeddings = visual_embeddings.reshape(
                batch_size,
                num_frames * num_tokens,
                hidden_dim,
            )

            expected_mask_shape = (
                batch_size,
                num_frames,
                num_tokens,
            )

            if attention_mask is not None:
                if attention_mask.shape == expected_mask_shape:
                    attention_mask = attention_mask.reshape(
                        batch_size,
                        num_frames * num_tokens,
                    )

                elif attention_mask.shape != (
                    batch_size,
                    num_frames * num_tokens,
                ):
                    raise ValueError(
                        "Attention mask must have shape "
                        f"{expected_mask_shape} or "
                        f"{(batch_size, num_frames * num_tokens)}."
                    )

        elif visual_embeddings.ndim == 3:
            batch_size, sequence_length, hidden_dim = (
                visual_embeddings.shape
            )

            if batch_size < 1:
                raise ValueError(
                    "Batch size must be positive."
                )

            if sequence_length < 1:
                raise ValueError(
                    "Visual embeddings must contain at least "
                    "one token."
                )

            embeddings = visual_embeddings

            if attention_mask is not None and attention_mask.shape != (
                batch_size,
                sequence_length,
            ):
                raise ValueError(
                    "Attention mask must match the visual "
                    "sequence shape."
                )

        else:
            raise ValueError(
                "Expected visual embeddings with shape "
                "(B, T, K, D) or (B, S, D), "
                f"got {tuple(visual_embeddings.shape)}."
            )

        if not embeddings.is_floating_point():
            raise TypeError(
                "Visual embeddings must be floating-point."
            )

        if hidden_dim != self.hidden_dim:
            raise ValueError(
                f"Decoder expects embedding dimension "
                f"{self.hidden_dim}, but received {hidden_dim}. "
                "Check the visual projection dimension."
            )

        if attention_mask is None:
            attention_mask = torch.ones(
                embeddings.shape[:2],
                dtype=torch.long,
                device=embeddings.device,
            )
        else:
            if attention_mask.dtype == torch.bool:
                attention_mask = attention_mask.long()
            elif attention_mask.is_floating_point():
                if not torch.isfinite(attention_mask).all():
                    raise ValueError(
                        "Attention mask must contain finite values."
                    )

            if not torch.all(
                (attention_mask == 0) | (attention_mask == 1)
            ):
                raise ValueError(
                    "Attention mask must contain only 0 and 1."
                )

            attention_mask = attention_mask.to(
                device=embeddings.device,
                dtype=torch.long,
            )

        if not attention_mask.any(dim=1).all():
            raise ValueError(
                "Every visual sequence must contain at least "
                "one unmasked token."
            )

        return embeddings, attention_mask

    def forward(
        self,
        visual_embeddings: torch.Tensor,
        labels: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
    ) -> Any:
        """
        Teacher-forced training.

        T5 executes in FP32 while allowing gradients to propagate
        through the decoder into visual embeddings.
        """

        if labels.ndim != 2:
            raise ValueError(
                "Labels must have shape (B, L)."
            )

        if labels.shape[0] < 1 or labels.shape[1] < 1:
            raise ValueError(
                "Labels must contain a non-empty batch and sequence."
            )

        embeddings, attention_mask = self._prepare_visual_inputs(
            visual_embeddings,
            attention_mask,
        )

        if labels.shape[0] != embeddings.shape[0]:
            raise ValueError(
                "Visual embeddings and labels must have matching "
                "batch dimensions."
            )

        labels = labels.to(
            device=embeddings.device,
            dtype=torch.long,
        )

        with torch.autocast(
            device_type=embeddings.device.type,
            enabled=False,
        ):
            outputs = self.backbone(
                inputs_embeds=embeddings.float(),
                attention_mask=attention_mask,
                labels=labels,
                return_dict=True,
            )

        return outputs

    @torch.no_grad()
    def generate(
        self,
        visual_embeddings: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
        max_new_tokens: int = 96,
        **generation_kwargs: Any,
    ) -> torch.Tensor:
        """
        Autoregressively generate a description conditioned
        on visual embeddings.
        """

        if max_new_tokens < 1:
            raise ValueError(
                "max_new_tokens must be at least 1."
            )

        reserved_arguments = {
            "inputs_embeds",
            "attention_mask",
            "max_new_tokens",
        }

        conflicting_arguments = (
            reserved_arguments.intersection(generation_kwargs)
        )

        if conflicting_arguments:
            raise ValueError(
                "Pass these arguments through their explicit "
                f"parameters: {sorted(conflicting_arguments)}."
            )

        embeddings, attention_mask = self._prepare_visual_inputs(
            visual_embeddings,
            attention_mask,
        )

        with torch.autocast(
            device_type=embeddings.device.type,
            enabled=False,
        ):
            generated_ids = self.backbone.generate(
                inputs_embeds=embeddings.float(),
                attention_mask=attention_mask,
                max_new_tokens=max_new_tokens,
                **generation_kwargs,
            )

        return generated_ids
