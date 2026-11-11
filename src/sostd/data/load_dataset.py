
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from datasets import Dataset, DatasetDict, load_dataset
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# Project configuration
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATASET_ROOT = PROJECT_ROOT / "data" / "OSCaR"

DATASET_ID = "ali-vosoughi/oscar-dataset"

DATASET_FILES = {
    "train": "manifests/llava_data.json",
    "validation": "splits/data_mapping_final_EK_test.csv",
    "metadata": "metadata/data_mapping_final.csv",
    "segment_index": "metadata/segment_index.csv",
}


class DatasetLoader:
    """Load OSCaR dataset assets exclusively from the local filesystem."""

    def __init__(
        self,
        dataset_id: str = DATASET_ID,
        streaming: bool = False,
        dataset_root: str | Path | None = None,
    ) -> None:
        if streaming:
            raise ValueError(
                "Streaming is not supported for the local OSCaR dataset."
            )

        self.dataset_id = dataset_id
        self.streaming = False
        self.hf_token: str | None = None

        self.dataset_root = (
            Path(dataset_root).expanduser().resolve()
            if dataset_root is not None
            else DATASET_ROOT
        )

        self.dataset: DatasetDict | None = None
        self.original_annotations: Any | None = None
        self._cache: dict[str, Any] = {}

        self.annotations_root = self.dataset_root / "annotations"
        self.images_root = self.dataset_root / "data"

    # ========================================================
    # Path resolution
    # ========================================================

    def _resolve_dataset_file(self, name: str) -> Path:
        if name not in DATASET_FILES:
            raise ValueError(f"Unknown dataset file: {name}")

        path = self.dataset_root / DATASET_FILES[name]

        if not path.is_file():
            raise FileNotFoundError(
                f"OSCaR dataset file not found: {path}"
            )

        return path

    def _resolve_annotation_file(
        self,
        filename: str,
        annotation_type: str,
    ) -> Path:
        allowed_types = {
            "state-change-json",
            "question-answers-clean",
            "conversation-clean",
        }

        if annotation_type not in allowed_types:
            raise ValueError(
                f"Invalid annotation type: {annotation_type}. "
                f"Choose from {sorted(allowed_types)}."
            )

        if not filename or Path(filename).name != filename:
            raise ValueError("Pass a filename, not a directory path.")

        path = (
            self.annotations_root
            / annotation_type
            / filename
        ).resolve()

        if not path.is_relative_to(
            (self.annotations_root / annotation_type).resolve()
        ):
            raise ValueError("Invalid annotation path.")

        if not path.is_file():
            raise FileNotFoundError(
                f"OSCaR annotation not found: {path}"
            )

        return path

    # ========================================================
    # Dataset loading
    # ========================================================

    def load(self) -> DatasetDict:
        """Load training and validation manifests locally."""

        if self.dataset is not None:
            return self.dataset

        train_path = self._resolve_dataset_file("train")
        validation_path = self._resolve_dataset_file("validation")

        print(f"Loading local OSCaR dataset: {self.dataset_root}")
        print("Loading training manifest...")

        training = load_dataset(
            "json",
            data_files={"train": str(train_path)},
        )

        print("Loading validation split...")

        validation = load_dataset(
            "csv",
            data_files={"validation": str(validation_path)},
        )

        self.dataset = DatasetDict(
            {
                "train": training["train"],
                "validation": validation["validation"],
            }
        )

        print("\nLocal OSCaR dataset loaded successfully!")

        return self.dataset

    # ========================================================
    # Metadata loading
    # ========================================================

    def load_metadata(self) -> Dataset:
        return self._load_csv("metadata")

    def load_segment_index(self) -> Dataset:
        return self._load_csv("segment_index")

    def _load_csv(self, name: str) -> Dataset:
        if name in self._cache:
            return self._cache[name]

        path = self._resolve_dataset_file(name)

        print(f"Loading local OSCaR {name}...")

        dataset = load_dataset(
            "csv",
            data_files=str(path),
            split="train",
        )

        self._cache[name] = dataset

        print(f"Loaded local OSCaR {name}.")

        return dataset

    # ========================================================
    # Original annotation loading
    # ========================================================

    def load_original_annotations(
        self,
        filename: str,
        annotation_type: str = "state-change-json",
    ) -> Any:
        """Load an individual annotation JSON from local storage."""

        path = self._resolve_annotation_file(
            filename,
            annotation_type,
        )

        cache_key = str(path)

        if cache_key in self._cache:
            self.original_annotations = self._cache[cache_key]
            return self.original_annotations

        with path.open("r", encoding="utf-8") as file:
            self.original_annotations = json.load(file)

        self._cache[cache_key] = self.original_annotations

        return self.original_annotations

    # ========================================================
    # Image retrieval
    # ========================================================

    def load_image(self, filename: str) -> str:
        """Resolve an image path inside the local OSCaR image directory."""

        relative_path = Path(filename)

        if (
            not filename
            or relative_path.is_absolute()
            or ".." in relative_path.parts
        ):
            raise ValueError("Invalid image path.")

        # Accept both repository-relative and data/ prefixed paths.
        parts = relative_path.parts

        if parts and parts[0] == "data":
            relative_path = Path(*parts[1:])

        image_path = (self.images_root / relative_path).resolve()

        if not image_path.is_relative_to(self.images_root.resolve()):
            raise ValueError("Invalid image path.")

        if not image_path.is_file():
            raise FileNotFoundError(
                f"OSCaR image not found: {image_path}"
            )

        return str(image_path)

    # ========================================================
    # Dataset inspection
    # ========================================================

    def inspect(self) -> None:
        if self.dataset is None:
            raise RuntimeError("Dataset has not been loaded.")

        print(self.dataset)

        for split, dataset in self.dataset.items():
            print(f"\nSplit: {split}")
            print(f"Number of examples: {len(dataset)}")
            print(f"Features: {dataset.features}")

    # ========================================================
    # Split access
    # ========================================================

    def get_split(self, split: str):
        if self.dataset is None:
            raise RuntimeError("Dataset has not been loaded.")

        if split not in self.dataset:
            raise ValueError(
                f"Split '{split}' not found. "
                f"Available splits: {list(self.dataset.keys())}"
            )

        return self.dataset[split]

    # ========================================================
    # Annotation access
    # ========================================================

    def get_original_annotations(self) -> Any:
        if self.original_annotations is None:
            raise RuntimeError(
                "Original annotations have not been loaded."
            )

        return self.original_annotations
