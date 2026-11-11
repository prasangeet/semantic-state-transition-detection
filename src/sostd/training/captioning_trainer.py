
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from src.sostd.training.captioning_engine import CaptioningEngine
from src.sostd.training.optimizer import OptimizerFactory
from src.sostd.training.scheduler import SchedulerFactory
from src.sostd.training.callbacks import CheckpointManager, EarlyStopping


class CaptioningTrainer:
    """
    Training lifecycle, metrics history, visualization, and checkpoints.

    Supports OSCaR-Lite V3 and V4.

    V3:
        State captioning + transition captioning.

    V4:
        State captioning + transition captioning
        + auxiliary object classification.
    """

    def __init__(
        self,
        engine: CaptioningEngine,
        optimizer: torch.optim.Optimizer,
        scheduler: Any | None = None,
        checkpoint_manager: CheckpointManager | None = None,
        early_stopping: EarlyStopping | None = None,
        config: dict[str, Any] | None = None,
    ) -> None:
        if not isinstance(optimizer, torch.optim.Optimizer):
            raise TypeError("optimizer must be a torch optimizer.")

        if config is not None and not isinstance(config, dict):
            raise TypeError("config must be a dictionary.")

        self.engine = engine
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.checkpoint_manager = checkpoint_manager
        self.early_stopping = early_stopping
        self.config = dict(config or {})

        self.start_epoch = 0
        self.best_metric = float("inf")
        self.history: list[dict[str, Any]] = []
        self.stopped_early = False

        visualization_config = self.config.get("visualization", {})

        if not isinstance(visualization_config, dict):
            raise TypeError(
                "config['visualization'] must be a dictionary."
            )

        self.visualization_enabled = bool(
            visualization_config.get("enabled", True)
        )

        configured_output_dir = visualization_config.get("output_dir")

        if configured_output_dir is not None:
            self.output_dir = Path(configured_output_dir)
        elif checkpoint_manager is not None:
            self.output_dir = Path(checkpoint_manager.directory)
        else:
            self.output_dir = Path("outputs/captioning_training")

        self.plot_every_epoch = bool(
            visualization_config.get("plot_every_epoch", True)
        )

        model_config = self.config.get("model", {})

        if not isinstance(model_config, dict):
            raise TypeError("config['model'] must be a dictionary.")

        self.model_version = str(
            model_config.get(
                "version",
                self.config.get("version", "v3"),
            )
        ).lower()

        if self.model_version not in {"v3", "v4"}:
            raise ValueError(
                f"Unsupported model version: {self.model_version}"
            )

    # ---------------------------------------------------------
    # Configuration helpers
    # ---------------------------------------------------------

    @staticmethod
    def _get_section(
        config: dict[str, Any],
        name: str,
    ) -> dict[str, Any]:
        section = config.get(name, {})

        if not isinstance(section, dict):
            raise TypeError(
                f"config['{name}'] must be a dictionary."
            )

        return section

    @staticmethod
    def _validate_class_weights(
        weights: Any,
    ) -> torch.Tensor | None:
        if weights is None:
            return None

        if not isinstance(
            weights,
            (list, tuple, torch.Tensor),
        ):
            raise TypeError(
                "engine.object_class_weights must be a "
                "list, tuple, or Tensor."
            )

        weights = torch.as_tensor(
            weights,
            dtype=torch.float32,
        )

        if weights.ndim != 1 or weights.numel() == 0:
            raise ValueError(
                "engine.object_class_weights must be a non-empty "
                "one-dimensional sequence."
            )

        if not torch.isfinite(weights).all():
            raise ValueError(
                "engine.object_class_weights contains non-finite values."
            )

        if torch.any(weights < 0):
            raise ValueError(
                "Object class weights cannot be negative."
            )

        if not torch.any(weights > 0):
            raise ValueError(
                "At least one object class weight must be positive."
            )

        return weights

    # ---------------------------------------------------------
    # Construction
    # ---------------------------------------------------------

    @classmethod
    def from_config(
        cls,
        model: nn.Module,
        config: dict[str, Any],
        checkpoint_dir: str | Path | None = None,
    ) -> "CaptioningTrainer":
        """Build the optimizer, scheduler, engine, and callbacks."""

        if not isinstance(config, dict):
            raise TypeError("config must be a dictionary.")

        if not torch.cuda.is_available():
            raise RuntimeError(
                "CUDA is required for training, but is unavailable."
            )

        trainable_parameters = [
            parameter
            for parameter in model.parameters()
            if parameter.requires_grad
        ]

        if not trainable_parameters:
            raise ValueError("Model has no trainable parameters.")

        optimizer_config = cls._get_section(config, "optimizer")
        scheduler_config = cls._get_section(config, "scheduler")
        engine_config = cls._get_section(config, "engine")
        data_config = cls._get_section(config, "data")
        stopping_config = cls._get_section(config, "early_stopping")

        device = str(engine_config.get("device", "cuda"))

        if not device.startswith("cuda"):
            raise ValueError(
                f"CUDA execution is required. Received: {device}"
            )

        # -----------------------------------------------------
        # Optimizer
        # -----------------------------------------------------

        optimizer_kwargs = dict(
            optimizer_config.get(
                "kwargs",
                {"weight_decay": 1e-4},
            )
        )

        if not isinstance(optimizer_kwargs, dict):
            raise TypeError("optimizer.kwargs must be a dictionary.")

        optimizer = OptimizerFactory.create(
            name=optimizer_config.get("name", "adamw"),
            parameters=trainable_parameters,
            lr=float(optimizer_config.get("lr", 1e-4)),
            **optimizer_kwargs,
        )

        # -----------------------------------------------------
        # Scheduler
        # -----------------------------------------------------

        scheduler = None
        scheduler_name = scheduler_config.get("name")

        if scheduler_name:
            scheduler_kwargs = scheduler_config.get("kwargs", {})

            if not isinstance(scheduler_kwargs, dict):
                raise TypeError(
                    "scheduler.kwargs must be a dictionary."
                )

            scheduler = SchedulerFactory.create(
                name=scheduler_name,
                optimizer=optimizer,
                **scheduler_kwargs,
            )

        # -----------------------------------------------------
        # Loss configuration
        # -----------------------------------------------------

        state_weight = float(
            engine_config.get("state_weight", 1.0)
        )

        transition_weight = float(
            engine_config.get("transition_weight", 1.0)
        )

        object_weight = float(
            engine_config.get("object_weight", 0.0)
        )

        loss_weights = {
            "state_weight": state_weight,
            "transition_weight": transition_weight,
            "object_weight": object_weight,
        }

        for name, value in loss_weights.items():
            if not math.isfinite(value) or value < 0:
                raise ValueError(
                    f"engine.{name} must be finite and non-negative."
                )

        if not any(value > 0 for value in loss_weights.values()):
            raise ValueError(
                "At least one configured loss weight must be positive."
            )

        object_class_weights = cls._validate_class_weights(
            engine_config.get("object_class_weights")
        )

        if object_weight > 0 and object_class_weights is None:
            raise ValueError(
                "object_weight is positive, but no object_class_weights "
                "were supplied. V4 object supervision requires the "
                "training vocabulary's class weights."
            )

        # -----------------------------------------------------
        # Training engine
        # -----------------------------------------------------

        engine = CaptioningEngine(
            device=device,
            amp=bool(engine_config.get("amp", True)),
            grad_clip=engine_config.get("grad_clip", 1.0),
            state_weight=state_weight,
            transition_weight=transition_weight,
            object_weight=object_weight,
            object_class_weights=object_class_weights,
            expected_feature_dim=data_config.get(
                "expected_feature_dim"
            ),
            expected_num_tokens=int(
                data_config.get("expected_num_tokens", 257)
            ),
        )

        # -----------------------------------------------------
        # Checkpoint manager
        # -----------------------------------------------------

        manager = (
            CheckpointManager(checkpoint_dir)
            if checkpoint_dir is not None
            else None
        )

        # -----------------------------------------------------
        # Early stopping
        # -----------------------------------------------------

        early_stopping = None

        if stopping_config.get("enabled", False):
            early_stopping = EarlyStopping(
                **{
                    key: value
                    for key, value in stopping_config.items()
                    if key != "enabled"
                }
            )

        return cls(
            engine=engine,
            optimizer=optimizer,
            scheduler=scheduler,
            checkpoint_manager=manager,
            early_stopping=early_stopping,
            config=config,
        )

    # ---------------------------------------------------------
    # Scheduler
    # ---------------------------------------------------------

    def _step_scheduler(
        self,
        validation_loss: float,
    ) -> None:
        if self.scheduler is None:
            return

        if isinstance(
            self.scheduler,
            torch.optim.lr_scheduler.ReduceLROnPlateau,
        ):
            self.scheduler.step(validation_loss)
        else:
            self.scheduler.step()

    # ---------------------------------------------------------
    # Checkpointing
    # ---------------------------------------------------------

    def _get_training_state(self) -> dict[str, Any]:
        return {
            "user_config": self.config,
            "history": self.history,
            "best_metric": self.best_metric,
            "early_stopping": (
                self.early_stopping.state_dict()
                if self.early_stopping is not None
                else None
            ),
            "stopped_early": self.stopped_early,
        }

    def _save_checkpoint(
        self,
        model: nn.Module,
        epoch: int,
        metric: float,
        is_best: bool,
    ) -> None:
        if self.checkpoint_manager is None:
            return

        save_arguments = {
            "model": model,
            "optimizer": self.optimizer,
            "scheduler": self.scheduler,
            "scaler": getattr(self.engine, "scaler", None),
            "epoch": epoch,
            "metric": metric,
            "config": self._get_training_state(),
        }

        self.checkpoint_manager.save_latest(**save_arguments)

        if is_best:
            self.checkpoint_manager.save_best(**save_arguments)

    @staticmethod
    def _validate_checkpoint_metadata(
        checkpoint: dict[str, Any],
    ) -> tuple[int, dict[str, Any]]:
        if not isinstance(checkpoint, dict):
            raise ValueError(
                "Invalid checkpoint: expected a dictionary."
            )

        saved_epoch = checkpoint.get("epoch")

        if (
            not isinstance(saved_epoch, int)
            or isinstance(saved_epoch, bool)
            or saved_epoch < 0
        ):
            raise ValueError(
                "Checkpoint epoch must be a non-negative integer."
            )

        saved_config = checkpoint.get("config")

        if not isinstance(saved_config, dict):
            raise ValueError(
                "Invalid checkpoint training metadata."
            )

        history = saved_config.get("history", [])

        if not isinstance(history, list):
            raise ValueError("Invalid checkpoint history.")

        best_metric = saved_config.get(
            "best_metric",
            checkpoint.get("metric", float("inf")),
        )

        try:
            best_metric = float(best_metric)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "Invalid checkpoint best_metric."
            ) from exc

        if math.isnan(best_metric):
            raise ValueError(
                "Checkpoint best_metric cannot be NaN."
            )

        stopped_early = saved_config.get("stopped_early", False)

        if not isinstance(stopped_early, bool):
            raise ValueError(
                "Invalid early-stop checkpoint state."
            )

        return saved_epoch, saved_config

    def resume(
        self,
        model: nn.Module,
        checkpoint_path: str | Path | None = None,
    ) -> int:
        """Restore model and optimizer state; return the next epoch index."""

        if (
            self.checkpoint_manager is None
            and checkpoint_path is None
        ):
            raise ValueError(
                "A checkpoint manager or explicit checkpoint path "
                "is required for resuming."
            )

        path = (
            Path(checkpoint_path)
            if checkpoint_path is not None
            else self.checkpoint_manager.latest_path
        )

        if not path.is_file():
            raise FileNotFoundError(
                f"Checkpoint not found: {path}"
            )

        device = torch.device(self.engine.device)

        checkpoint = torch.load(
            path,
            map_location=device,
            weights_only=False,
        )

        saved_epoch, saved_config = (
            self._validate_checkpoint_metadata(checkpoint)
        )

        saved_early_stopping = saved_config.get("early_stopping")

        if (
            saved_early_stopping is not None
            and self.early_stopping is None
        ):
            raise ValueError(
                "Checkpoint contains early-stopping state, "
                "but early stopping is disabled."
            )

        if (
            saved_early_stopping is None
            and self.early_stopping is not None
        ):
            raise ValueError(
                "Early stopping is enabled, but checkpoint has no "
                "early-stopping state."
            )

        if saved_early_stopping is not None:
            current_state = self.early_stopping.state_dict()

            for key in ("patience", "min_delta", "mode"):
                if (
                    key in saved_early_stopping
                    and key in current_state
                    and saved_early_stopping[key] != current_state[key]
                ):
                    raise ValueError(
                        "Incompatible early-stopping configuration: "
                        f"{key} differs from checkpoint."
                    )

        model.to(device)

        loaded = CheckpointManager.load(
            path=path,
            model=model,
            optimizer=self.optimizer,
            scheduler=self.scheduler,
            scaler=getattr(self.engine, "scaler", None),
            map_location=device,
        )

        self.history = saved_config.get("history", [])

        self.best_metric = float(
            saved_config.get(
                "best_metric",
                loaded.get("metric", float("inf")),
            )
        )

        self.stopped_early = saved_config.get(
            "stopped_early",
            False,
        )

        if saved_early_stopping is not None:
            self.early_stopping.load_state_dict(
                saved_early_stopping
            )

        self.start_epoch = saved_epoch

        self._save_history()
        self._save_plots()

        return self.start_epoch

    # ---------------------------------------------------------
    # Metrics serialization
    # ---------------------------------------------------------

    @staticmethod
    def _to_json_safe(value: Any) -> Any:
        """Convert nested metric values to JSON-serializable values."""

        if isinstance(value, dict):
            return {
                str(key): CaptioningTrainer._to_json_safe(item)
                for key, item in value.items()
            }

        if isinstance(value, (list, tuple)):
            return [
                CaptioningTrainer._to_json_safe(item)
                for item in value
            ]

        if isinstance(value, torch.Tensor):
            if value.numel() == 1:
                return value.detach().cpu().item()

            return value.detach().cpu().tolist()

        if hasattr(value, "item") and callable(value.item):
            try:
                return value.item()
            except (ValueError, TypeError):
                pass

        if isinstance(value, (str, int, float, bool)) or value is None:
            return value

        return str(value)

    def _save_history(self) -> None:
        """Persist epoch metrics as JSON."""

        if not self.visualization_enabled:
            return

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        history_path = self.output_dir / "training_history.json"
        temporary_path = history_path.with_suffix(".json.tmp")

        with temporary_path.open("w", encoding="utf-8") as file:
            json.dump(
                self._to_json_safe(self.history),
                file,
                indent=2,
                allow_nan=True,
            )

        temporary_path.replace(history_path)

    @staticmethod
    def _metric_values(
        history: list[dict[str, Any]],
        split: str,
        metric: str,
    ) -> list[float]:
        values: list[float] = []

        for item in history:
            metrics = item.get(split, {})

            value = (
                metrics.get(metric)
                if isinstance(metrics, dict)
                else None
            )

            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                numeric_value = float("nan")

            values.append(numeric_value)

        return values

    # ---------------------------------------------------------
    # Plotting
    # ---------------------------------------------------------

    def _save_plots(self) -> None:
        """Save loss, object metric, and learning-rate curves."""

        if not self.visualization_enabled or not self.history:
            return

        try:
            import matplotlib

            matplotlib.use("Agg")

            import matplotlib.pyplot as plt

        except ImportError:
            print(
                "WARNING: matplotlib is unavailable. Metrics are saved "
                "to training_history.json, but plots cannot be generated."
            )
            return

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        epochs = [
            int(item.get("epoch", index + 1))
            for index, item in enumerate(self.history)
        ]

        version_label = self.model_version.upper()

        # -----------------------------------------------------
        # Overall loss
        # -----------------------------------------------------

        train_loss = self._metric_values(
            self.history,
            "train",
            "loss",
        )

        validation_loss = self._metric_values(
            self.history,
            "validation",
            "loss",
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.plot(
            epochs,
            train_loss,
            marker="o",
            label="Training loss",
        )

        ax.plot(
            epochs,
            validation_loss,
            marker="o",
            label="Validation loss",
        )

        ax.set_title(
            f"OSCaR-Lite {version_label} - Training and Validation Loss"
        )
        ax.set_xlabel("Epoch")
        ax.set_ylabel("Loss")
        ax.grid(True, alpha=0.3)
        ax.legend()

        fig.tight_layout()

        fig.savefig(
            self.output_dir / "loss_curves.png",
            dpi=200,
            bbox_inches="tight",
        )

        plt.close(fig)

        # -----------------------------------------------------
        # Component losses
        # -----------------------------------------------------

        component_metrics = [
            ("state_loss", "Validation state loss"),
            ("transition_loss", "Validation transition loss"),
            ("object_loss", "Validation object loss"),
        ]

        available_components = []

        for metric_name, label in component_metrics:
            values = self._metric_values(
                self.history,
                "validation",
                metric_name,
            )

            if any(math.isfinite(value) for value in values):
                available_components.append(
                    (label, values)
                )

        if available_components:
            fig, ax = plt.subplots(figsize=(10, 6))

            for label, values in available_components:
                ax.plot(
                    epochs,
                    values,
                    marker="o",
                    label=label,
                )

            ax.set_title(
                f"OSCaR-Lite {version_label} - Validation Component Losses"
            )
            ax.set_xlabel("Epoch")
            ax.set_ylabel("Loss")
            ax.grid(True, alpha=0.3)
            ax.legend()

            fig.tight_layout()

            fig.savefig(
                self.output_dir / "component_loss_curves.png",
                dpi=200,
                bbox_inches="tight",
            )

            plt.close(fig)

        # -----------------------------------------------------
        # Object classification metrics (V4)
        # -----------------------------------------------------

        object_metrics = [
            ("object_accuracy", "Object accuracy"),
            ("object_macro_f1", "Object macro-F1"),
        ]

        available_object_metrics = []

        for metric_name, label in object_metrics:
            values = self._metric_values(
                self.history,
                "validation",
                metric_name,
            )

            if any(math.isfinite(value) for value in values):
                available_object_metrics.append(
                    (label, values)
                )

        if available_object_metrics:
            fig, ax = plt.subplots(figsize=(10, 6))

            for label, values in available_object_metrics:
                ax.plot(
                    epochs,
                    values,
                    marker="o",
                    label=label,
                )

            ax.set_title(
                f"OSCaR-Lite {version_label} - Object Classification Metrics"
            )
            ax.set_xlabel("Epoch")
            ax.set_ylabel("Score")
            ax.set_ylim(0.0, 1.0)
            ax.grid(True, alpha=0.3)
            ax.legend()

            fig.tight_layout()

            fig.savefig(
                self.output_dir / "object_metrics.png",
                dpi=200,
                bbox_inches="tight",
            )

            plt.close(fig)

        # -----------------------------------------------------
        # Learning rate
        # -----------------------------------------------------

        learning_rates: list[float] = []

        for item in self.history:
            try:
                learning_rates.append(
                    float(item.get("learning_rate"))
                )
            except (TypeError, ValueError):
                learning_rates.append(float("nan"))

        if any(math.isfinite(value) for value in learning_rates):
            fig, ax = plt.subplots(figsize=(10, 5))

            ax.plot(
                epochs,
                learning_rates,
                marker="o",
                label="Learning rate",
            )

            ax.set_title(
                f"OSCaR-Lite {version_label} - Learning Rate Schedule"
            )
            ax.set_xlabel("Epoch")
            ax.set_ylabel("Learning rate")
            ax.grid(True, alpha=0.3)
            ax.legend()

            fig.tight_layout()

            fig.savefig(
                self.output_dir / "learning_rate_curve.png",
                dpi=200,
                bbox_inches="tight",
            )

            plt.close(fig)

    # ---------------------------------------------------------
    # Training
    # ---------------------------------------------------------

    def fit(
        self,
        model: nn.Module,
        train_loader: DataLoader,
        validation_loader: DataLoader,
        epochs: int,
    ) -> list[dict[str, Any]]:
        """Run training, validation, checkpointing, and metric logging.

        Optional V4.2 loss schedule:
            config["loss_schedule"]["disable_object_after_epoch"] = 9

        With this setting, the auxiliary object loss is used for epochs 1-9
        and disabled from epoch 10 onward. Object classification metrics
        continue to be calculated and logged.

        The reported ``loss`` metric is always the weighted captioning
        objective (state + transition). The actual training objective,
        including the auxiliary object term when enabled, is retained as
        ``optimization_loss``. This keeps scheduler, early-stopping, and
        best-checkpoint comparisons consistent across the schedule change.
        """

        if (
            not isinstance(epochs, int)
            or isinstance(epochs, bool)
            or epochs < 1
        ):
            raise ValueError(
                "epochs must be an integer of at least 1."
            )

        if self.stopped_early:
            raise ValueError(
                "Training has already stopped due to early stopping."
            )

        if self.start_epoch >= epochs:
            raise ValueError(
                "Training already completed for the requested epochs."
            )

        loss_schedule = self.config.get("loss_schedule", {})

        if not isinstance(loss_schedule, dict):
            raise TypeError(
                "config['loss_schedule'] must be a dictionary."
            )

        disable_object_after_epoch = loss_schedule.get(
            "disable_object_after_epoch"
        )

        if disable_object_after_epoch is not None:
            if (
                not isinstance(disable_object_after_epoch, int)
                or isinstance(disable_object_after_epoch, bool)
                or disable_object_after_epoch < 1
            ):
                raise ValueError(
                    "loss_schedule.disable_object_after_epoch "
                    "must be a positive integer."
                )

            if self.model_version != "v4":
                raise ValueError(
                    "The auxiliary object-loss schedule is only "
                    "supported for V4."
                )

        device = torch.device(self.engine.device)
        model.to(device)

        for name, parameter in model.named_parameters():
            if parameter.device != device:
                raise RuntimeError(
                    f"Parameter {name} is on {parameter.device}; "
                    f"expected {device}."
                )

        print(f"Training device: {device}")

        if device.type == "cuda":
            print(f"GPU: {torch.cuda.get_device_name(device)}")

        print(f"Model version: {self.model_version.upper()}")
        print(
            "AMP enabled: "
            f"{getattr(self.engine, 'amp', False)}"
        )

        if disable_object_after_epoch is not None:
            print(
                "Object-loss schedule: "
                f"disable after epoch {disable_object_after_epoch}"
            )

        if self.visualization_enabled:
            print(
                f"Training artifacts: {self.output_dir.resolve()}"
            )

        for epoch in range(self.start_epoch, epochs):
            # -------------------------------------------------
            # V4.2 auxiliary object-loss schedule
            # -------------------------------------------------

            if (
                disable_object_after_epoch is not None
                and epoch >= disable_object_after_epoch
                and self.engine.object_weight != 0.0
            ):
                self.engine.object_weight = 0.0
                print(
                    "\nV4.2 schedule: auxiliary object loss disabled "
                    f"at the beginning of epoch {epoch + 1}. "
                    "State and transition losses remain enabled."
                )

            # -------------------------------------------------
            # Training
            # -------------------------------------------------

            train_metrics = self.engine.train_one_epoch(
                model=model,
                dataloader=train_loader,
                optimizer=self.optimizer,
            )

            # -------------------------------------------------
            # Validation
            # -------------------------------------------------

            validation_metrics = self.engine.validate(
                model=model,
                dataloader=validation_loader,
            )

            if not isinstance(train_metrics, dict):
                raise TypeError(
                    "Training engine must return a metrics dictionary."
                )

            if not isinstance(validation_metrics, dict):
                raise TypeError(
                    "Validation engine must return a metrics dictionary."
                )

            required_metrics = (
                "loss",
                "state_loss",
                "transition_loss",
            )

            for split_name, metrics in (
                ("training", train_metrics),
                ("validation", validation_metrics),
            ):
                missing = [
                    name for name in required_metrics
                    if name not in metrics
                ]
                if missing:
                    raise ValueError(
                        f"{split_name.capitalize()} metrics are missing "
                        f"required values: {missing}."
                    )

            # Preserve the actual objective used by the engine. During
            # Stage 1 this includes the auxiliary object-loss term.
            train_optimization_loss = float(train_metrics["loss"])
            validation_engine_loss = float(validation_metrics["loss"])

            if not math.isfinite(train_optimization_loss):
                raise FloatingPointError(
                    f"Non-finite training loss at epoch {epoch + 1}."
                )

            if not math.isfinite(validation_engine_loss):
                raise FloatingPointError(
                    f"Non-finite validation loss at epoch {epoch + 1}."
                )

            # -------------------------------------------------
            # Consistent caption-only objective
            # -------------------------------------------------

            state_weight = float(self.engine.state_weight)
            transition_weight = float(self.engine.transition_weight)

            train_state_loss = float(train_metrics["state_loss"])
            train_transition_loss = float(
                train_metrics["transition_loss"]
            )
            validation_state_loss = float(
                validation_metrics["state_loss"]
            )
            validation_transition_loss = float(
                validation_metrics["transition_loss"]
            )

            component_values = {
                "training state loss": train_state_loss,
                "training transition loss": train_transition_loss,
                "validation state loss": validation_state_loss,
                "validation transition loss": validation_transition_loss,
            }

            for metric_name, metric_value in component_values.items():
                if not math.isfinite(metric_value):
                    raise FloatingPointError(
                        f"Non-finite {metric_name} at epoch {epoch + 1}."
                    )

            train_caption_loss = (
                state_weight * train_state_loss
                + transition_weight * train_transition_loss
            )
            validation_caption_loss = (
                state_weight * validation_state_loss
                + transition_weight * validation_transition_loss
            )

            if (
                not math.isfinite(train_caption_loss)
                or not math.isfinite(validation_caption_loss)
            ):
                raise FloatingPointError(
                    f"Non-finite captioning objective at epoch {epoch + 1}."
                )

            # Keep the raw optimization/engine losses for diagnostics,
            # while making the canonical "loss" comparable at every epoch.
            train_metrics["optimization_loss"] = train_optimization_loss
            train_metrics["loss"] = train_caption_loss

            validation_metrics["loss_with_auxiliary"] = (
                validation_engine_loss
            )
            validation_metrics["loss"] = validation_caption_loss

            train_loss = train_caption_loss
            validation_loss = validation_caption_loss

            # -------------------------------------------------
            # Scheduler and best checkpoint
            # -------------------------------------------------

            # Scheduler, early stopping, and best-checkpoint selection
            # all monitor the same caption-only validation objective.
            self._step_scheduler(validation_loss)

            is_best = validation_loss < self.best_metric

            if is_best:
                self.best_metric = validation_loss

            # -------------------------------------------------
            # History
            # -------------------------------------------------

            epoch_metrics = {
                "epoch": epoch + 1,
                "train": self._to_json_safe(train_metrics),
                "validation": self._to_json_safe(validation_metrics),
                "learning_rate": float(
                    self.optimizer.param_groups[0]["lr"]
                ),
                "best_metric": float(self.best_metric),
                "active_loss_weights": {
                    "state": state_weight,
                    "transition": transition_weight,
                    "object": float(self.engine.object_weight),
                },
            }

            self.history.append(epoch_metrics)
            self.start_epoch = epoch + 1

            # -------------------------------------------------
            # Early stopping
            # -------------------------------------------------

            should_stop = (
                self.early_stopping.step(validation_loss)
                if self.early_stopping is not None
                else False
            )

            if should_stop:
                self.stopped_early = True

            # -------------------------------------------------
            # Persistence
            # -------------------------------------------------

            self._save_checkpoint(
                model=model,
                epoch=epoch + 1,
                metric=validation_loss,
                is_best=is_best,
            )

            self._save_history()

            if self.plot_every_epoch:
                self._save_plots()

            # -------------------------------------------------
            # Epoch summary
            # -------------------------------------------------

            summary = (
                f"Epoch {epoch + 1}/{epochs} | "
                f"Train Caption Loss: {train_loss:.4f} | "
                f"Validation Caption Loss: {validation_loss:.4f} | "
                f"State Loss: {validation_state_loss:.4f} | "
                f"Transition Loss: {validation_transition_loss:.4f}"
            )

            object_loss = float(
                validation_metrics.get("object_loss", float("nan"))
            )

            if math.isfinite(object_loss):
                object_accuracy = float(
                    validation_metrics.get(
                        "object_accuracy",
                        float("nan"),
                    )
                )

                object_macro_f1 = float(
                    validation_metrics.get(
                        "object_macro_f1",
                        float("nan"),
                    )
                )

                summary += (
                    f" | Object Loss: {object_loss:.4f}"
                    f" | Object Acc: {object_accuracy:.4f}"
                    f" | Object Macro-F1: {object_macro_f1:.4f}"
                )

            summary += (
                f" | Object Weight: {self.engine.object_weight:.4f}"
                f" | LR: "
                f"{self.optimizer.param_groups[0]['lr']:.2e}"
            )

            print(summary)

            if should_stop:
                print(
                    f"Early stopping triggered at epoch {epoch + 1}."
                )
                break

        # -----------------------------------------------------
        # Final artifact persistence
        # -----------------------------------------------------

        self._save_history()
        self._save_plots()

        if self.visualization_enabled:
            print("\nTraining artifacts saved:")
            print(
                f"  History: "
                f"{self.output_dir / 'training_history.json'}"
            )
            print(
                f"  Loss curves: "
                f"{self.output_dir / 'loss_curves.png'}"
            )
            print(
                f"  Component losses: "
                f"{self.output_dir / 'component_loss_curves.png'}"
            )
            print(
                f"  Object metrics: "
                f"{self.output_dir / 'object_metrics.png'}"
            )
            print(
                f"  Learning rate: "
                f"{self.output_dir / 'learning_rate_curve.png'}"
            )

        return self.history
