
"""Batch inference and caption decoding for OSCaR-Lite evaluation."""

from __future__ import annotations

from typing import Any

import torch
import torch.nn as nn


class InferenceRunner:
    """Run model generation and decode temporal captions."""

    EXPECTED_FRAMES = 3
    EXPECTED_TOKENS = 257
    EXPECTED_FEATURE_DIM = 384

    def __init__(
        self,
        model: nn.Module,
        tokenizer: Any,
        device: str | torch.device = "cuda",
        amp: bool = True,
        max_state_tokens: int = 64,
        max_transition_tokens: int = 96,
        num_beams: int = 4,
        repetition_penalty: float = 1.0,
        no_repeat_ngram_size: int = 0,
        length_penalty: float = 1.0,
        expected_feature_dim: int = EXPECTED_FEATURE_DIM,
        expected_num_tokens: int = EXPECTED_TOKENS,
        expected_num_frames: int = EXPECTED_FRAMES,
    ) -> None:
        self.device = torch.device(device)
        self.amp = amp

        # Generation length settings.
        self.max_state_tokens = max_state_tokens
        self.max_transition_tokens = max_transition_tokens

        # Generation strategy.
        self.num_beams = num_beams
        self.repetition_penalty = repetition_penalty
        self.no_repeat_ngram_size = no_repeat_ngram_size
        self.length_penalty = length_penalty

        # Cached feature dimensions.
        self.expected_feature_dim = expected_feature_dim
        self.expected_num_tokens = expected_num_tokens
        self.expected_num_frames = expected_num_frames

        self._validate_configuration()

        if self.device.type == "cuda" and not torch.cuda.is_available():
            raise RuntimeError("CUDA unavailable.")

        self.model = model.to(self.device)
        self.model.eval()
        self.tokenizer = tokenizer

    def _validate_configuration(self) -> None:
        """Validate generation and feature configuration."""

        if self.max_state_tokens < 1:
            raise ValueError(
                "max_state_tokens must be at least 1."
            )

        if self.max_transition_tokens < 1:
            raise ValueError(
                "max_transition_tokens must be at least 1."
            )

        if self.num_beams < 1:
            raise ValueError(
                "num_beams must be at least 1."
            )

        if self.repetition_penalty <= 0:
            raise ValueError(
                "repetition_penalty must be greater than 0."
            )

        if self.no_repeat_ngram_size < 0:
            raise ValueError(
                "no_repeat_ngram_size must be non-negative."
            )

        if self.length_penalty <= 0:
            raise ValueError(
                "length_penalty must be greater than 0."
            )

        if self.expected_feature_dim not in {384, 768, 1024}:
            raise ValueError(
                "expected_feature_dim must be 384, 768, or 1024."
            )

        if self.expected_num_tokens != self.EXPECTED_TOKENS:
            raise ValueError(
                f"expected_num_tokens must be "
                f"{self.EXPECTED_TOKENS}."
            )

        if self.expected_num_frames != self.EXPECTED_FRAMES:
            raise ValueError(
                f"expected_num_frames must be "
                f"{self.EXPECTED_FRAMES}."
            )

    def _validate_frames(self, frames: Any) -> None:
        """Validate a batch of cached visual features."""

        if not isinstance(frames, torch.Tensor):
            raise TypeError(
                "frames must be a torch.Tensor."
            )

        if frames.ndim != 4:
            raise ValueError(
                "frames must have shape (B, T, N, D)."
            )

        batch, frame_count, token_count, feature_dim = frames.shape

        if batch < 1:
            raise ValueError(
                "Batch must contain at least one sample."
            )

        if frame_count != self.expected_num_frames:
            raise ValueError(
                f"Expected exactly three temporal frames, "
                f"received {frame_count}."
            )

        if token_count != self.expected_num_tokens:
            raise ValueError(
                f"Expected {self.expected_num_tokens} visual tokens, "
                f"received {token_count}."
            )

        if feature_dim != self.expected_feature_dim:
            raise ValueError(
                f"Expected {self.expected_feature_dim} features, "
                f"got {feature_dim}."
            )

        if not frames.is_floating_point():
            raise TypeError(
                "Cached features must be floating-point tensors."
            )

        if not torch.isfinite(frames).all():
            raise ValueError(
                "frames contain non-finite values (NaN or Inf)."
            )

    def _decode(
        self,
        tokens: Any,
        name: str = "tokens",
    ) -> list[str]:
        """Decode a batch of token sequences into captions."""

        if not isinstance(tokens, torch.Tensor):
            raise TypeError(
                f"{name} must be a torch.Tensor."
            )

        if tokens.ndim != 2:
            raise ValueError(
                f"{name} must have shape (B, L)."
            )

        decoded = self.tokenizer.batch_decode(
            tokens.detach().cpu(),
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True,
        )

        if len(decoded) != tokens.shape[0]:
            raise RuntimeError(
                "Unexpected decoder output size."
            )

        return [text.strip() for text in decoded]

    @torch.inference_mode()
    def run_batch(
        self,
        frames: torch.Tensor,
    ) -> list[dict[str, str]]:
        """Generate temporal state and transition captions."""

        self._validate_frames(frames)

        frames = frames.to(
            self.device,
            non_blocking=self.device.type == "cuda",
        )

        use_amp = self.amp and self.device.type == "cuda"

        generation_kwargs = {
            "num_beams": self.num_beams,
            "repetition_penalty": self.repetition_penalty,
            "no_repeat_ngram_size": self.no_repeat_ngram_size,
            "length_penalty": self.length_penalty,
            "do_sample": False,
            "early_stopping": True,
        }

        with torch.autocast(
            device_type=self.device.type,
            dtype=torch.float16,
            enabled=use_amp,
        ):
            generated = self.model.generate(
                frames,
                max_state_tokens=self.max_state_tokens,
                max_transition_tokens=self.max_transition_tokens,
                **generation_kwargs,
            )

        if not isinstance(generated, dict):
            raise TypeError(
                "Model generation must return a dictionary."
            )

        required = {
            "state_tokens",
            "transition_tokens",
        }

        missing = required - generated.keys()

        if missing:
            raise KeyError(
                f"Missing generation outputs: {sorted(missing)}"
            )

        states = generated["state_tokens"]
        transitions = generated["transition_tokens"]

        batch_size = frames.shape[0]

        if not isinstance(states, torch.Tensor):
            raise TypeError(
                "state_tokens must be a torch.Tensor."
            )

        if states.ndim != 3:
            raise ValueError(
                "state_tokens must have shape (B, 3, L)."
            )

        if tuple(states.shape[:2]) != (
            batch_size,
            self.expected_num_frames,
        ):
            raise ValueError(
                "state_tokens dimensions do not match the input batch "
                "size and expected temporal frame count."
            )

        if states.shape[2] < 1:
            raise ValueError(
                "state_tokens contains an empty token sequence."
            )

        if not isinstance(transitions, torch.Tensor):
            raise TypeError(
                "transition_tokens must be a torch.Tensor."
            )

        if transitions.ndim != 2:
            raise ValueError(
                "transition_tokens must have shape (B, L)."
            )

        if transitions.shape[0] != batch_size:
            raise ValueError(
                "transition_tokens batch size does not match "
                "the input batch size."
            )

        if transitions.shape[1] < 1:
            raise ValueError(
                "transition_tokens contains an empty token sequence."
            )

        decoded_states = self._decode(
            states.reshape(
                batch_size * self.expected_num_frames,
                -1,
            ),
            name="state_tokens",
        )

        decoded_transitions = self._decode(
            transitions,
            name="transition_tokens",
        )

        return [
            {
                "before": decoded_states[
                    index * self.expected_num_frames
                ],
                "during": decoded_states[
                    index * self.expected_num_frames + 1
                ],
                "after": decoded_states[
                    index * self.expected_num_frames + 2
                ],
                "transition": decoded_transitions[index],
            }
            for index in range(batch_size)
        ]
