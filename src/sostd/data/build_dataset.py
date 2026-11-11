from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from src.sostd.data.annotation_parser import (
    OSCaRAnnotationParser,
    OSCaRClipAnnotation,
)
from src.sostd.data.frame_loader import RGBFrameLoader
from src.sostd.data.load_dataset import DatasetLoader
from src.sostd.data.temporal_dataset import InputMode, TemporalDataset
from src.sostd.data.temporal_sample_builder import (
    TemporalSample,
    TemporalSampleBuilder,
)


@dataclass(slots=True)
class TemporalDatasetBuildResult:
    """Summary of the temporal samples constructed from OSCaR."""

    samples: list[TemporalSample]
    clips_seen: int
    clips_built: int


def _build_validation_annotations(
    dataset_loader: DatasetLoader,
    parser: OSCaRAnnotationParser,
) -> tuple[list[OSCaRClipAnnotation], int]:
    """Build clip annotations from the OSCaR validation manifest."""

    grouped_records: dict[str, list[Any]] = defaultdict(list)

    for record in dataset_loader.get_split("validation"):
        annotation = parser.parse_record(record)
        grouped_records[annotation.clip_id].append(annotation)

    clip_annotations: list[OSCaRClipAnnotation] = []

    for clip_id, frame_annotations in grouped_records.items():
        state_change_json = dataset_loader.load_original_annotations(
            f"{clip_id}.json",
            annotation_type="state-change-json",
        )

        clip_annotation = parser.build_clip_annotation(
            frame_annotations,
            state_change_json,
        )

        clip_annotations.append(clip_annotation)

    return clip_annotations, len(grouped_records)


def _build_training_annotations(
    dataset_loader: DatasetLoader,
    parser: OSCaRAnnotationParser,
) -> tuple[list[OSCaRClipAnnotation], int]:
    """Build clip annotations from the OSCaR training manifest."""

    metadata_by_path: dict[str, Any] = {}

    for metadata in dataset_loader.load_metadata():
        image_path = metadata.get("image_path")

        if not image_path:
            raise ValueError(
                "Training metadata contains a record without image_path."
            )

        if image_path in metadata_by_path:
            raise ValueError(
                f"Duplicate image path in training metadata: {image_path}"
            )

        metadata_by_path[image_path] = metadata

    grouped_records: dict[str, list[Any]] = defaultdict(list)

    for record in dataset_loader.get_split("train"):
        image_path = record.get("image")

        if image_path not in metadata_by_path:
            raise ValueError(
                f"Training metadata not found for image: {image_path}"
            )

        annotation = parser.parse_training_record(
            record,
            metadata_by_path[image_path],
        )

        grouped_records[annotation.clip_id].append(annotation)

    clip_annotations = [
        parser.build_training_clip_annotation(frame_annotations)
        for frame_annotations in grouped_records.values()
    ]

    return clip_annotations, len(grouped_records)


def build_temporal_dataset(
    split: str = "validation",
    feature_dir: str | Path = "data/OSCaR/cached_features",
    expected_feature_dim: int | None = None,
    *,
    input_mode: InputMode = "cached_features",
    frame_loader: Any | None = None,
    transform: Callable | None = None,
    expected_num_tokens: int | None = 257,
    dataset_loader: DatasetLoader | None = None,
) -> tuple[TemporalDataset, TemporalDatasetBuildResult]:
    """Build an OSCaR temporal dataset.

    Supported input modes
    ---------------------
    cached_features:
        Loads precomputed visual features from feature_dir.
        Preserves the existing V1/V2 workflow.

    raw_frames:
        Loads RGB frames directly from disk.
        Intended for online visual encoder execution and fine-tuning,
        including the OSCaR-Lite V3 DINOv2-Large experiment.

    auto:
        Allows TemporalDataset to select the input mode based on the
        available frame loader and dataset configuration.

    Parameters
    ----------
    split:
        Dataset split. Supported values are "train", "validation", and
        the legacy alias "val".

    feature_dir:
        Directory containing precomputed visual features.

    expected_feature_dim:
        Expected feature dimension when loading cached features.

    input_mode:
        Selects raw-frame loading or cached-feature loading.
        Defaults to cached_features for backward compatibility.

    frame_loader:
        Optional injected RGB frame loader.

    transform:
        Optional image transform applied by TemporalDataset in raw-frame
        mode.

    expected_num_tokens:
        Expected number of visual tokens in cached features.

    dataset_loader:
        Optional injected OSCaR dataset loader.

    Returns
    -------
    tuple[TemporalDataset, TemporalDatasetBuildResult]
        The constructed temporal dataset and its build summary.
    """

    # Normalize legacy split names.
    if split == "val":
        split = "validation"

    if split not in {"train", "validation"}:
        raise ValueError(
            "Unsupported split. Choose 'train' or 'validation'."
        )

    if input_mode not in {
        "raw_frames",
        "cached_features",
        "auto",
    }:
        raise ValueError(
            f"Unsupported input_mode: {input_mode!r}."
        )

    # Initialize the dataset loader.
    loader = (
        dataset_loader
        if dataset_loader is not None
        else DatasetLoader()
    )

    loader.load()

    # Parse annotations and construct temporal samples.
    parser = OSCaRAnnotationParser()

    if split == "train":
        clip_annotations, clips_seen = _build_training_annotations(
            loader,
            parser,
        )
    else:
        clip_annotations, clips_seen = _build_validation_annotations(
            loader,
            parser,
        )

    samples = TemporalSampleBuilder.build_samples(
        clip_annotations
    )

    # Initialize the RGB frame loader.
    #
    # The default loader inherits the authentication token from the
    # dataset loader. This preserves compatibility with the local
    # OSCaR dataset-loading workflow.
    rgb_loader = (
        frame_loader
        if frame_loader is not None
        else RGBFrameLoader(token=loader.hf_token)
    )

    # Construct the temporal dataset.
    temporal_dataset = TemporalDataset(
        samples=samples,
        split_name=split,
        feature_dir=feature_dir,
        frame_loader=rgb_loader,
        transform=transform,
        expected_feature_dim=expected_feature_dim,
        expected_num_tokens=expected_num_tokens,
        input_mode=input_mode,
    )

    # Build dataset summary.
    result = TemporalDatasetBuildResult(
        samples=samples,
        clips_seen=clips_seen,
        clips_built=len(samples),
    )

    return temporal_dataset, result