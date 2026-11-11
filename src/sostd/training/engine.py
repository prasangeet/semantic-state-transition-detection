from __future__ import annotations

from typing import Any

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


class TrainingEngine:
    """
    PyTorch training and validation engine.

    Supports:
        - Image-level classification: (B, C)
        - Temporal classification: (B, T, C)
        - Automatic mixed precision on CUDA
        - Gradient clipping
        - Batch-level and epoch-level metric aggregation

    Batch formats:
        (inputs, targets)

        {
            "inputs": inputs,
            "targets": targets,
        }
    """

    def __init__(
        self,
        device: str | torch.device = "cpu",
        amp: bool = False,
        grad_clip: float | None = None,
    ):
        self.device = torch.device(device)

        if self.device.type == "cuda" and not torch.cuda.is_available():
            raise RuntimeError("CUDA requested but not available.")

        if grad_clip is not None and grad_clip <= 0:
            raise ValueError("grad_clip must be positive.")

        self.amp = amp and self.device.type == "cuda"
        self.grad_clip = grad_clip

        self.scaler = torch.amp.GradScaler(
            "cuda",
            enabled=self.amp,
        )

    @staticmethod
    def _unpack_batch(batch: Any):
        """Extract inputs and targets from supported batch formats."""

        if isinstance(batch, dict):
            if "inputs" not in batch or "targets" not in batch:
                raise ValueError(
                    "Dictionary batches must contain "
                    "'inputs' and 'targets'."
                )

            return batch["inputs"], batch["targets"]

        if isinstance(batch, (tuple, list)) and len(batch) == 2:
            return batch[0], batch[1]

        raise ValueError(
            "Batch must be (inputs, targets) or a dictionary "
            "containing 'inputs' and 'targets'."
        )

    def _prepare_batch(self, batch):
        inputs, targets = self._unpack_batch(batch)

        if not isinstance(inputs, torch.Tensor):
            raise TypeError("Model inputs must be a torch.Tensor.")

        if not isinstance(targets, torch.Tensor):
            raise TypeError("Targets must be a torch.Tensor.")

        inputs = inputs.to(
            self.device,
            non_blocking=True,
        )

        targets = targets.to(
            self.device,
            dtype=torch.long,
            non_blocking=True,
        )

        return inputs, targets

    @staticmethod
    def _prepare_predictions(logits, targets):
        """
        Normalize image-level and temporal predictions.

        (B, C)   + (B,)   -> (B, C)   + (B,)
        (B,T,C)  + (B,T)  -> (B*T,C) + (B*T,)
        """

        if logits.ndim not in (2, 3):
            raise ValueError(
                f"Expected 2D or 3D logits, got shape {logits.shape}."
            )

        if logits.shape[:-1] != targets.shape:
            raise ValueError(
                f"Logits shape {logits.shape} is incompatible "
                f"with targets shape {targets.shape}."
            )

        if logits.shape[-1] < 2:
            raise ValueError("At least two output classes are required.")

        if targets.numel() == 0:
            raise ValueError("Targets cannot be empty.")

        return (
            logits.reshape(-1, logits.shape[-1]),
            targets.reshape(-1),
        )

    def _run_epoch(
        self,
        model: nn.Module,
        dataloader: DataLoader,
        criterion: nn.Module,
        optimizer: torch.optim.Optimizer | None = None,
    ) -> dict[str, float | int]:

        training = optimizer is not None

        model.train(training)

        total_loss = 0.0
        total_correct = 0
        total_samples = 0

        context = torch.enable_grad if training else torch.no_grad

        with context():
            for batch in dataloader:
                inputs, targets = self._prepare_batch(batch)

                if training:
                    optimizer.zero_grad(set_to_none=True)

                with torch.autocast(
                    device_type=self.device.type,
                    enabled=self.amp,
                ):
                    logits = model(inputs)

                    flat_logits, flat_targets = (
                        self._prepare_predictions(logits, targets)
                    )

                    loss = criterion(flat_logits, flat_targets)

                if loss.ndim != 0:
                    raise ValueError("Criterion must return a scalar loss.")

                if not torch.isfinite(loss):
                    raise FloatingPointError(
                        f"Non-finite loss encountered: {loss.item()}"
                    )

                if training:
                    self.scaler.scale(loss).backward()

                    if self.grad_clip is not None:
                        self.scaler.unscale_(optimizer)

                        nn.utils.clip_grad_norm_(
                            model.parameters(),
                            max_norm=self.grad_clip,
                        )

                    self.scaler.step(optimizer)
                    self.scaler.update()

                predictions = flat_logits.detach().argmax(dim=-1)

                batch_samples = flat_targets.numel()

                total_loss += loss.detach().item() * batch_samples

                total_correct += (
                    predictions == flat_targets
                ).sum().item()

                total_samples += batch_samples

        if total_samples == 0:
            raise ValueError("DataLoader produced no samples.")

        return {
            "loss": total_loss / total_samples,
            "accuracy": total_correct / total_samples,
            "samples": total_samples,
        }

    def train_one_epoch(
        self,
        model: nn.Module,
        dataloader: DataLoader,
        criterion: nn.Module,
        optimizer: torch.optim.Optimizer,
    ) -> dict[str, float | int]:

        model.to(self.device)

        return self._run_epoch(
            model=model,
            dataloader=dataloader,
            criterion=criterion,
            optimizer=optimizer,
        )

    def validate(
        self,
        model: nn.Module,
        dataloader: DataLoader,
        criterion: nn.Module,
    ) -> dict[str, float | int]:

        model.to(self.device)

        return self._run_epoch(
            model=model,
            dataloader=dataloader,
            criterion=criterion,
            optimizer=None,
        )
