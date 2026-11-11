
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Iterable

import torch


IGNORE_INDEX = -100
VOCABULARY_VERSION = 1


class ObjectVocabulary:
    """Training-derived object-label vocabulary for OSCaR."""

    def __init__(
        self,
        class_to_idx: dict[str, int],
        class_counts: dict[str, int],
    ) -> None:
        if not class_to_idx:
            raise ValueError("Object vocabulary cannot be empty.")

        if set(class_to_idx) != set(class_counts):
            raise ValueError(
                "Vocabulary labels and frequency labels must match."
            )

        indices = sorted(class_to_idx.values())

        if indices != list(range(len(indices))):
            raise ValueError(
                "Class indices must be contiguous and start at zero."
            )

        if any(count <= 0 for count in class_counts.values()):
            raise ValueError("Class counts must be positive.")

        self.class_to_idx = dict(class_to_idx)
        self.class_counts = dict(class_counts)

        self.idx_to_class = {
            index: label
            for label, index in self.class_to_idx.items()
        }

    @classmethod
    def from_labels(
        cls,
        labels: Iterable[str],
    ) -> ObjectVocabulary:
        """Build a deterministic vocabulary from training labels."""

        counts: Counter[str] = Counter()

        for label in labels:
            if not isinstance(label, str):
                raise TypeError(
                    f"Object labels must be strings; got {type(label).__name__}."
                )

            label = label.strip()

            if not label:
                raise ValueError("Object labels cannot be empty.")

            counts[label] += 1

        if not counts:
            raise ValueError("Cannot build vocabulary from no labels.")

        classes = sorted(counts)

        return cls(
            class_to_idx={
                label: index
                for index, label in enumerate(classes)
            },
            class_counts=dict(counts),
        )

    @property
    def num_classes(self) -> int:
        return len(self.class_to_idx)

    def encode(self, label: str) -> int:
        """Return IGNORE_INDEX for labels unseen during training."""

        if not isinstance(label, str):
            return IGNORE_INDEX

        return self.class_to_idx.get(label.strip(), IGNORE_INDEX)

    def decode(self, index: int) -> str:
        return self.idx_to_class[index]

    def class_weights(self) -> torch.Tensor:
        """Compute normalized inverse-square-root frequency weights."""

        weights = torch.tensor(
            [
                1.0 / (self.class_counts[label] ** 0.5)
                for label in self.idx_to_class.values()
            ],
            dtype=torch.float32,
        )

        return weights / weights.mean()

    def to_dict(self) -> dict:
        return {
            "version": VOCABULARY_VERSION,
            "class_to_idx": self.class_to_idx,
            "class_counts": self.class_counts,
            "num_classes": self.num_classes,
            "ignore_index": IGNORE_INDEX,
            "weighting": "inverse_sqrt_frequency",
        }

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(
                self.to_dict(),
                file,
                indent=2,
                ensure_ascii=False,
            )

    @classmethod
    def load(cls, path: str | Path) -> ObjectVocabulary:
        path = Path(path)

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if data.get("version") != VOCABULARY_VERSION:
            raise ValueError(
                f"Unsupported vocabulary version: {data.get('version')}"
            )

        vocabulary = cls(
            class_to_idx={
                str(label): int(index)
                for label, index in data["class_to_idx"].items()
            },
            class_counts={
                str(label): int(count)
                for label, count in data["class_counts"].items()
            },
        )

        if data.get("num_classes") != vocabulary.num_classes:
            raise ValueError("Vocabulary class count is inconsistent.")

        return vocabulary
