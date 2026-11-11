
from src.sostd.data.annotation_parser import OSCaRClipAnnotation
from src.sostd.data.label_analyzer import AnnotationLabelAnalyzer


def make_annotation(
    object_name: str = "drawer",
    action_narration: str = "open drawer",
    state_descriptions: dict[str, str] | None = None,
    transition_description: str = "The drawer progressively opens.",
) -> OSCaRClipAnnotation:
    return OSCaRClipAnnotation(
        clip_id="P01_05_110",
        object_name=object_name,
        action_narration=action_narration,
        frame_annotations={},
        state_descriptions=(
            state_descriptions
            if state_descriptions is not None
            else {
                "Frame_1": "Drawer partially open.",
                "Frame_2": "Drawer further open.",
                "Frame_3": "Drawer fully extended.",
            }
        ),
        transition_description=transition_description,
    )


def test_analyze_total_annotations():
    annotations = [
        make_annotation(object_name="drawer"),
        make_annotation(object_name="cabinet"),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.total_annotations == 2


def test_counts_object_names():
    annotations = [
        make_annotation(object_name="drawer"),
        make_annotation(object_name="drawer"),
        make_annotation(object_name="cabinet"),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.object_names == {
        "drawer": 2,
        "cabinet": 1,
    }


def test_preserves_original_action_narrations():
    annotations = [
        make_annotation(action_narration="peel the onion"),
        make_annotation(action_narration="cut the onion"),
        make_annotation(action_narration="peel the onion"),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.action_narrations == {
        "peel the onion": 2,
        "cut the onion": 1,
    }


def test_counts_individual_action_terms():
    annotations = [
        make_annotation(action_narration="open drawer"),
        make_annotation(action_narration="close drawer"),
        make_annotation(action_narration="open cabinet"),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.action_terms == {
        "open": 2,
        "drawer": 2,
        "close": 1,
        "cabinet": 1,
    }


def test_counts_action_combinations():
    annotations = [
        make_annotation(action_narration="open drawer"),
        make_annotation(action_narration="open drawer"),
        make_annotation(action_narration="close drawer"),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.action_combinations == {
        ("open", "drawer"): 2,
        ("close", "drawer"): 1,
    }


def test_counts_state_descriptions():
    annotations = [
        make_annotation(
            state_descriptions={
                "Frame_1": "Drawer partially open.",
                "Frame_2": "Drawer fully open.",
            }
        ),
        make_annotation(
            state_descriptions={
                "Frame_1": "Drawer partially open.",
                "Frame_2": "Drawer closed.",
            }
        ),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.state_descriptions == {
        "Drawer partially open.": 2,
        "Drawer fully open.": 1,
        "Drawer closed.": 1,
    }


def test_counts_transition_descriptions():
    annotations = [
        make_annotation(
            transition_description="The drawer progressively opens."
        ),
        make_annotation(
            transition_description="The drawer progressively opens."
        ),
        make_annotation(
            transition_description="The drawer closes."
        ),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.transition_descriptions == {
        "The drawer progressively opens.": 2,
        "The drawer closes.": 1,
    }


def test_handles_empty_annotations():
    annotations = [
        make_annotation(
            object_name="",
            action_narration="",
            state_descriptions={},
            transition_description="",
        ),
        make_annotation(
            object_name="mango",
            action_narration="cut mango",
            state_descriptions={
                "Frame_1": "Mango is whole.",
            },
            transition_description="Mango is cut into pieces.",
        ),
    ]

    result = AnnotationLabelAnalyzer.analyze(annotations)

    assert result.total_annotations == 2
    assert result.object_names == {"mango": 1}
    assert result.action_narrations == {"cut mango": 1}
    assert result.state_descriptions == {"Mango is whole.": 1}
    assert result.transition_descriptions == {
        "Mango is cut into pieces.": 1
    }


def test_handles_empty_annotation_list():
    result = AnnotationLabelAnalyzer.analyze([])

    assert result.total_annotations == 0
    assert not result.object_names
    assert not result.action_narrations
    assert not result.action_terms
    assert not result.action_combinations
    assert not result.state_descriptions
    assert not result.transition_descriptions
