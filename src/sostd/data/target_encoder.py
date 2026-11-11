
from __future__ import annotations

from dataclasses import dataclass

from src.sostd.data.temporal_sample_builder import TemporalSample


Conversation = tuple[tuple[str, str], ...]


@dataclass(slots=True, frozen=True)
class SemanticTransitionTarget:
    """Semantic and temporal supervision for one OSCaR sample."""

    clip_id: str
    object_name: str
    action_narration: str

    # None represents a missing frame-state annotation.
    state_descriptions: tuple[tuple[str, str | None], ...]
    transition_description: str

    # Original conversational supervision.
    frame_conversations: tuple[tuple[str, Conversation], ...]
    transition_conversation: Conversation

    # Temporal frame information.
    before_frame_idx: int
    before_frame_path: str

    during_frames: tuple[tuple[int, str], ...]

    after_frame_idx: int
    after_frame_path: str


class TargetEncoder:
    """Encode OSCaR temporal samples into semantic supervision targets."""

    @staticmethod
    def _freeze_conversation(
        messages: tuple[dict[str, str], ...],
    ) -> Conversation:
        """Convert conversation messages into immutable pairs."""

        return tuple(
            (message["from"], message["value"])
            for message in messages
        )

    @classmethod
    def encode(
        cls,
        sample: TemporalSample,
    ) -> SemanticTransitionTarget:
        """Encode one temporal sample."""

        annotation = sample.annotation

        frame_conversations = tuple(
            (
                frame_key,
                cls._freeze_conversation(
                    annotation.frame_annotations[frame_key].conversations
                ),
            )
            for frame_key in ("Frame_1", "Frame_2", "Frame_3")
            if frame_key in annotation.frame_annotations
        )

        return SemanticTransitionTarget(
            clip_id=annotation.clip_id,
            object_name=annotation.object_name,
            action_narration=annotation.action_narration,
            state_descriptions=tuple(
                annotation.state_descriptions.items()
            ),
            transition_description=annotation.transition_description,
            frame_conversations=frame_conversations,
            transition_conversation=cls._freeze_conversation(
                annotation.transition_conversation
            ),
            before_frame_idx=sample.before_frame_idx,
            before_frame_path=sample.before_frame_path,
            during_frames=tuple(sample.during_frames.items()),
            after_frame_idx=sample.after_frame_idx,
            after_frame_path=sample.after_frame_path,
        )

    @classmethod
    def encode_many(
        cls,
        samples: list[TemporalSample],
    ) -> list[SemanticTransitionTarget]:
        """Encode multiple temporal samples."""

        return [cls.encode(sample) for sample in samples]
