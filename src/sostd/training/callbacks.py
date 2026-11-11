from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import torch
import torch.nn as nn


class CheckpointManager:
    """Manage model checkpoints and training-state persistence."""

    def __init__(self, directory: str | Path):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)

        self.best_path = self.directory / "best.pt"
        self.latest_path = self.directory / "latest.pt"

    def _build_state(
        self,
        model: nn.Module,
        optimizer: torch.optim.Optimizer | None,
        scheduler: Any | None,
        epoch: int,
        metric: float | None,
        config: dict | None,
        scaler: Any | None,
    ) -> dict:

        return {
            "epoch": epoch,
            "metric": metric,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": (
                optimizer.state_dict() if optimizer else None
            ),
            "scheduler_state_dict": (
                scheduler.state_dict() if scheduler else None
            ),
            "scaler_state_dict": (
                scaler.state_dict() if scaler else None
            ),
            "config": config or {},
        }

    def _save_atomic(
        self,
        state: dict,
        path: Path,
    ) -> None:
        """Save checkpoint atomically to avoid corrupted partial files."""

        temporary_path = path.with_suffix(path.suffix + ".tmp")

        try:
            torch.save(state, temporary_path)
            os.replace(temporary_path, path)
        finally:
            if temporary_path.exists():
                temporary_path.unlink()

    def save_best(
        self,
        model: nn.Module,
        optimizer: torch.optim.Optimizer | None = None,
        scheduler: Any | None = None,
        epoch: int = 0,
        metric: float | None = None,
        config: dict | None = None,
        scaler: Any | None = None,
    ) -> Path:

        state = self._build_state(
            model, optimizer, scheduler,
            epoch, metric, config, scaler,
        )

        self._save_atomic(state, self.best_path)

        return self.best_path

    def save_latest(
        self,
        model: nn.Module,
        optimizer: torch.optim.Optimizer | None = None,
        scheduler: Any | None = None,
        epoch: int = 0,
        metric: float | None = None,
        config: dict | None = None,
        scaler: Any | None = None,
    ) -> Path:

        state = self._build_state(
            model, optimizer, scheduler,
            epoch, metric, config, scaler,
        )

        self._save_atomic(state, self.latest_path)

        return self.latest_path

    @staticmethod
    def load(
        path: str | Path,
        model: nn.Module,
        optimizer: torch.optim.Optimizer | None = None,
        scheduler: Any | None = None,
        scaler: Any | None = None,
        map_location: str | torch.device = "cpu",
        strict: bool = True,
    ) -> dict:
        """
        Restore model and optional training state.

        Only load checkpoints from trusted sources because
        weights_only=False permits Python object deserialization.
        """

        path = Path(path)

        if not path.is_file():
            raise FileNotFoundError(
                f"Checkpoint not found: {path}"
            )

        checkpoint = torch.load(
            path,
            map_location=map_location,
            weights_only=False,
        )

        required_keys = {"model_state_dict", "epoch"}

        if not isinstance(checkpoint, dict) or not required_keys.issubset(checkpoint):
            raise ValueError("Invalid checkpoint format.")

        model.load_state_dict(
            checkpoint["model_state_dict"],
            strict=strict,
        )

        if optimizer is not None:
            state = checkpoint.get("optimizer_state_dict")

            if state is not None:
                optimizer.load_state_dict(state)

        if scheduler is not None:
            state = checkpoint.get("scheduler_state_dict")

            if state is not None:
                scheduler.load_state_dict(state)

        if scaler is not None:
            state = checkpoint.get("scaler_state_dict")

            if state is not None:
                scaler.load_state_dict(state)

        return checkpoint


class EarlyStopping:
    """Stop training when a monitored metric stops improving."""

    def __init__(
        self,
        patience: int = 5,
        min_delta: float = 0.0,
        mode: str = "min",
    ):
        if patience < 1:
            raise ValueError("patience must be at least 1.")

        if min_delta < 0:
            raise ValueError("min_delta cannot be negative.")

        if mode not in {"min", "max"}:
            raise ValueError("mode must be 'min' or 'max'.")

        self.patience = patience
        self.min_delta = min_delta
        self.mode = mode

        self.best_score: float | None = None
        self.counter = 0
        self.early_stop = False

    def step(self, metric: float) -> bool:
        """Update monitored metric and return whether training should stop."""

        if self.early_stop:
            return True

        if not torch.isfinite(torch.tensor(metric)).item():
            self.counter += 1
        else:
            improved = (
                self.best_score is None
                or (
                    metric < self.best_score - self.min_delta
                    if self.mode == "min"
                    else metric > self.best_score + self.min_delta
                )
            )

            if improved:
                self.best_score = float(metric)
                self.counter = 0
            else:
                self.counter += 1

        if self.counter >= self.patience:
            self.early_stop = True

        return self.early_stop

    def state_dict(self) -> dict:
        return {
            "patience": self.patience,
            "min_delta": self.min_delta,
            "mode": self.mode,
            "best_score": self.best_score,
            "counter": self.counter,
            "early_stop": self.early_stop,
        }

    def load_state_dict(self, state: dict) -> None:
        if state["mode"] != self.mode:
            raise ValueError("Early stopping mode mismatch.")

        if state["patience"] != self.patience:
            raise ValueError("Early stopping patience mismatch.")

        if state["min_delta"] != self.min_delta:
            raise ValueError("Early stopping min_delta mismatch.")

        self.best_score = state["best_score"]
        self.counter = state["counter"]
        self.early_stop = state["early_stop"]
