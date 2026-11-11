
"""End-to-end inference and reference collection for OSCaR-Lite evaluation.

Supports V1, V2 and V3 configurations while preserving the legacy V2
constructor interfaces and defaults.
"""

from __future__ import annotations

import inspect
import random
from typing import Any, Callable

import numpy as np
import torch
from torch.utils.data import DataLoader

from src.sostd.data.build_dataset import build_temporal_dataset
from src.sostd.evaluation.config import EvaluationConfig
from src.sostd.evaluation.dataset import EvaluationDataset, evaluation_collate
from src.sostd.evaluation.inference import InferenceRunner
from src.sostd.evaluation.model_loader import ModelLoader
from src.sostd.evaluation.reference_adapter import ReferenceAdapter


class EvaluationRunner:
    """Load evaluation components and collect predictions and references."""

    def __init__(
        self,
        config: EvaluationConfig,
        dataset_builder: Callable[..., Any] = build_temporal_dataset,
        model_loader_factory: Callable[..., Any] = ModelLoader,
        tokenizer_loader: Callable[..., Any] | None = None,
        inference_runner_factory: Callable[..., Any] = InferenceRunner,
        reference_adapter: ReferenceAdapter | None = None,
    ) -> None:
        self.config = config
        self.dataset_builder = dataset_builder
        self.model_loader_factory = model_loader_factory
        self.tokenizer_loader = tokenizer_loader
        self.inference_runner_factory = inference_runner_factory
        self.reference_adapter = reference_adapter or ReferenceAdapter()

        # Newer configuration fields have defaults for legacy V2 configs.
        self.model_version = getattr(config, "model_version", "v2")
        self.input_mode = getattr(config, "input_mode", "cached_features")
        self.model_config = getattr(config, "model_config", {}) or {}

        self.expected_num_frames = getattr(
            config, "expected_num_frames", 3
        )
        self.expected_num_tokens = getattr(
            config, "expected_num_tokens", 257
        )
        self.expected_feature_dim = getattr(
            config, "expected_feature_dim", 768
        )

    def _set_seed(self) -> None:
        """Set random seeds for reproducible evaluation."""

        random.seed(self.config.seed)
        np.random.seed(self.config.seed)
        torch.manual_seed(self.config.seed)

        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.config.seed)

    def _load_tokenizer(self) -> Any:
        """Load the tokenizer matching the trained language model."""

        if self.tokenizer_loader is not None:
            return self.tokenizer_loader(self.config.tokenizer_name)

        try:
            from transformers import AutoTokenizer
        except ImportError as exc:
            raise ImportError(
                "Install transformers to load the evaluation tokenizer."
            ) from exc

        return AutoTokenizer.from_pretrained(
            self.config.tokenizer_name
        )

    def _load_model(self) -> torch.nn.Module:
        """Load the model using the configured architecture."""

        loader_kwargs = {
            "checkpoint": self.config.checkpoint,
            "device": self.config.device,
        }

        # Preserve compatibility with the original V2 ModelLoader.
        # The extended loader must accept these additional arguments.
        if self.model_version.lower() != "v2" or self.model_config:
            loader_kwargs.update({
                "model_version": self.model_version,
                "model_config": self.model_config,
                "input_mode": self.input_mode,
            })

        model = self.model_loader_factory(**loader_kwargs).load()

        if not isinstance(model, torch.nn.Module):
            raise TypeError(
                "ModelLoader.load() must return a torch.nn.Module; "
                f"received {type(model).__name__}."
            )

        return model

    def _build_dataloader(self) -> DataLoader:
        """Build the evaluation dataloader for the selected feature version."""

        dataset_kwargs = {
            "split": self.config.split,
            "feature_dir": self.config.feature_dir,
            "expected_feature_dim": self.expected_feature_dim,
        }

        # Only pass newer arguments when the dataset builder supports them.
        # This keeps older injected builders and the original V2 builder usable.
        try:
            signature = inspect.signature(self.dataset_builder)
            parameters = signature.parameters
            accepts_kwargs = any(
                parameter.kind == inspect.Parameter.VAR_KEYWORD
                for parameter in parameters.values()
            )
        except (TypeError, ValueError):
            parameters = {}
            accepts_kwargs = False

        optional_dataset_kwargs = {
            "expected_num_tokens": self.expected_num_tokens,
            "input_mode": self.input_mode,
        }

        for name, value in optional_dataset_kwargs.items():
            if accepts_kwargs or name in parameters:
                dataset_kwargs[name] = value

        dataset, _ = self.dataset_builder(**dataset_kwargs)

        if len(dataset) == 0:
            raise ValueError(
                f"The {self.config.split} evaluation dataset is empty."
            )

        evaluation_dataset = EvaluationDataset(dataset)

        if self.config.limit is not None:
            if self.config.limit <= 0:
                raise ValueError(
                    f"Evaluation limit must be positive, "
                    f"received {self.config.limit}."
                )

            evaluation_dataset = torch.utils.data.Subset(
                evaluation_dataset,
                range(min(self.config.limit, len(evaluation_dataset))),
            )

        if len(evaluation_dataset) == 0:
            raise ValueError("No evaluation samples selected.")

        return DataLoader(
            evaluation_dataset,
            batch_size=self.config.batch_size,
            shuffle=False,
            num_workers=self.config.num_workers,
            pin_memory=(
                self.config.pin_memory
                and self.config.device.startswith("cuda")
            ),
            collate_fn=evaluation_collate,
        )

    def _build_inference_runner(
        self,
        model: torch.nn.Module,
        tokenizer: Any,
    ) -> Any:
        """Create a dimension-aware inference runner."""

        inference_kwargs = {
            "model": model,
            "tokenizer": tokenizer,
            "device": self.config.device,
            "amp": self.config.amp,
            "max_state_tokens": self.config.max_state_tokens,
            "max_transition_tokens": self.config.max_transition_tokens,
            "num_beams": self.config.num_beams,
        }

        # The extended InferenceRunner accepts these fields.
        # Keep compatibility with injected legacy factories.
        try:
            signature = inspect.signature(self.inference_runner_factory)
            parameters = signature.parameters
            accepts_kwargs = any(
                parameter.kind == inspect.Parameter.VAR_KEYWORD
                for parameter in parameters.values()
            )
        except (TypeError, ValueError):
            parameters = {}
            accepts_kwargs = False

        dimension_kwargs = {
            "expected_num_frames": self.expected_num_frames,
            "expected_num_tokens": self.expected_num_tokens,
            "expected_feature_dim": self.expected_feature_dim,
        }

        generation_kwargs = {
            "repetition_penalty": self.config.repetition_penalty,
            "no_repeat_ngram_size": self.config.no_repeat_ngram_size,
            "length_penalty": self.config.length_penalty,
        }

        for optional_kwargs in (dimension_kwargs, generation_kwargs):
            for name, value in optional_kwargs.items():
                if accepts_kwargs or name in parameters:
                    inference_kwargs[name] = value

        return self.inference_runner_factory(**inference_kwargs)

    def run(self) -> dict[str, Any]:
        """Run inference and return predictions paired with references."""

        self._set_seed()

        print("=" * 70)
        print(f"OSCaR-Lite {self.model_version.upper()} Evaluation")
        print("=" * 70)
        print(f"Checkpoint: {self.config.checkpoint}")
        print(f"Tokenizer: {self.config.tokenizer_name}")
        print(f"Split: {self.config.split}")
        print(f"Input mode: {self.input_mode}")
        print(f"Feature directory: {self.config.feature_dir}")
        print(
            "Expected feature shape: "
            f"({self.expected_num_frames}, "
            f"{self.expected_num_tokens}, "
            f"{self.expected_feature_dim})"
        )
        print(f"Device: {self.config.device}")

        model = self._load_model()
        tokenizer = self._load_tokenizer()
        inference = self._build_inference_runner(model, tokenizer)
        dataloader = self._build_dataloader()

        print(f"Evaluation batches: {len(dataloader)}")

        predictions: list[dict[str, str]] = []
        references: list[dict[str, str]] = []
        metadata: list[dict[str, Any]] = []

        with torch.inference_mode():
            for batch_index, batch in enumerate(dataloader, start=1):
                batch_predictions = inference.run_batch(batch["frames"])

                batch_references = self.reference_adapter.adapt_batch(
                    batch
                )

                batch_size = len(batch_predictions)

                if batch_size != len(batch_references):
                    raise RuntimeError(
                        "Inference and reference batch sizes do not match: "
                        f"{batch_size} != {len(batch_references)}."
                    )

                if not (
                    batch_size
                    == len(batch["object"])
                    == len(batch["image_paths"])
                ):
                    raise RuntimeError(
                        "Inference and metadata batch sizes do not match: "
                        f"predictions={batch_size}, "
                        f"objects={len(batch['object'])}, "
                        f"image_paths={len(batch['image_paths'])}."
                    )

                predictions.extend(batch_predictions)
                references.extend(batch_references)

                for index in range(batch_size):
                    metadata.append({
                        "object": batch["object"][index],
                        "action": batch["action"][index],
                        "frame_indices": batch["frame_indices"][index],
                        "image_paths": batch["image_paths"][index],
                    })

                print(
                    f"Processed batch {batch_index}/{len(dataloader)} "
                    f"| Samples: {len(predictions)}"
                )

        if not predictions:
            raise RuntimeError("Evaluation produced no predictions.")

        if not (
            len(predictions)
            == len(references)
            == len(metadata)
        ):
            raise RuntimeError(
                "Final prediction, reference and metadata counts differ."
            )

        print("\nInference completed.")
        print(f"Total samples: {len(predictions)}")

        return {
            "model_version": self.model_version,
            "input_mode": self.input_mode,
            "split": self.config.split,
            "num_samples": len(predictions),
            "predictions": predictions,
            "references": references,
            "metadata": metadata,
        }
