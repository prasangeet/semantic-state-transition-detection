
import pytest

from src.sostd.data.annotation_parser import (
    OSCaRClipAnnotation,
    OSCaRFrameAnnotation,
)
from src.sostd.data.target_encoder import (
    SemanticTransitionTarget,
    TargetEncoder,
)
from src.sostd.data.temporal_sample_builder import TemporalSample


@pytest.fixture
def sample():
    frame_conversations = {
        "Frame_1": (
            {"from": "human", "value": "Describe the state of the drawer."},
            {"from": "gpt", "value": "Drawer partially open."},
        ),
        "Frame_2": (
            {"from": "human", "value": "Describe the state of the drawer."},
            {"from": "gpt", "value": "Drawer further open."},
        ),
        "Frame_3": (
            {"from": "human", "value": "Describe the state of the drawer."},
            {"from": "gpt", "value": "Drawer fully extended."},
        ),
    }

    frame_annotations = {
        key: OSCaRFrameAnnotation(
            clip_id="P01_05_110",
            image_path=f"object-state-data/P01_05_110/{key}.jpg",
            caption_key=key,
            caption_path="",
            qa_path="",
            conversation_path="",
            object_name="drawer",
            action_narration="open drawer",
            conversations=conversation,
        )
        for key, conversation in frame_conversations.items()
    }

    transition_conversation = (
        {
            "from": "human",
            "value": "Describe the state change progression.",
        },
        {
            "from": "gpt",
            "value": "The drawer progressively opens.",
        },
    )

    annotation = OSCaRClipAnnotation(
        clip_id="P01_05_110",
        object_name="drawer",
        action_narration="open drawer",
        frame_annotations=frame_annotations,
        state_descriptions={
            "Frame_1": "Drawer partially open.",
            "Frame_2": "Drawer further open.",
            "Frame_3": "Drawer fully extended.",
        },
        transition_description="The drawer progressively opens.",
        transition_conversation=transition_conversation,
    )

    return TemporalSample(
        annotation=annotation,
        before_frame_idx=23923,
        before_frame_path=(
            "object-state-data/P01_05_110/frame_23923.jpg"
        ),
        during_frames={
            23949: "object-state-data/P01_05_110/frame_23949.jpg",
        },
        after_frame_idx=23976,
        after_frame_path=(
            "object-state-data/P01_05_110/frame_23976.jpg"
        ),
    )


def test_encode_returns_semantic_transition_target(sample):
    target = TargetEncoder.encode(sample)

    assert isinstance(target, SemanticTransitionTarget)


def test_preserves_clip_and_object_information(sample):
    target = TargetEncoder.encode(sample)

    assert target.clip_id == "P01_05_110"
    assert target.object_name == "drawer"


def test_preserves_original_action_narration(sample):
    target = TargetEncoder.encode(sample)

    assert target.action_narration == "open drawer"


def test_preserves_state_descriptions(sample):
    target = TargetEncoder.encode(sample)

    assert target.state_descriptions == (
        ("Frame_1", "Drawer partially open."),
        ("Frame_2", "Drawer further open."),
        ("Frame_3", "Drawer fully extended."),
    )


def test_preserves_transition_description(sample):
    target = TargetEncoder.encode(sample)

    assert target.transition_description == (
        "The drawer progressively opens."
    )


def test_preserves_frame_conversations(sample):
    target = TargetEncoder.encode(sample)

    assert target.frame_conversations == (
        (
            "Frame_1",
            (
                ("human", "Describe the state of the drawer."),
                ("gpt", "Drawer partially open."),
            ),
        ),
        (
            "Frame_2",
            (
                ("human", "Describe the state of the drawer."),
                ("gpt", "Drawer further open."),
            ),
        ),
        (
            "Frame_3",
            (
                ("human", "Describe the state of the drawer."),
                ("gpt", "Drawer fully extended."),
            ),
        ),
    )


def test_preserves_transition_conversation(sample):
    target = TargetEncoder.encode(sample)

    assert target.transition_conversation == (
        ("human", "Describe the state change progression."),
        ("gpt", "The drawer progressively opens."),
    )


def test_conversations_are_immutable_tuples(sample):
    target = TargetEncoder.encode(sample)

    assert isinstance(target.frame_conversations, tuple)
    assert isinstance(target.transition_conversation, tuple)

    for _, conversation in target.frame_conversations:
        assert isinstance(conversation, tuple)
        assert all(isinstance(message, tuple) for message in conversation)


def test_preserves_temporal_frame_indices(sample):
    target = TargetEncoder.encode(sample)

    assert target.before_frame_idx == 23923
    assert target.during_frames == ((23949, sample.during_frames[23949]),)
    assert target.after_frame_idx == 23976


def test_preserves_temporal_frame_paths(sample):
    target = TargetEncoder.encode(sample)

    assert target.before_frame_path == (
        "object-state-data/P01_05_110/frame_23923.jpg"
    )

    assert target.during_frames == (
        (
            23949,
            "object-state-data/P01_05_110/frame_23949.jpg",
        ),
    )

    assert target.after_frame_path == (
        "object-state-data/P01_05_110/frame_23976.jpg"
    )


def test_preserves_multiple_during_frames(sample):
    sample.during_frames[23960] = (
        "object-state-data/P01_05_110/frame_23960.jpg"
    )

    target = TargetEncoder.encode(sample)

    assert target.during_frames == (
        (
            23949,
            "object-state-data/P01_05_110/frame_23949.jpg",
        ),
        (
            23960,
            "object-state-data/P01_05_110/frame_23960.jpg",
        ),
    )


def test_handles_empty_during_frames(sample):
    sample.during_frames.clear()

    target = TargetEncoder.encode(sample)

    assert target.during_frames == ()


def test_handles_empty_semantic_descriptions(sample):
    from dataclasses import replace

    sample.annotation = replace(
        sample.annotation,
        state_descriptions={},
        transition_description="",
    )

    target = TargetEncoder.encode(sample)

    assert target.state_descriptions == ()
    assert target.transition_description == ""


def test_encode_many(sample):
    targets = TargetEncoder.encode_many([sample, sample])

    assert len(targets) == 2
    assert all(
        isinstance(target, SemanticTransitionTarget)
        for target in targets
    )


def test_target_is_immutable(sample):
    target = TargetEncoder.encode(sample)

    with pytest.raises(AttributeError):
        target.before_frame_idx = 100


def test_target_state_descriptions_are_immutable(sample):
    target = TargetEncoder.encode(sample)

    with pytest.raises(AttributeError):
        target.state_descriptions = ()
