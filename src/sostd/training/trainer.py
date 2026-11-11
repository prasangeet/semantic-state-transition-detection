from __future__ import annotations

from pathlib import Path
from typing import Any

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from src.sostd.training.callbacks import (
    CheckpointManager,
    EarlyStopping,
)
from src.sostd.training.engine import TrainingEngine


class Trainer:
    """
    Complete PyTorch training orchestrator.

    Responsibilities:
        - Training and validation epochs
        - Learning-rate scheduling
        - Early stopping
        - Best/latest checkpoint management
        - Training resumption
        - Metric history tracking

    Supported monitoring metrics:
        - val_loss
        - val_accuracy
        - train_loss
        - train_accuracy
    """

    VALID_METRICS = {
        "val_loss",
        "val_accuracy",
        "train_loss",
        "train_accuracy",
    }

    def __init__(
        self,
        model: nn.Module,
        train_loader: DataLoader,
        val_loader: DataLoader,
        criterion: nn.Module,
        optimizer: torch.optim.Optimizer,
        scheduler: Any | None = None,
        device: str | torch.device = "cpu",
        epochs: int = 25,
        checkpoint_dir: str | Path = "checkpoints",
        early_stopping: EarlyStopping | None = None,
        monitor: str = "val_loss",
        mode: str = "min",
        amp: bool = False,
        grad_clip: float | None = None,
        config: dict | None = None,
    ):
        if epochs < 1:
            raise ValueError("epochs must be at least 1.")

        if monitor not in self.VALID_METRICS:
            raise ValueError(
                f"Unsupported monitor: {monitor}. "
                f"Available: {sorted(self.VALID_METRICS)}"
            )

        if mode not in {"min", "max"}:
            raise ValueError("mode must be 'min' or 'max'.")

        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.criterion = criterion
        self.optimizer = optimizer
        self.scheduler = scheduler

        self.epochs = epochs
        self.monitor = monitor
        self.mode = mode
        self.config = config or {}

        self.engine = TrainingEngine(
            device=device,
            amp=amp,
            grad_clip=grad_clip,
        )

        self.model.to(self.engine.device)

        self.early_stopping = early_stopping

        if (
            self.early_stopping is not None
            and self.early_stopping.mode != mode
        ):
            raise ValueError(
                "EarlyStopping mode must match trainer mode."
            )

        self.checkpoints = CheckpointManager(checkpoint_dir)

        self.history: list[dict] = []
        self.start_epoch = 0
        self.best_metric: float | None = None
        self.stopped_early = False

    def _get_monitor_value(
        self,
        train_metrics: dict,
        val_metrics: dict,
    ) -> float:

        prefix, metric_name = self.monitor.split("_", maxsplit=1)

        metrics = (
            train_metrics if prefix == "train" else val_metrics
        )

        value = float(metrics[metric_name])

        if not torch.isfinite(torch.tensor(value)).item():
            raise FloatingPointError(
                f"Monitored metric {self.monitor} is non-finite."
            )

        return value

    def _is_improvement(self, value: float) -> bool:

        if self.best_metric is None:
            return True

        if self.mode == "min":
            return value < self.best_metric

        return value > self.best_metric

    def _step_scheduler(self, monitored_value: float) -> None:

        if self.scheduler is None:
            return

        if isinstance(
            self.scheduler,
            torch.optim.lr_scheduler.ReduceLROnPlateau,
        ):
            self.scheduler.step(monitored_value)
        else:
            self.scheduler.step()

    def _get_training_state(self) -> dict:

        return {
            "user_config": self.config,
            "history": self.history,
            "best_metric": self.best_metric,
            "early_stopping": (
                self.early_stopping.state_dict()
                if self.early_stopping is not None
                else None
            ),
            "monitor": self.monitor,
            "mode": self.mode,
        }

    def _save_checkpoint(
        self,
        epoch: int,
        metric: float,
        best: bool = False,
    ) -> None:

        save_function = (
            self.checkpoints.save_best
            if best
            else self.checkpoints.save_latest
        )

        save_function(
            model=self.model,
            optimizer=self.optimizer,
            scheduler=self.scheduler,
            scaler=self.engine.scaler,
            epoch=epoch,
            metric=metric,
            config=self._get_training_state(),
        )

    def resume(
        self,
        checkpoint_path: str | Path | None = None,
    ) -> int:
        """
        Resume training from a checkpoint.

        Returns:
            Next epoch index to execute.
        """

        path = (
            Path(checkpoint_path)
            if checkpoint_path is not None
            else self.checkpoints.latest_path
        )

        checkpoint = CheckpointManager.load(
            path=path,
            model=self.model,
            optimizer=self.optimizer,
            scheduler=self.scheduler,
            scaler=self.engine.scaler,
            map_location=self.engine.device,
        )

        if checkpoint["epoch"] < 0:
            raise ValueError("Checkpoint epoch cannot be negative.")

        saved_config = checkpoint.get("config") or {}

        if (
            saved_config.get("monitor", self.monitor) != self.monitor
            or saved_config.get("mode", self.mode) != self.mode
        ):
            raise ValueError(
                "Checkpoint monitoring configuration mismatch."
            )

        self.history = saved_config.get("history", [])
        self.best_metric = saved_config.get("best_metric")

        early_stopping_state = saved_config.get("early_stopping")

        if (
            self.early_stopping is not None
            and early_stopping_state is not None
        ):
            self.early_stopping.load_state_dict(
                early_stopping_state
            )

        self.start_epoch = checkpoint["epoch"] + 1

        return self.start_epoch

    def fit(self) -> list[dict]:
        """Execute the complete training lifecycle."""

        if self.start_epoch >= self.epochs or self.stopped_early:
            raise ValueError(
                "Training already completed or stopped early."
            )

        for epoch in range(self.start_epoch, self.epochs):

            train_metrics = self.engine.train_one_epoch(
                model=self.model,
                dataloader=self.train_loader,
                criterion=self.criterion,
                optimizer=self.optimizer,
            )

            val_metrics = self.engine.validate(
                model=self.model,
                dataloader=self.val_loader,
                criterion=self.criterion,
            )

            monitored_value = self._get_monitor_value(
                train_metrics,
                val_metrics,
            )

            self._step_scheduler(monitored_value)

            learning_rate = self.optimizer.param_groups[0]["lr"]

            epoch_record = {
                "epoch": epoch + 1,
                "train_loss": train_metrics["loss"],
                "train_accuracy": train_metrics["accuracy"],
                "val_loss": val_metrics["loss"],
                "val_accuracy": val_metrics["accuracy"],
                "learning_rate": learning_rate,
                "monitored_metric": monitored_value,
            }

            self.history.append(epoch_record)

            improved = self._is_improvement(monitored_value)

            if improved:
                self.best_metric = monitored_value

            # Update the next epoch before saving checkpoint state.
            self.start_epoch = epoch + 1

            should_stop = False

            if self.early_stopping is not None:
                should_stop = self.early_stopping.step(monitored_value)

            if should_stop:
                self.stopped_early = True

            # Save the best checkpoint when the monitored metric improves.
            if improved:
                self._save_checkpoint(
                    epoch=epoch,
                    metric=monitored_value,
                    best=True,
                )

            # Always save the latest checkpoint with updated state.
            self._save_checkpoint(
                epoch=epoch,
                metric=monitored_value,
                best=False,
            )

            print(
                f"Epoch [{epoch + 1}/{self.epochs}] "
                f"Train Loss: {train_metrics['loss']:.4f} | "
                f"Train Acc: {train_metrics['accuracy']:.4f} | "
                f"Val Loss: {val_metrics['loss']:.4f} | "
                f"Val Acc: {val_metrics['accuracy']:.4f} | "
                f"LR: {learning_rate:.6g}"
            )

            if should_stop:
                print(
                    f"Early stopping triggered at epoch "
                    f"{epoch + 1}."
                )
                break

        return self.history
