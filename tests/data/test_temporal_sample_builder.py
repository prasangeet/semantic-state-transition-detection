
import pytest

from src.sostd.data.annotation_parser import (
    OSCaRAnnotationParser,
)
from src.sostd.data.temporal_sample_builder import (
    TemporalSample,
    TemporalSampleBuilder,
)


@pytest.fixture
def clip_annotation():
    parser = OSCaRAnnotationParser()

    clip_id = "P01_05_110"

    records = []

    for key, frame in [
        ("Frame_1", 23923),
        ("Frame_2", 23949),
        ("Frame_3", 23976),
        ("State_change_caption", None),
    ]:
        filename = (
            "state_change.jpg"
            if frame is None
            else f"frame_{frame}.jpg"
        )

        records.append({
            "image_path": (
                f"object-state-data/{clip_id}/{filename}"
            ),
            "caption_key": key,
            "caption_path": f"state-change-json/{clip_id}.json",
            "qa_path": f"question-answers-clean/{clip_id}.json",
            "conversation_path": (
                f"conversation-clean/{clip_id}.json"
            ),
            "object": "drawer",
            "action_narration": "open drawer",
        })

    frame_annotations = [
        parser.parse_record(record)
        for record in records
    ]

    state_change_json = {
        "Frame_1": "Drawer partially open.",
        "Frame_2": "Drawer further open.",
        "Frame_3": "Drawer fully extended.",
        "State_change_caption": "The drawer progressively opens.",
    }

    return parser.build_clip_annotation(
        frame_annotations,
        state_change_json,
    )


def test_build_sample_returns_temporal_sample(clip_annotation):
    sample = TemporalSampleBuilder.build_sample(clip_annotation)

    assert isinstance(sample, TemporalSample)


def test_build_sample_preserves_clip_annotation(clip_annotation):
    sample = TemporalSampleBuilder.build_sample(clip_annotation)

    assert sample.annotation is clip_annotation


def test_build_sample_preserves_frame_indices(clip_annotation):
    sample = TemporalSampleBuilder.build_sample(clip_annotation)

    assert sample.before_frame_idx == 23923
    assert list(sample.during_frames.keys()) == [23949]
    assert sample.after_frame_idx == 23976


def test_build_sample_preserves_image_paths(clip_annotation):
    sample = TemporalSampleBuilder.build_sample(clip_annotation)

    assert sample.before_frame_path.endswith("frame_23923.jpg")
    assert sample.during_frames[23949].endswith("frame_23949.jpg")
    assert sample.after_frame_path.endswith("frame_23976.jpg")


def test_build_sample_preserves_semantic_annotations(clip_annotation):
    sample = TemporalSampleBuilder.build_sample(clip_annotation)

    assert (
        sample.annotation.state_descriptions["Frame_1"]
        == "Drawer partially open."
    )

    assert (
        sample.annotation.transition_description
        == "The drawer progressively opens."
    )


def test_build_samples(clip_annotation):
    samples = TemporalSampleBuilder.build_samples(
        [clip_annotation, clip_annotation]
    )

    assert len(samples) == 2
    assert all(isinstance(sample, TemporalSample) for sample in samples)


def test_build_sample_rejects_invalid_temporal_order(
    clip_annotation,
):
    clip_annotation.frame_annotations["Frame_2"] = (
        clip_annotation.frame_annotations["Frame_2"].__class__(
            clip_id="P01_05_110",
            image_path=(
                "object-state-data/P01_05_110/frame_23910.jpg"
            ),
            caption_key="Frame_2",
            caption_path="state-change-json/P01_05_110.json",
            qa_path="question-answers-clean/P01_05_110.json",
            conversation_path="conversation-clean/P01_05_110.json",
            object_name="drawer",
            action_narration="open drawer",
        )
    )

    with pytest.raises(ValueError, match="Invalid temporal ordering"):
        TemporalSampleBuilder.build_sample(clip_annotation)
