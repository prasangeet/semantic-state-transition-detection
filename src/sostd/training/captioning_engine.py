
from __future__ import annotations

from typing import Any, Sequence

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

from src.sostd.training.losses import LossFactory


IGNORE_INDEX = -100


class CaptioningEngine:
    """
    CUDA-first training and validation engine for OSCaR-Lite V3 and V4.

    V3:
        State caption loss + transition caption loss.

    V4:
        State caption loss + transition caption loss
        + optional auxiliary object classification loss.

    Object classification loss is calculated by this engine using
    LossFactory. Object labels are deliberately not passed to the model,
    preventing duplicate or unweighted model-side object loss calculation.
    """

    def __init__(
        self,
        device: str | torch.device = "cuda",
        amp: bool = True,
        grad_clip: float | None = 1.0,
        state_weight: float = 1.0,
        transition_weight: float = 1.0,
        object_weight: float = 0.0,
        object_class_weights: Sequence[float] | torch.Tensor | None = None,
        expected_feature_dim: int | None = None,
        expected_num_tokens: int = 257,
    ) -> None:
        self.device = torch.device(device)

        if self.device.type != "cuda":
            raise RuntimeError(
                f"CUDA execution is required, received device={self.device}."
            )

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA requested but unavailable.")

        if self.device.index is not None:
            if self.device.index >= torch.cuda.device_count():
                raise RuntimeError(
                    f"CUDA device {self.device.index} does not exist."
                )
        else:
            self.device = torch.device(
                "cuda",
                torch.cuda.current_device(),
            )

        if grad_clip is not None and grad_clip <= 0:
            raise ValueError("grad_clip must be positive.")

        weights = {
            "state_weight": state_weight,
            "transition_weight": transition_weight,
            "object_weight": object_weight,
        }

        for name, value in weights.items():
            if value < 0:
                raise ValueError(f"{name} cannot be negative.")

        if not any(value > 0 for value in weights.values()):
            raise ValueError("At least one loss weight must be positive.")

        if (
            expected_feature_dim is not None
            and expected_feature_dim <= 0
        ):
            raise ValueError("expected_feature_dim must be positive.")

        if expected_num_tokens <= 0:
            raise ValueError("expected_num_tokens must be positive.")

        self.amp = bool(amp)
        self.grad_clip = grad_clip

        self.state_weight = float(state_weight)
        self.transition_weight = float(transition_weight)
        self.object_weight = float(object_weight)

        self.expected_feature_dim = expected_feature_dim
        self.expected_num_tokens = expected_num_tokens

        self.object_class_weights: torch.Tensor | None = None

        if object_class_weights is not None:
            class_weights = torch.as_tensor(
                object_class_weights,
                dtype=torch.float32,
            )

            if class_weights.ndim != 1 or class_weights.numel() == 0:
                raise ValueError(
                    "object_class_weights must be a non-empty 1D sequence."
                )

            if not torch.isfinite(class_weights).all():
                raise ValueError(
                    "object_class_weights contains non-finite values."
                )

            if torch.any(class_weights < 0):
                raise ValueError(
                    "Object class weights cannot be negative."
                )

            if not torch.any(class_weights > 0):
                raise ValueError(
                    "At least one object class weight must be positive."
                )

            self.object_class_weights = class_weights.to(self.device)

        self.object_criterion = LossFactory.create(
            name="cross_entropy",
            weight=self.object_class_weights,
            ignore_index=IGNORE_INDEX,
        ).to(self.device)

        self.scaler = torch.amp.GradScaler(
            "cuda",
            enabled=self.amp,
        )

        print(f"Training device: {self.device}")
        print(f"GPU: {torch.cuda.get_device_name(self.device)}")
        print(f"Mixed precision: {self.amp}")
        print(f"Loss weights: {weights}")
        print(f"Expected visual tokens: {self.expected_num_tokens}")
        print(f"Expected feature dimension: {self.expected_feature_dim}")

        if self.object_class_weights is not None:
            print(
                "Object class weights: "
                f"{self.object_class_weights.numel()} classes"
            )

    # ---------------------------------------------------------
    # Batch preparation and validation
    # ---------------------------------------------------------

    def _prepare_batch(
        self,
        batch: dict[str, Any],
    ) -> dict[str, torch.Tensor]:
        """Move batch tensors to the training device and validate shapes."""

        required_keys = {
            "frames",
            "state_labels",
            "state_mask",
            "transition_labels",
        }

        missing = required_keys.difference(batch)

        if missing:
            raise ValueError(
                f"Missing batch keys: {sorted(missing)}"
            )

        prepared: dict[str, torch.Tensor] = {}

        for name in required_keys:
            value = batch[name]

            if not isinstance(value, torch.Tensor):
                raise TypeError(f"{name} must be a Tensor.")

            prepared[name] = value.to(
                self.device,
                non_blocking=True,
            )

        frames = prepared["frames"]
        state_labels = prepared["state_labels"]
        state_mask = prepared["state_mask"]
        transition_labels = prepared["transition_labels"]

        # Accept raw RGB frames (B,T,C,H,W) or cached features (B,T,N,D).
        if frames.ndim not in (4, 5):
            raise ValueError(
                "frames must have shape (B,T,N,D) or (B,T,C,H,W)."
            )

        if frames.shape[0] < 1 or frames.shape[1] < 1:
            raise ValueError("Frames must contain a non-empty batch and sequence.")

        if frames.ndim == 5:
            if frames.shape[2] != 3:
                raise ValueError(
                    "Raw frames (B,T,C,H,W) must have 3 channels."
                )

            if not torch.is_floating_point(frames):
                raise TypeError(
                    "Raw image frames must be floating-point tensors."
                )

            if not torch.isfinite(frames).all():
                raise ValueError(
                    "Raw image frames contain non-finite values."
                )

        else:
            if frames.shape[2] != self.expected_num_tokens:
                raise ValueError(
                    f"Expected {self.expected_num_tokens} visual tokens, "
                    f"received {frames.shape[2]}."
                )

            if (
                self.expected_feature_dim is not None
                and frames.shape[3] != self.expected_feature_dim
            ):
                raise ValueError(
                    "Feature dimension mismatch: "
                    f"expected {self.expected_feature_dim}, "
                    f"received {frames.shape[3]}."
                )

            if not torch.is_floating_point(frames):
                raise TypeError(
                    "Precomputed visual features must be floating-point."
                )

            if not torch.isfinite(frames).all():
                raise ValueError(
                    "Precomputed visual features contain non-finite values."
                )

        # Validate supervision dimensions.
        if state_labels.ndim != 3:
            raise ValueError(
                "state_labels must have shape (B,T,L)."
            )

        if state_mask.ndim != 2:
            raise ValueError(
                "state_mask must have shape (B,T)."
            )

        if transition_labels.ndim != 2:
            raise ValueError(
                "transition_labels must have shape (B,L)."
            )

        batch_size, num_frames = frames.shape[:2]

        if state_labels.shape[:2] != (batch_size, num_frames):
            raise ValueError(
                "State labels do not match frame dimensions."
            )

        if state_mask.shape != (batch_size, num_frames):
            raise ValueError(
                "State mask does not match frame dimensions."
            )

        if transition_labels.shape[0] != batch_size:
            raise ValueError(
                "Transition labels do not match batch size."
            )

        if state_mask.dtype != torch.bool:
            raise TypeError("state_mask must have dtype bool.")

        if state_labels.shape[-1] < 1 or transition_labels.shape[-1] < 1:
            raise ValueError("Caption label sequences cannot be empty.")

        if not torch.any(transition_labels != IGNORE_INDEX):
            raise ValueError("No valid transition target tokens.")

        prepared["state_labels"] = state_labels.long()
        prepared["transition_labels"] = transition_labels.long()

        # Optional V4 object supervision.
        # V3 batches do not contain this key.
        if "object_labels" in batch:
            object_labels = batch["object_labels"]

            if not isinstance(object_labels, torch.Tensor):
                raise TypeError("object_labels must be a Tensor.")

            if object_labels.ndim != 1:
                raise ValueError(
                    "object_labels must have shape (B,)."
                )

            if object_labels.shape[0] != batch_size:
                raise ValueError(
                    "Object labels do not match batch size."
                )

            if object_labels.dtype not in (
                torch.int8,
                torch.int16,
                torch.int32,
                torch.int64,
                torch.uint8,
            ):
                raise TypeError(
                    "object_labels must contain integer class indices."
                )

            prepared["object_labels"] = object_labels.to(
                device=self.device,
                dtype=torch.long,
                non_blocking=True,
            )

        return prepared

    # ---------------------------------------------------------
    # Loss handling
    # ---------------------------------------------------------

    @staticmethod
    def _extract_loss(
        output: Any,
        task_name: str,
    ) -> torch.Tensor | None:
        """Extract and validate a scalar loss from a decoder output."""

        if output is None:
            return None

        loss = getattr(output, "loss", None)

        if loss is None or not isinstance(loss, torch.Tensor):
            raise ValueError(f"Invalid {task_name} loss.")

        if loss.ndim != 0:
            raise ValueError(f"{task_name} loss must be scalar.")

        if not torch.isfinite(loss).item():
            raise FloatingPointError(
                f"Non-finite {task_name} loss."
            )

        return loss

    def _compute_object_loss(
        self,
        object_logits: Any,
        object_labels: torch.Tensor,
    ) -> torch.Tensor | None:
        """Compute class-weighted V4 object classification loss."""

        valid_mask = object_labels != IGNORE_INDEX

        if not valid_mask.any():
            return None

        if not isinstance(object_logits, torch.Tensor):
            raise TypeError(
                "Object labels were provided, but the model did not return "
                "a Tensor named 'object_logits'."
            )

        if object_logits.ndim != 2:
            raise ValueError("object_logits must have shape (B,C).")

        if object_logits.shape[0] != object_labels.shape[0]:
            raise ValueError(
                "Object logits and labels have different batch sizes."
            )

        if object_logits.shape[1] <= 1:
            raise ValueError(
                "Object classifier must predict at least two classes."
            )

        if not torch.isfinite(object_logits).all():
            raise FloatingPointError(
                "Object logits contain non-finite values."
            )

        valid_labels = object_labels[valid_mask]

        if torch.any(valid_labels < 0):
            raise ValueError(
                "Object labels contain invalid negative class indices."
            )

        if torch.any(valid_labels >= object_logits.shape[1]):
            raise ValueError(
                "An object label exceeds the number of classifier classes. "
                f"Classifier has {object_logits.shape[1]} classes."
            )

        if self.object_class_weights is not None:
            if self.object_class_weights.numel() != object_logits.shape[1]:
                raise ValueError(
                    "Object class weight count does not match classifier "
                    f"output dimension ({self.object_class_weights.numel()} "
                    f"vs {object_logits.shape[1]})."
                )

        loss = self.object_criterion(
            object_logits.float(),
            object_labels,
        )

        if not torch.isfinite(loss).item():
            raise FloatingPointError(
                "Non-finite object classification loss."
            )

        return loss

    # ---------------------------------------------------------
    # Metric helpers
    # ---------------------------------------------------------

    @staticmethod
    def _token_count(labels: torch.Tensor) -> int:
        """Count valid target tokens, excluding ignored positions."""

        return int((labels != IGNORE_INDEX).sum().item())

    @staticmethod
    def _object_confusion_matrix(
        logits: torch.Tensor,
        labels: torch.Tensor,
    ) -> torch.Tensor:
        """Build a confusion matrix for valid object labels."""

        valid_mask = labels != IGNORE_INDEX
        num_classes = logits.shape[1]

        if not valid_mask.any():
            return torch.zeros(
                (num_classes, num_classes),
                dtype=torch.int64,
                device="cpu",
            )

        predictions = logits.detach().argmax(dim=1)[valid_mask]
        targets = labels[valid_mask]

        encoded = targets * num_classes + predictions

        confusion = torch.bincount(
            encoded,
            minlength=num_classes * num_classes,
        ).reshape(num_classes, num_classes)

        return confusion.to(device="cpu", dtype=torch.int64)

    @staticmethod
    def _object_metrics(
        confusion: torch.Tensor,
    ) -> dict[str, float | int]:
        """
        Calculate accuracy and macro-F1.

        Macro-F1 is calculated over classes with at least one
        ground-truth example in the evaluated epoch.
        """

        total = int(confusion.sum().item())

        if total == 0:
            return {
                "object_accuracy": 0.0,
                "object_macro_f1": 0.0,
                "object_samples": 0,
            }

        matrix = confusion.to(torch.float64)

        true_positive = torch.diag(matrix)
        support = matrix.sum(dim=1)
        predicted_count = matrix.sum(dim=0)

        accuracy = (
            true_positive.sum() / matrix.sum()
        ).item()

        denominator = support + predicted_count

        f1 = torch.zeros_like(true_positive)

        valid_denominator = denominator > 0

        f1[valid_denominator] = (
            2.0
            * true_positive[valid_denominator]
            / denominator[valid_denominator]
        )

        present_classes = support > 0
        macro_f1 = f1[present_classes].mean().item()

        return {
            "object_accuracy": float(accuracy),
            "object_macro_f1": float(macro_f1),
            "object_samples": total,
        }

    def _running_metrics(
        self,
        state_loss_sum: float,
        transition_loss_sum: float,
        state_token_count: int,
        transition_token_count: int,
        object_loss_sum: float = 0.0,
        object_loss_denominator: float = 0.0,
        include_object: bool = False,
    ) -> dict[str, float]:
        """
        Aggregate epoch losses using their correct reduction denominators.

        Caption decoder losses are token means, so they are aggregated by
        valid target-token count. Weighted cross-entropy uses the sum of
        target-class weights as its mean-reduction denominator, rather than
        the number of examples.
        """
        state_loss = (
            state_loss_sum / state_token_count
            if state_token_count
            else 0.0
        )
        transition_loss = (
            transition_loss_sum / transition_token_count
            if transition_token_count
            else 0.0
        )

        metrics = {
            "loss": (
                self.state_weight * state_loss
                + self.transition_weight * transition_loss
            ),
            "state_loss": state_loss,
            "transition_loss": transition_loss,
        }

        if include_object:
            object_loss = (
                object_loss_sum / object_loss_denominator
                if object_loss_denominator > 0
                else 0.0
            )
            metrics["object_loss"] = object_loss
            metrics["loss"] += self.object_weight * object_loss

        return metrics

    # ---------------------------------------------------------
    # Epoch execution
    # ---------------------------------------------------------

    def _run_epoch(
        self,
        model: nn.Module,
        dataloader: DataLoader,
        optimizer: torch.optim.Optimizer | None = None,
    ) -> dict[str, float | int]:
        """Execute one training or validation epoch."""

        training = optimizer is not None

        model.to(self.device)

        try:
            model_device = next(model.parameters()).device
        except StopIteration as exc:
            raise ValueError("Model contains no parameters.") from exc

        if model_device.type != "cuda":
            raise RuntimeError("Model is not running on CUDA.")

        for name, parameter in model.named_parameters():
            if parameter.device != self.device:
                raise RuntimeError(
                    f"Parameter {name} is on {parameter.device}, "
                    f"expected {self.device}."
                )

        model.train(training)

        state_loss_sum = 0.0
        transition_loss_sum = 0.0
        object_loss_sum = 0.0
        object_loss_denominator_sum = 0.0
        object_sample_count = 0

        state_token_count = 0
        transition_token_count = 0

        total_samples = 0
        total_batches = 0

        object_confusion: torch.Tensor | None = None
        include_object = False

        progress = tqdm(
            dataloader,
            desc="Training" if training else "Validation",
            leave=True,
            dynamic_ncols=True,
        )

        context = torch.enable_grad if training else torch.no_grad

        with context():
            for batch in progress:
                prepared = self._prepare_batch(batch)

                frames = prepared["frames"]
                state_labels = prepared["state_labels"]
                state_mask = prepared["state_mask"]
                transition_labels = prepared["transition_labels"]

                has_object_labels = "object_labels" in prepared

                if has_object_labels:
                    include_object = True
                    object_labels = prepared["object_labels"]
                else:
                    object_labels = None

                if training:
                    optimizer.zero_grad(set_to_none=True)

                with torch.autocast(
                    device_type="cuda",
                    dtype=torch.float16,
                    enabled=self.amp,
                ):
                    # Do not pass object_labels to the model.
                    # V4 returns object_logits without labels, allowing
                    # this engine to calculate the weighted loss once.
                    # V3's forward signature remains unchanged.
                    outputs = model(
                        frames,
                        state_labels=state_labels,
                        transition_labels=transition_labels,
                        state_mask=state_mask,
                    )

                    if not isinstance(outputs, dict):
                        raise TypeError(
                            "Model must return a dictionary."
                        )

                    state_loss = self._extract_loss(
                        outputs.get("state_output"),
                        "State",
                    )

                    transition_loss = self._extract_loss(
                        outputs.get("transition_output"),
                        "Transition",
                    )

                    if (
                        state_loss is None
                        and transition_loss is None
                    ):
                        raise ValueError(
                            "Model returned no valid captioning losses."
                        )

                    object_loss = None

                    if has_object_labels:
                        object_loss = self._compute_object_loss(
                            outputs.get("object_logits"),
                            object_labels,
                        )

                    batch_loss = None

                    if state_loss is not None and self.state_weight > 0:
                        batch_loss = self.state_weight * state_loss

                    if (
                        transition_loss is not None
                        and self.transition_weight > 0
                    ):
                        component = (
                            self.transition_weight * transition_loss
                        )

                        batch_loss = (
                            component
                            if batch_loss is None
                            else batch_loss + component
                        )

                    if object_loss is not None and self.object_weight > 0:
                        component = self.object_weight * object_loss

                        batch_loss = (
                            component
                            if batch_loss is None
                            else batch_loss + component
                        )

                if batch_loss is None:
                    raise RuntimeError(
                        "Combined batch loss was not calculated. "
                        "Check loss weights and available supervision."
                    )

                if not torch.isfinite(batch_loss).item():
                    raise FloatingPointError(
                        "Non-finite combined loss."
                    )

                if training:
                    self.scaler.scale(batch_loss).backward()

                    if self.grad_clip is not None:
                        self.scaler.unscale_(optimizer)

                        nn.utils.clip_grad_norm_(
                            (
                                parameter
                                for parameter in model.parameters()
                                if parameter.requires_grad
                            ),
                            max_norm=self.grad_clip,
                        )

                    self.scaler.step(optimizer)
                    self.scaler.update()

                # Aggregate caption losses by valid token count.
                batch_state_tokens = self._token_count(state_labels)
                batch_transition_tokens = self._token_count(
                    transition_labels
                )

                if state_loss is not None:
                    state_loss_sum += (
                        state_loss.detach().item()
                        * batch_state_tokens
                    )
                    state_token_count += batch_state_tokens

                if transition_loss is not None:
                    transition_loss_sum += (
                        transition_loss.detach().item()
                        * batch_transition_tokens
                    )
                    transition_token_count += batch_transition_tokens

                # Aggregate object loss using the exact denominator of
                # weighted cross-entropy's mean reduction. With class weights,
                # that denominator is sum(weight[target]); without weights,
                # it is the number of valid targets.
                if object_loss is not None:
                    valid_object_labels = object_labels[
                        object_labels != IGNORE_INDEX
                    ]
                    valid_object_count = int(valid_object_labels.numel())

                    if self.object_class_weights is None:
                        batch_object_denominator = float(valid_object_count)
                    else:
                        batch_object_denominator = float(
                            self.object_class_weights[
                                valid_object_labels
                            ].sum().item()
                        )

                    object_loss_sum += (
                        object_loss.detach().item()
                        * batch_object_denominator
                    )
                    object_loss_denominator_sum += batch_object_denominator
                    object_sample_count += valid_object_count

                # Object metrics.
                if has_object_labels:
                    batch_logits = outputs.get("object_logits")

                    if isinstance(batch_logits, torch.Tensor):
                        batch_confusion = self._object_confusion_matrix(
                            batch_logits,
                            object_labels,
                        )

                        if object_confusion is None:
                            object_confusion = batch_confusion
                        else:
                            if object_confusion.shape != batch_confusion.shape:
                                raise ValueError(
                                    "Object classifier output dimension "
                                    "changed during the epoch."
                                )

                            object_confusion += batch_confusion

                total_samples += frames.shape[0]
                total_batches += 1

                metrics = self._running_metrics(
                    state_loss_sum,
                    transition_loss_sum,
                    state_token_count,
                    transition_token_count,
                    object_loss_sum,
                    object_loss_denominator_sum,
                    include_object=include_object,
                )

                postfix = {
                    "loss": f"{metrics['loss']:.4f}",
                    "state_loss": f"{metrics['state_loss']:.4f}",
                    "transition_loss": (
                        f"{metrics['transition_loss']:.4f}"
                    ),
                }

                if include_object:
                    postfix["object_loss"] = (
                        f"{metrics['object_loss']:.4f}"
                    )

                progress.set_postfix(postfix)

        if total_batches == 0:
            raise ValueError("DataLoader produced no batches.")

        metrics = self._running_metrics(
            state_loss_sum,
            transition_loss_sum,
            state_token_count,
            transition_token_count,
            object_loss_sum,
            object_loss_denominator_sum,
            include_object=include_object,
        )

        result: dict[str, float | int] = {
            **metrics,
            "state_tokens": state_token_count,
            "transition_tokens": transition_token_count,
            "samples": total_samples,
            "batches": total_batches,
        }

        # Preserve V3's metric structure.
        if include_object:
            if object_confusion is not None:
                result.update(
                    self._object_metrics(object_confusion)
                )
            else:
                result.update({
                    "object_accuracy": 0.0,
                    "object_macro_f1": 0.0,
                    "object_samples": 0,
                })

        return result

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def train_one_epoch(
        self,
        model: nn.Module,
        dataloader: DataLoader,
        optimizer: torch.optim.Optimizer,
    ) -> dict[str, float | int]:
        """Run one training epoch."""

        return self._run_epoch(
            model=model,
            dataloader=dataloader,
            optimizer=optimizer,
        )

    def validate(
        self,
        model: nn.Module,
        dataloader: DataLoader,
    ) -> dict[str, float | int]:
        """Run one validation epoch."""

        return self._run_epoch(
            model=model,
            dataloader=dataloader,
            optimizer=None,
        )
