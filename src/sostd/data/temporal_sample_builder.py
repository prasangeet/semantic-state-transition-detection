
from __future__ import annotations

from dataclasses import dataclass

from src.sostd.data.annotation_parser import OSCaRClipAnnotation


@dataclass(slots=True)
class TemporalSample:
    """RGB frame references associated with one OSCaR transition."""

    annotation: OSCaRClipAnnotation

    before_frame_idx: int
    before_frame_path: str

    during_frames: dict[int, str]

    after_frame_idx: int
    after_frame_path: str


class TemporalSampleBuilder:
    """Build temporal RGB samples from OSCaR clip annotations."""

    @staticmethod
    def _get_frame_index(
        annotation: OSCaRClipAnnotation,
        key: str,
    ) -> int:
        frame_annotation = annotation.frame_annotations[key]
        frame_index = frame_annotation.frame_index

        if frame_index is None:
            raise ValueError(
                f"Could not extract frame index for {key} "
                f"in clip '{annotation.clip_id}'."
            )

        return frame_index

    @classmethod
    def build_sample(
        cls,
        annotation: OSCaRClipAnnotation,
    ) -> TemporalSample:
        """Build one temporal sample from an OSCaR clip."""

        required_keys = (
            "Frame_1",
            "Frame_2",
            "Frame_3",
        )

        for key in required_keys:
            if key not in annotation.frame_annotations:
                raise ValueError(
                    f"Missing {key} for clip '{annotation.clip_id}'."
                )

        before = annotation.frame_annotations["Frame_1"]
        during = annotation.frame_annotations["Frame_2"]
        after = annotation.frame_annotations["Frame_3"]

        before_idx = cls._get_frame_index(annotation, "Frame_1")
        during_idx = cls._get_frame_index(annotation, "Frame_2")
        after_idx = cls._get_frame_index(annotation, "Frame_3")

        if not before_idx < during_idx < after_idx:
            raise ValueError(
                f"Invalid temporal ordering in clip "
                f"'{annotation.clip_id}': "
                f"{before_idx}, {during_idx}, {after_idx}."
            )

        return TemporalSample(
            annotation=annotation,
            before_frame_idx=before_idx,
            before_frame_path=before.image_path,
            during_frames={
                during_idx: during.image_path,
            },
            after_frame_idx=after_idx,
            after_frame_path=after.image_path,
        )

    @classmethod
    def build_samples(
        cls,
        annotations: list[OSCaRClipAnnotation],
    ) -> list[TemporalSample]:
        """Build temporal samples for multiple OSCaR clips."""

        return [
            cls.build_sample(annotation)
            for annotation in annotations
        ]
