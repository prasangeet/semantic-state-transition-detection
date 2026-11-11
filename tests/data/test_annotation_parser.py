
import pytest

from src.sostd.data.annotation_parser import (
    OSCaRAnnotationParser,
    OSCaRFrameAnnotation,
)


@pytest.fixture
def parser():
    return OSCaRAnnotationParser()


@pytest.fixture
def frame_records():
    clip_id = "P01_05_110"

    records = []

    for key, frame in [
        ("Frame_1", 23923),
        ("Frame_2", 23949),
        ("Frame_3", 23976),
        ("State_change_caption", None),
    ]:
        filename = (
            f"state_change.jpg"
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

    return records


@pytest.fixture
def state_change_json():
    return {
        "Frame_1": "Drawer partially open.",
        "Frame_2": "Drawer further open.",
        "Frame_3": "Drawer fully extended.",
        "State_change_caption": (
            "The drawer progressively opens."
        ),
    }


def test_parse_record(parser, frame_records):
    annotation = parser.parse_record(frame_records[0])

    assert isinstance(annotation, OSCaRFrameAnnotation)
    assert annotation.clip_id == "P01_05_110"
    assert annotation.object_name == "drawer"
    assert annotation.action_narration == "open drawer"
    assert annotation.caption_key == "Frame_1"


def test_parse_record_extracts_frame_index(parser, frame_records):
    annotation = parser.parse_record(frame_records[0])

    assert annotation.frame_index == 23923


def test_parse_record_state_change_has_no_frame_index(
    parser,
    frame_records,
):
    annotation = parser.parse_record(frame_records[3])

    assert annotation.frame_index is None


@pytest.mark.parametrize(
    "field",
    [
        "image_path",
        "caption_key",
        "caption_path",
        "qa_path",
        "conversation_path",
        "object",
        "action_narration",
    ],
)
def test_parse_record_rejects_missing_fields(
    parser,
    frame_records,
    field,
):
    record = frame_records[0].copy()
    record[field] = ""

    with pytest.raises(ValueError, match="Missing required"):
        parser.parse_record(record)


def test_parse_record_rejects_invalid_image_directory(
    parser,
    frame_records,
):
    record = frame_records[0].copy()
    record["image_path"] = "unexpected/P01_05_110/frame_23923.jpg"

    with pytest.raises(ValueError, match="Unexpected OSCaR image directory"):
        parser.parse_record(record)


def test_parse_record_rejects_unsupported_image_format(
    parser,
    frame_records,
):
    record = frame_records[0].copy()
    record["image_path"] = (
        "object-state-data/P01_05_110/frame_23923.gif"
    )

    with pytest.raises(ValueError, match="Unsupported image format"):
        parser.parse_record(record)


def test_build_clip_annotation(
    parser,
    frame_records,
    state_change_json,
):
    annotations = [
        parser.parse_record(record)
        for record in frame_records
    ]

    clip = parser.build_clip_annotation(
        annotations,
        state_change_json,
    )

    assert clip.clip_id == "P01_05_110"
    assert clip.object_name == "drawer"
    assert clip.action_narration == "open drawer"

    assert set(clip.frame_annotations) == {
        "Frame_1",
        "Frame_2",
        "Frame_3",
        "State_change_caption",
    }

    assert clip.state_descriptions["Frame_1"] == (
        "Drawer partially open."
    )

    assert clip.state_descriptions["Frame_3"] == (
        "Drawer fully extended."
    )

    assert clip.transition_description == (
        "The drawer progressively opens."
    )


def test_build_clip_rejects_missing_temporal_frame(
    parser,
    frame_records,
    state_change_json,
):
    annotations = [
        parser.parse_record(record)
        for record in frame_records
        if record["caption_key"] != "Frame_2"
    ]

    with pytest.raises(ValueError, match="Missing temporal frame"):
        parser.build_clip_annotation(
            annotations,
            state_change_json,
        )


def test_build_clip_rejects_different_clips(
    parser,
    frame_records,
    state_change_json,
):
    annotations = [
        parser.parse_record(record)
        for record in frame_records
    ]

    annotations[1] = OSCaRFrameAnnotation(
        clip_id="different_clip",
        image_path=annotations[1].image_path,
        caption_key=annotations[1].caption_key,
        caption_path=annotations[1].caption_path,
        qa_path=annotations[1].qa_path,
        conversation_path=annotations[1].conversation_path,
        object_name=annotations[1].object_name,
        action_narration=annotations[1].action_narration,
    )

    with pytest.raises(ValueError, match="same clip"):
        parser.build_clip_annotation(
            annotations,
            state_change_json,
        )


@pytest.fixture
def training_records():
    clip_id = "P01_109_402"

    records = []

    examples = [
        (
            "frame_70172.jpg",
            "Frame_1",
            "The salt is falling from the jar.",
        ),
        (
            "frame_70190.jpg",
            "Frame_2",
            "The salt is falling more densely.",
        ),
        (
            "frame_70209.jpg",
            "Frame_3",
            "The salt has landed on the eggs.",
        ),
        (
            "state_change.jpg",
            "State_change_caption",
            "The salt transitions from falling to settled.",
        ),
    ]

    for filename, caption_key, description in examples:
        image_path = (
            f"object-state-data/{clip_id}/{filename}"
        )

        records.append({
            "record": {
                "image": image_path,
                "conversations": [
                    {
                        "from": "human",
                        "value": "<image>\nDescribe state of salt",
                    },
                    {
                        "from": "gpt",
                        "value": description,
                    },
                    {
                        "from": "human",
                        "value": "What is happening?",
                    },
                    {
                        "from": "gpt",
                        "value": "Salt is being sprinkled.",
                    },
                ],
            },
            "metadata": {
                "image_path": image_path,
                "caption_key": caption_key,
                "caption_path": (
                    f"state-change-json/{clip_id}.json"
                ),
                "qa_path": (
                    f"question-answers-clean/{clip_id}.json"
                ),
                "conversation_path": (
                    f"conversation-clean/{clip_id}.json"
                ),
                "object": "salt",
                "action_narration": "sprinkle salt",
            },
        })

    return records


def test_parse_training_record(
    parser,
    training_records,
):
    item = training_records[0]

    annotation = parser.parse_training_record(
        item["record"],
        item["metadata"],
    )

    assert annotation.clip_id == "P01_109_402"
    assert annotation.caption_key == "Frame_1"
    assert annotation.object_name == "salt"
    assert annotation.action_narration == "sprinkle salt"
    assert annotation.frame_index == 70172
    assert len(annotation.conversations) == 4
    assert annotation.conversations[1]["value"] == (
        "The salt is falling from the jar."
    )


def test_parse_training_record_rejects_mismatched_paths(
    parser,
    training_records,
):
    item = training_records[0]
    metadata = item["metadata"].copy()
    metadata["image_path"] = (
        "object-state-data/another_clip/frame_70172.jpg"
    )

    with pytest.raises(ValueError, match="do not match"):
        parser.parse_training_record(
            item["record"],
            metadata,
        )


def test_parse_training_record_rejects_invalid_conversations(
    parser,
    training_records,
):
    item = training_records[0]
    record = item["record"].copy()
    record["conversations"] = [
        {"from": "human", "value": "Describe the image"},
    ]

    with pytest.raises(ValueError, match="complete message pairs"):
        parser.parse_training_record(
            record,
            item["metadata"],
        )


def test_build_training_clip_annotation(
    parser,
    training_records,
):
    annotations = [
        parser.parse_training_record(
            item["record"],
            item["metadata"],
        )
        for item in training_records
    ]

    clip = parser.build_training_clip_annotation(
        annotations
    )

    assert clip.clip_id == "P01_109_402"
    assert clip.object_name == "salt"
    assert clip.action_narration == "sprinkle salt"

    assert set(clip.frame_annotations) == {
        "Frame_1",
        "Frame_2",
        "Frame_3",
        "State_change_caption",
    }

    assert clip.state_descriptions["Frame_1"] == (
        "The salt is falling from the jar."
    )

    assert clip.state_descriptions["Frame_3"] == (
        "The salt has landed on the eggs."
    )

    assert clip.transition_description == (
        "The salt transitions from falling to settled."
    )

    assert len(
        clip.frame_annotations["Frame_1"].conversations
    ) == 4

    assert len(clip.transition_conversation) == 4
