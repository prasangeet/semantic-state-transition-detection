
"""Convert OSCaR annotations into evaluation reference captions.

Supports missing frame-state annotations without fabricating ground truth.
Compatible with the V3 and V4 reference-adaptation interfaces.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Any


class ReferenceAdapter:
    """Adapt OSCaR ground-truth annotations to evaluation format."""

    FRAME_MAPPING = {
        "before": "Frame_1",
        "during": "Frame_2",
        "after": "Frame_3",
    }

    FRAME_NAMES = ("Frame_1", "Frame_2", "Frame_3")

    SECTION_PATTERN = re.compile(
        r"(?m)^[ \t]*(Frame_[123]|State_change_caption)"
        r"[ \t]*:[ \t]*\n?"
    )

    def __init__(self) -> None:
        self.missing_frame_counts: Counter[str] = Counter()
        self.total_samples = 0

    @classmethod
    def _extract_embedded_sections(
        cls,
        text: str,
    ) -> dict[str, str]:
        """Extract non-empty sections from structured annotation text."""

        if not isinstance(text, str):
            return {}

        matches = list(cls.SECTION_PATTERN.finditer(text))
        sections: dict[str, str] = {}

        for index, match in enumerate(matches):
            section_name = match.group(1)
            start = match.end()
            end = (
                matches[index + 1].start()
                if index + 1 < len(matches)
                else len(text)
            )

            content = text[start:end].strip()

            if content:
                sections[section_name] = content

        return sections

    @classmethod
    def _extract_embedded_frame_captions(
        cls,
        transition: str,
    ) -> dict[str, str]:
        """Extract frame captions embedded in transition text."""

        sections = cls._extract_embedded_sections(transition)

        return {
            name: caption
            for name, caption in sections.items()
            if name in cls.FRAME_NAMES
        }

    @classmethod
    def _normalize_transition_reference(
        cls,
        transition: str,
    ) -> str:
        """Extract the transition section from structured annotations."""

        sections = cls._extract_embedded_sections(transition)

        has_frame_sections = any(
            name in sections for name in cls.FRAME_NAMES
        )

        if "State_change_caption" in sections:
            return sections["State_change_caption"]

        if has_frame_sections:
            raise ValueError(
                "Structured transition_description contains frame "
                "sections but no State_change_caption section."
            )

        return transition.strip()

    @staticmethod
    def _normalize_caption(value: Any) -> str | None:
        """Return a valid caption or None when it is unavailable."""

        if not isinstance(value, str):
            return None

        value = value.strip()
        return value if value else None

    def adapt_sample(
        self,
        sample: dict[str, Any],
    ) -> dict[str, str | None]:
        """Convert one sample into three state and one transition reference.

        Missing frame captions are represented by None. They must be
        excluded from that frame's metric calculation downstream.
        """

        if not isinstance(sample, dict):
            raise TypeError("Sample must be a dictionary.")

        state_descriptions = sample.get("state_descriptions")

        if state_descriptions is None:
            state_descriptions = {}

        if not isinstance(state_descriptions, dict):
            raise TypeError(
                "state_descriptions must be a dictionary or None."
            )

        transition = self._normalize_caption(
            sample.get("transition_description")
        )

        if transition is None:
            raise ValueError(
                "Missing or invalid transition_description."
            )

        embedded_captions = self._extract_embedded_frame_captions(
            transition
        )

        references: dict[str, str | None] = {}

        for stage, frame_key in self.FRAME_MAPPING.items():
            caption = self._normalize_caption(
                state_descriptions.get(frame_key)
            )

            if caption is None:
                caption = self._normalize_caption(
                    embedded_captions.get(frame_key)
                )

            references[stage] = caption

            if caption is None:
                self.missing_frame_counts[stage] += 1

        references["transition"] = (
            self._normalize_transition_reference(transition)
        )

        if not references["transition"]:
            raise ValueError(
                "The extracted transition reference is empty."
            )

        self.total_samples += 1

        return references

    def adapt_batch(
        self,
        batch: dict[str, Any],
    ) -> list[dict[str, str | None]]:
        """Convert a collated batch into evaluation references."""

        if not isinstance(batch, dict):
            raise TypeError("Batch must be a dictionary.")

        required = {
            "state_descriptions",
            "transition_description",
        }

        missing = required - batch.keys()

        if missing:
            raise KeyError(
                f"Evaluation batch is missing fields: {sorted(missing)}"
            )

        states = batch["state_descriptions"]
        transitions = batch["transition_description"]

        if not isinstance(states, (list, tuple)):
            raise TypeError(
                "Batch state_descriptions must be a list or tuple."
            )

        if not isinstance(transitions, (list, tuple)):
            raise TypeError(
                "Batch transition_description must be a list or tuple."
            )

        if len(states) != len(transitions):
            raise ValueError(
                "State descriptions and transition descriptions "
                "must have equal lengths. "
                f"Received {len(states)} and {len(transitions)}."
            )

        return [
            self.adapt_sample({
                "state_descriptions": state,
                "transition_description": transition,
            })
            for state, transition in zip(states, transitions)
        ]

    def get_missing_reference_summary(self) -> dict[str, Any]:
        """Return missing-reference counts accumulated during adaptation."""

        return {
            "total_samples": self.total_samples,
            "missing_frame_references": {
                stage: self.missing_frame_counts.get(stage, 0)
                for stage in self.FRAME_MAPPING
            },
            "valid_frame_references": {
                stage: (
                    self.total_samples
                    - self.missing_frame_counts.get(stage, 0)
                )
                for stage in self.FRAME_MAPPING
            },
        }
