
from __future__ import annotations

import gc
import tempfile
from pathlib import Path

import torch
from torch.utils.data import DataLoader, Subset
from transformers import AutoTokenizer

from src.sostd.data.build_dataset import build_temporal_dataset
from src.sostd.data.collate import CaptioningCollator
from src.sostd.models.oscar_lite import OSCaRLite
from src.sostd.training.callbacks import CheckpointManager
from src.sostd.training.captioning_engine import CaptioningEngine


def assert_finite_metrics(metrics: dict, name: str) -> None:
    for key in ("loss", "state_loss", "transition_loss"):
        value = metrics.get(key)

        if value is not None and not torch.isfinite(
            torch.tensor(value)
        ):
            raise AssertionError(
                f"{name}: {key} is not finite: {value}"
            )


def create_loader(dataset, collator, name: str):
    if len(dataset) == 0:
        raise RuntimeError(f"{name} dataset is empty.")

    return DataLoader(
        Subset(dataset, [0]),
        batch_size=1,
        shuffle=False,
        collate_fn=collator,
        num_workers=0,
    )


def verify_batch(batch: dict, name: str) -> None:
    required = {
        "frames",
        "state_labels",
        "state_mask",
        "transition_labels",
    }

    missing = required.difference(batch)

    if missing:
        raise AssertionError(
            f"{name}: missing batch keys: {sorted(missing)}"
        )

    frames = batch["frames"]

    assert frames.ndim == 5
    assert frames.shape[:2] == (1, 3)
    assert frames.shape[2] == 3
    assert torch.isfinite(frames).all()

    assert batch["state_labels"].ndim == 3
    assert batch["state_labels"].shape[:2] == (1, 3)

    assert batch["state_mask"].shape == (1, 3)
    assert batch["state_mask"].dtype == torch.bool

    assert batch["transition_labels"].ndim == 2
    assert batch["transition_labels"].shape[0] == 1

    assert (batch["transition_labels"] != -100).any()

    print(f"\n{name} batch verified.")

    for key in required:
        value = batch[key]
        print(f"  {key}: {tuple(value.shape)}")


def create_optimizer(model):
    parameters = [
        parameter
        for parameter in model.parameters()
        if parameter.requires_grad
    ]

    if not parameters:
        raise AssertionError("Model has no trainable parameters.")

    return torch.optim.AdamW(
        parameters,
        lr=1e-4,
        weight_decay=1e-4,
    )


def main() -> None:
    print("=" * 70)
    print("OSCaR-Lite Comprehensive Integration Test")
    print("=" * 70)

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print(f"\nDevice: {device}")

    if device.type == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(device)}")

    # ---------------------------------------------------------
    # 1. Load real training and validation datasets.
    # ---------------------------------------------------------

    print("\n[1/9] Loading real datasets...")

    train_dataset, train_result = build_temporal_dataset(
        split="train"
    )

    validation_dataset, validation_result = build_temporal_dataset(
        split="validation"
    )

    assert len(train_dataset) > 0
    assert len(validation_dataset) > 0

    print(f"Training samples: {len(train_dataset)}")
    print(f"Training clips built: {train_result.clips_built}")

    print(f"Validation samples: {len(validation_dataset)}")
    print(
        f"Validation clips built: "
        f"{validation_result.clips_built}"
    )

    # ---------------------------------------------------------
    # 2. Tokenizer, collator and real batches.
    # ---------------------------------------------------------

    print("\n[2/9] Preparing batches...")

    tokenizer = AutoTokenizer.from_pretrained(
        "google/flan-t5-small"
    )

    collator = CaptioningCollator(
        tokenizer=tokenizer,
        max_state_length=128,
        max_transition_length=128,
    )

    train_loader = create_loader(
        train_dataset,
        collator,
        "Training",
    )

    validation_loader = create_loader(
        validation_dataset,
        collator,
        "Validation",
    )

    train_batch = next(iter(train_loader))
    validation_batch = next(iter(validation_loader))

    verify_batch(train_batch, "Training")
    verify_batch(validation_batch, "Validation")

    # ---------------------------------------------------------
    # 3. Initialize model and optimizer.
    # ---------------------------------------------------------

    print("\n[3/9] Initializing OSCaR-Lite...")

    model = OSCaRLite().to(device)

    total_parameters = sum(
        parameter.numel()
        for parameter in model.parameters()
    )

    trainable_parameters = [
        parameter
        for parameter in model.parameters()
        if parameter.requires_grad
    ]

    trainable_count = sum(
        parameter.numel()
        for parameter in trainable_parameters
    )

    print(f"Total parameters: {total_parameters:,}")
    print(f"Trainable parameters: {trainable_count:,}")
    print(
        f"Trainable percentage: "
        f"{100 * trainable_count / total_parameters:.2f}%"
    )

    optimizer = create_optimizer(model)

    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer,
        T_max=25,
        eta_min=1e-6,
    )

    engine = CaptioningEngine(
        device=device,
        amp=False,
        grad_clip=1.0,
    )

    # ---------------------------------------------------------
    # 4. Verify backward pass and parameter updates.
    # ---------------------------------------------------------

    print("\n[4/9] Testing training and gradients...")

    model.train()

    before_update = {
        name: parameter.detach().clone()
        for name, parameter in model.named_parameters()
        if parameter.requires_grad
    }

    metrics = engine.train_one_epoch(
        model=model,
        dataloader=[train_batch],
        optimizer=optimizer,
    )

    assert_finite_metrics(metrics, "Training")

    gradients_present = 0
    gradients_missing = []

    for name, parameter in model.named_parameters():
        if not parameter.requires_grad:
            continue

        if parameter.grad is None:
            gradients_missing.append(name)
            continue

        if not torch.isfinite(parameter.grad).all():
            raise AssertionError(
                f"Non-finite gradient in {name}"
            )

        gradients_present += 1

    if gradients_missing:
        raise AssertionError(
            f"Missing gradients: {gradients_missing}"
        )

    changed_parameters = 0

    for name, parameter in model.named_parameters():
        if not parameter.requires_grad:
            continue

        if not torch.equal(
            before_update[name],
            parameter.detach(),
        ):
            changed_parameters += 1

    if changed_parameters == 0:
        raise AssertionError(
            "Optimizer did not update any trainable parameters."
        )

    print(f"Training loss: {metrics['loss']:.6f}")
    print(f"State loss: {metrics['state_loss']:.6f}")
    print(f"Transition loss: {metrics['transition_loss']:.6f}")

    print(
        f"Gradient coverage: "
        f"{gradients_present}/{len(trainable_parameters)}"
    )

    print(
        f"Updated parameter tensors: "
        f"{changed_parameters}/{len(trainable_parameters)}"
    )

    # ---------------------------------------------------------
    # 5. Verify validation.
    # ---------------------------------------------------------

    print("\n[5/9] Testing validation...")



    metrics_before_validation = {
        name: parameter.detach().clone()
        for name, parameter in model.named_parameters()
    }


    # Clear gradients left by the training step before testing validation.
    model.zero_grad(set_to_none=True)

    validation_metrics = engine.validate(
        model,
        validation_loader,
    )

    assert_finite_metrics(
        validation_metrics,
        "Validation",
    )

    if any(
        parameter.grad is not None
        for parameter in model.parameters()
    ):
        raise AssertionError(
            "Validation unexpectedly populated gradients."
        )

    for name, parameter in model.named_parameters():
        if not torch.equal(
            metrics_before_validation[name],
            parameter.detach(),
        ):
            raise AssertionError(
                f"Validation modified model parameter: {name}"
            )

    print(
        f"Validation loss: "
        f"{validation_metrics['loss']:.6f}"
    )
    print(
        f"Validation state loss: "
        f"{validation_metrics['state_loss']:.6f}"
    )
    print(
        f"Validation transition loss: "
        f"{validation_metrics['transition_loss']:.6f}"
    )

    # A training update has occurred, so scheduler stepping is valid.
    scheduler.step()

    # ---------------------------------------------------------
    # 6. Save best and latest checkpoints.
    # ---------------------------------------------------------

    print("\n[6/9] Testing checkpoint saving...")

    with tempfile.TemporaryDirectory(
        prefix="oscar_lite_test_"
    ) as temporary_directory:

        checkpoint_manager = CheckpointManager(
            Path(temporary_directory)
        )

        checkpoint_config = {
            "model": {
                "name": "OSCaR-Lite",
                "tokenizer": "google/flan-t5-small",
            },
            "optimizer": {
                "name": "adamw",
                "lr": 1e-4,
            },
            "test": True,
        }

        latest_path = checkpoint_manager.save_latest(
            model=model,
            optimizer=optimizer,
            scheduler=scheduler,
            epoch=1,
            metric=validation_metrics["loss"],
            config=checkpoint_config,
        )

        best_path = checkpoint_manager.save_best(
            model=model,
            optimizer=optimizer,
            scheduler=scheduler,
            epoch=1,
            metric=validation_metrics["loss"],
            config=checkpoint_config,
        )

        assert latest_path.exists()
        assert best_path.exists()

        print(f"Latest checkpoint: {latest_path}")
        print(f"Best checkpoint: {best_path}")

        # -----------------------------------------------------
        # 7. Restore into a fresh model.
        # -----------------------------------------------------

        print("\n[7/9] Testing model checkpoint restoration...")

        expected_parameters = {
            name: parameter.detach().cpu().clone()
            for name, parameter in model.named_parameters()
        }

        expected_scheduler_state = scheduler.state_dict()
        expected_optimizer_state = optimizer.state_dict()

        del metrics_before_validation
        del model
        del optimizer
        del scheduler

        gc.collect()

        if device.type == "cuda":
            torch.cuda.empty_cache()

        restored_model = OSCaRLite().cpu()
        restored_optimizer = create_optimizer(restored_model)

        restored_scheduler = (
            torch.optim.lr_scheduler.CosineAnnealingLR(
                restored_optimizer,
                T_max=25,
                eta_min=1e-6,
            )
        )

        checkpoint = CheckpointManager.load(
            latest_path,
            model=restored_model,
            optimizer=restored_optimizer,
            scheduler=restored_scheduler,
            map_location="cpu",
        )

        assert checkpoint["epoch"] == 1

        for name, parameter in restored_model.named_parameters():
            if not torch.equal(
                expected_parameters[name],
                parameter.detach(),
            ):
                raise AssertionError(
                    f"Checkpoint mismatch in parameter: {name}"
                )

        print("All model parameters restored exactly.")

        # -----------------------------------------------------
        # 8. Verify optimizer and scheduler restoration.
        # -----------------------------------------------------

        print("\n[8/9] Testing optimizer and scheduler restoration...")

        restored_scheduler_state = restored_scheduler.state_dict()

        if (
            restored_scheduler_state
            != expected_scheduler_state
        ):
            raise AssertionError(
                "Scheduler state was not restored correctly."
            )

        if (
            len(restored_optimizer.state)
            != len(expected_optimizer_state["state"])
        ):
            raise AssertionError(
                "Optimizer state was not restored correctly."
            )

        for parameter_id, expected_state in (
            expected_optimizer_state["state"].items()
        ):
            restored_state = restored_optimizer.state.get(
                next(
                    parameter
                    for parameter in restored_optimizer.param_groups[0]["params"]
                    if parameter in restored_optimizer.state
                ),
                None,
            )

            # Verify optimizer state exists for trained parameters.
            if restored_state is None:
                raise AssertionError(
                    "Restored optimizer state is missing."
                )

            break

        print("Optimizer state restored.")
        print("Scheduler state restored.")
        print(f"Checkpoint epoch: {checkpoint['epoch']}")

        # -----------------------------------------------------
        # 9. Final report.
        # -----------------------------------------------------

        print("\n[9/9] Final verification...")

        print("Real training data: PASS")
        print("Real validation data: PASS")
        print("Collation and tokenization: PASS")
        print("Forward and backward passes: PASS")
        print("Gradient coverage: PASS")
        print("Optimizer updates: PASS")
        print("Validation without gradients: PASS")
        print("Best/latest checkpoint saving: PASS")
        print("Model checkpoint restoration: PASS")
        print("Optimizer restoration: PASS")
        print("Scheduler restoration: PASS")

        del restored_model
        del restored_optimizer
        del restored_scheduler

        gc.collect()

        if device.type == "cuda":
            torch.cuda.empty_cache()

    print("\n" + "=" * 70)
    print("ALL INTEGRATION CHECKS PASSED")
    print("OSCaR-Lite is ready for full training.")
    print("=" * 70)


if __name__ == "__main__":
    main()
