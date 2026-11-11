from __future__ import annotations

import os
from torch.utils.data import DataLoader

from src.sostd.data.build_dataset import build_temporal_dataset
from src.sostd.data.collate import temporal_collate_fn


def create_temporal_dataloader(
    split: str = "validation",
    batch_size: int = 16,
    shuffle: bool = True,
    num_workers: int = 8,
    pin_memory: bool = True,
    prefetch_factor: int = 2,
) -> tuple[DataLoader, object]:
    """Create a high-performance PyTorch DataLoader for OSCaR temporal samples."""

    if batch_size < 1:
        raise ValueError("batch_size must be at least 1.")

    if num_workers < 0:
        raise ValueError("num_workers cannot be negative.")

    dataset, report = build_temporal_dataset(split=split)

    # Automatically adjust prefetch_factor: PyTorch requires prefetch_factor 
    # to be omitted or None when num_workers=0.
    effective_prefetch = prefetch_factor if num_workers > 0 else None

    dataloader = DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        pin_memory=pin_memory,
        collate_fn=temporal_collate_fn,
        persistent_workers=(num_workers > 0),
        prefetch_factor=effective_prefetch,
    )

    return dataloader, report