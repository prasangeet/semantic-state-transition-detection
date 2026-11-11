
from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any


@dataclass(slots=True, frozen=True)
class OSCaRFrameAnnotation:
    """Annotation metadata associated with one OSCaR image."""

    clip_id: str
    image_path: str
    caption_key: str
    caption_path: str
    qa_path: str
    conversation_path: str
    object_name: str
    action_narration: str
    conversations: tuple[dict[str, str], ...] = ()

    @property
    def frame_index(self) -> int | None:
        """Extract the original frame index from the image filename."""

        stem = PurePosixPath(self.image_path).stem

        if not stem.startswith("frame_"):
            return None

        try:
            return int(stem.removeprefix("frame_"))
        except ValueError:
            return None


@dataclass(slots=True, frozen=True)
class OSCaRClipAnnotation:
    """Semantic annotations associated with one OSCaR clip."""

    clip_id: str
    object_name: str
    action_narration: str

    frame_annotations: dict[str, OSCaRFrameAnnotation]

    state_descriptions: dict[str, str | None]
    transition_description: str

    transition_conversation: tuple[dict[str, str], ...] = ()


class OSCaRAnnotationParser:
    """Parse OSCaR training and evaluation annotations."""

    REQUIRED_FIELDS = (
        "image_path",
        "caption_key",
        "caption_path",
        "qa_path",
        "conversation_path",
        "object",
        "action_narration",
    )

    TEMPORAL_KEYS = (
        "Frame_1",
        "Frame_2",
        "Frame_3",
    )

    @staticmethod
    def _required_string(
        record: dict[str, Any],
        field: str,
    ) -> str:
        value = record.get(field)

        if value is None or not str(value).strip():
            raise ValueError(
                f"Missing required OSCaR field: {field}"
            )

        return str(value).strip()

    @staticmethod
    def _validate_image_path(image_path: str) -> PurePosixPath:
        path = PurePosixPath(image_path)

        if path.is_absolute() or ".." in path.parts:
            raise ValueError(
                f"Invalid OSCaR image path: {image_path}"
            )

        if len(path.parts) < 3:
            raise ValueError(
                f"Image path does not contain a clip directory: {image_path}"
            )

        if path.parts[0] != "object-state-data":
            raise ValueError(
                f"Unexpected OSCaR image directory: {image_path}"
            )

        if path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            raise ValueError(
                f"Unsupported image format: {path.suffix}"
            )

        return path

    @staticmethod
    def _parse_conversations(
        conversations: Any,
    ) -> tuple[dict[str, str], ...]:
        """
        Validate and preserve OSCaR conversation messages.

        Empty GPT responses are permitted because some OSCaR records
        contain missing frame-state descriptions.

        Human prompts must remain non-empty, and conversation roles
        must alternate in complete human/GPT pairs.
        """

        if not isinstance(conversations, list) or not conversations:
            raise ValueError(
                "Training conversations must be a non-empty list."
            )

        parsed = []

        for message in conversations:
            if not isinstance(message, dict):
                raise ValueError(
                    "Every conversation message must be a dictionary."
                )

            role = message.get("from")
            value = message.get("value")

            if role not in {"human", "gpt"}:
                raise ValueError(
                    f"Unsupported conversation role: {role}"
                )

            if not isinstance(value, str):
                raise ValueError(
                    "Conversation message values must be strings."
                )

            if role == "human" and not value.strip():
                raise ValueError(
                    "Human conversation prompts must be non-empty."
                )

            parsed.append({
                "from": role,
                "value": value,
            })

        if len(parsed) % 2 != 0:
            raise ValueError(
                "Training conversations must contain complete message pairs."
            )

        for index, message in enumerate(parsed):
            expected_role = "human" if index % 2 == 0 else "gpt"

            if message["from"] != expected_role:
                raise ValueError(
                    "Training conversations must alternate human and gpt messages."
                )

        return tuple(parsed)

    def parse_record(
        self,
        record: dict[str, Any],
    ) -> OSCaRFrameAnnotation:
        """Parse one OSCaR evaluation manifest record."""

        values = {
            field: self._required_string(record, field)
            for field in self.REQUIRED_FIELDS
        }

        image_path = self._validate_image_path(values["image_path"])

        return OSCaRFrameAnnotation(
            clip_id=image_path.parts[-2],
            image_path=values["image_path"],
            caption_key=values["caption_key"],
            caption_path=values["caption_path"],
            qa_path=values["qa_path"],
            conversation_path=values["conversation_path"],
            object_name=values["object"],
            action_narration=values["action_narration"],
        )

    def parse_training_record(
        self,
        record: dict[str, Any],
        metadata: dict[str, Any],
    ) -> OSCaRFrameAnnotation:
        """Parse one training manifest record with its metadata row."""

        image_value = self._required_string(record, "image")
        image_path = self._validate_image_path(image_value)

        metadata_path = self._required_string(metadata, "image_path")

        if image_value != metadata_path:
            raise ValueError(
                "Training record and metadata image paths do not match: "
                f"{image_value} != {metadata_path}"
            )

        values = {
            field: self._required_string(metadata, field)
            for field in (
                "caption_key",
                "caption_path",
                "qa_path",
                "conversation_path",
                "object",
                "action_narration",
            )
        }

        conversations = self._parse_conversations(
            record.get("conversations")
        )

        return OSCaRFrameAnnotation(
            clip_id=image_path.parts[-2],
            image_path=image_value,
            caption_key=values["caption_key"],
            caption_path=values["caption_path"],
            qa_path=values["qa_path"],
            conversation_path=values["conversation_path"],
            object_name=values["object"],
            action_narration=values["action_narration"],
            conversations=conversations,
        )

    def build_clip_annotation(
        self,
        frame_annotations: list[OSCaRFrameAnnotation],
        state_change_json: dict[str, Any],
    ) -> OSCaRClipAnnotation:
        """Combine image records and their shared state-change JSON."""

        if not frame_annotations:
            raise ValueError("Cannot build an empty OSCaR clip.")

        clip_ids = {item.clip_id for item in frame_annotations}
        object_names = {item.object_name for item in frame_annotations}
        actions = {item.action_narration for item in frame_annotations}

        if len(clip_ids) != 1:
            raise ValueError(
                "All frame annotations must belong to the same clip."
            )

        if len(object_names) != 1 or len(actions) != 1:
            raise ValueError(
                "Inconsistent object or action metadata within clip."
            )

        frame_annotations_by_key = {}

        for item in frame_annotations:
            if item.caption_key in frame_annotations_by_key:
                raise ValueError(
                    f"Duplicate caption key: {item.caption_key}"
                )

            frame_annotations_by_key[item.caption_key] = item

        for key in self.TEMPORAL_KEYS:
            if key not in frame_annotations_by_key:
                raise ValueError(
                    f"Missing temporal frame annotation: {key}"
                )

            if key not in state_change_json:
                raise ValueError(
                    f"Missing state description: {key}"
                )

        if "State_change_caption" not in frame_annotations_by_key:
            raise ValueError(
                "Missing State_change_caption manifest record."
            )

        transition_description = state_change_json.get(
            "State_change_caption"
        )

        if not isinstance(transition_description, str):
            raise ValueError(
                "State_change_caption must be a string."
            )

        if not transition_description.strip():
            raise ValueError(
                "State_change_caption cannot be empty."
            )

        state_descriptions: dict[str, str | None] = {}

        for key in self.TEMPORAL_KEYS:
            description = state_change_json[key]

            if description is None:
                state_descriptions[key] = None
            elif isinstance(description, str):
                state_descriptions[key] = description.strip() or None
            else:
                raise ValueError(
                    f"State description for {key} must be a string or None."
                )

        return OSCaRClipAnnotation(
            clip_id=next(iter(clip_ids)),
            object_name=next(iter(object_names)),
            action_narration=next(iter(actions)),
            frame_annotations=frame_annotations_by_key,
            state_descriptions=state_descriptions,
            transition_description=transition_description,
        )

    def build_training_clip_annotation(
        self,
        frame_annotations: list[OSCaRFrameAnnotation],
    ) -> OSCaRClipAnnotation:
        """Build a clip annotation from embedded training conversations."""

        if not frame_annotations:
            raise ValueError("Cannot build an empty OSCaR training clip.")

        clip_ids = {item.clip_id for item in frame_annotations}
        object_names = {item.object_name for item in frame_annotations}
        actions = {item.action_narration for item in frame_annotations}

        if len(clip_ids) != 1:
            raise ValueError(
                "All training annotations must belong to the same clip."
            )

        if len(object_names) != 1 or len(actions) != 1:
            raise ValueError(
                "Inconsistent object or action metadata within training clip."
            )

        by_key = {}

        for item in frame_annotations:
            if item.caption_key in by_key:
                raise ValueError(
                    f"Duplicate training caption key: {item.caption_key}"
                )

            by_key[item.caption_key] = item

        required_keys = (*self.TEMPORAL_KEYS, "State_change_caption")

        for key in required_keys:
            if key not in by_key:
                raise ValueError(
                    f"Missing training annotation: {key}"
                )

        state_descriptions: dict[str, str | None] = {}

        for key in self.TEMPORAL_KEYS:
            conversation = by_key[key].conversations

            if len(conversation) < 2:
                raise ValueError(
                    f"Missing training conversation answer for {key}."
                )

            description = conversation[1]["value"].strip()

            # Preserve the frame and its temporal position, but mark
            # missing state-caption supervision explicitly.
            state_descriptions[key] = description or None

        transition_conversation = by_key[
            "State_change_caption"
        ].conversations

        if len(transition_conversation) < 2:
            raise ValueError(
                "Missing state-change training conversation answer."
            )

        transition_description = (
            transition_conversation[1]["value"].strip()
        )

        # Unlike individual frame captions, the transition caption
        # is mandatory for a valid training clip.
        if not transition_description:
            raise ValueError(
                "State-change training caption cannot be empty."
            )

        return OSCaRClipAnnotation(
            clip_id=next(iter(clip_ids)),
            object_name=next(iter(object_names)),
            action_narration=next(iter(actions)),
            frame_annotations=by_key,
            state_descriptions=state_descriptions,
            transition_description=transition_description,
            transition_conversation=transition_conversation,
        )
