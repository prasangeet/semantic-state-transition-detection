
import pytest

from src.sostd.data.annotation_parser import (
    OSCaRAnnotationParser,
    OSCaRFrameAnnotation,
)


@pytest.fixture
def parser():
    return OSCaRAnnotationParser()


@pytest.fixture
def frame_annotations():
    keys = (
        "Frame_1",
        "Frame_2",
        "Frame_3",
        "State_change_caption",
    )

    return [
        OSCaRFrameAnnotation(
            clip_id="P01_001",
            image_path=f"object-state-data/P01_001/frame_{i}.jpg",
            caption_key=key,
            caption_path="captions/example.json",
            qa_path="qa/example.json",
            conversation_path="conversations/example.json",
            object_name="salt",
            action_narration="Sprinkling salt",
        )
        for i, key in enumerate(keys, start=1)
    ]


@pytest.fixture
def valid_state_change():
    return {
        "Frame_1": "Salt is inside the container.",
        "Frame_2": "Salt is being poured.",
        "Frame_3": "Salt is scattered on the surface.",
        "State_change_caption": "Salt is poured from the container.",
    }


def test_missing_state_description_becomes_none(
    parser,
    frame_annotations,
    valid_state_change,
):
    valid_state_change["Frame_2"] = None

    result = parser.build_clip_annotation(
        frame_annotations,
        valid_state_change,
    )

    assert result.state_descriptions == {
        "Frame_1": "Salt is inside the container.",
        "Frame_2": None,
        "Frame_3": "Salt is scattered on the surface.",
    }


def test_empty_state_description_becomes_none(
    parser,
    frame_annotations,
    valid_state_change,
):
    valid_state_change["Frame_1"] = ""
    valid_state_change["Frame_2"] = "   "

    result = parser.build_clip_annotation(
        frame_annotations,
        valid_state_change,
    )

    assert result.state_descriptions["Frame_1"] is None
    assert result.state_descriptions["Frame_2"] is None


def test_valid_state_descriptions_are_stripped(
    parser,
    frame_annotations,
    valid_state_change,
):
    valid_state_change["Frame_1"] = "  Salt is inside the container.  "

    result = parser.build_clip_annotation(
        frame_annotations,
        valid_state_change,
    )

    assert (
        result.state_descriptions["Frame_1"]
        == "Salt is inside the container."
    )


def test_all_missing_state_descriptions_are_allowed(
    parser,
    frame_annotations,
    valid_state_change,
):
    for key in ("Frame_1", "Frame_2", "Frame_3"):
        valid_state_change[key] = None

    result = parser.build_clip_annotation(
        frame_annotations,
        valid_state_change,
    )

    assert result.state_descriptions == {
        "Frame_1": None,
        "Frame_2": None,
        "Frame_3": None,
    }


def test_non_string_state_description_is_rejected(
    parser,
    frame_annotations,
    valid_state_change,
):
    valid_state_change["Frame_2"] = 123

    with pytest.raises(
        ValueError,
        match="State description for Frame_2",
    ):
        parser.build_clip_annotation(
            frame_annotations,
            valid_state_change,
        )


def test_missing_state_key_is_still_rejected(
    parser,
    frame_annotations,
    valid_state_change,
):
    del valid_state_change["Frame_2"]

    with pytest.raises(
        ValueError,
        match="Missing state description: Frame_2",
    ):
        parser.build_clip_annotation(
            frame_annotations,
            valid_state_change,
        )


def test_empty_transition_caption_is_still_rejected(
    parser,
    frame_annotations,
    valid_state_change,
):
    valid_state_change["State_change_caption"] = "   "

    with pytest.raises(
        ValueError,
        match="State_change_caption cannot be empty",
    ):
        parser.build_clip_annotation(
            frame_annotations,
            valid_state_change,
        )
