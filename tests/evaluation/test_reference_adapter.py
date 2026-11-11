import pytest

from src.sostd.evaluation.reference_adapter import ReferenceAdapter


@pytest.fixture
def adapter():
    return ReferenceAdapter()


@pytest.fixture
def sample():
    return {
        "state_descriptions": {
            "Frame_1": "The drawer is partially open.",
            "Frame_2": "The drawer is further open.",
            "Frame_3": "The drawer is fully open.",
        },
        "transition_description": "The drawer progressively opens.",
    }


def test_adapts_sample(adapter, sample):
    result = adapter.adapt_sample(sample)

    assert result == {
        "before": "The drawer is partially open.",
        "during": "The drawer is further open.",
        "after": "The drawer is fully open.",
        "transition": "The drawer progressively opens.",
    }


def test_preserves_original_caption_content(adapter, sample):
    result = adapter.adapt_sample(sample)

    assert result["before"] == sample["state_descriptions"]["Frame_1"]
    assert result["transition"] == sample["transition_description"]


def test_strips_outer_whitespace(adapter, sample):
    sample["state_descriptions"]["Frame_1"] = "  Partially open.  "

    result = adapter.adapt_sample(sample)

    assert result["before"] == "Partially open."


def test_rejects_non_dictionary_sample(adapter):
    with pytest.raises(TypeError, match="Sample must be a dictionary"):
        adapter.adapt_sample([])


def test_rejects_invalid_state_descriptions(adapter, sample):
    sample["state_descriptions"] = None

    with pytest.raises(TypeError, match="state_descriptions"):
        adapter.adapt_sample(sample)


@pytest.mark.parametrize("frame_key", ["Frame_1", "Frame_2", "Frame_3"])
def test_rejects_missing_frame_caption(adapter, sample, frame_key):
    del sample["state_descriptions"][frame_key]

    with pytest.raises(ValueError, match=frame_key):
        adapter.adapt_sample(sample)


@pytest.mark.parametrize("caption", ["", "  ", None, 123])
def test_rejects_invalid_frame_caption(adapter, sample, caption):
    sample["state_descriptions"]["Frame_1"] = caption

    with pytest.raises(ValueError, match="Frame_1"):
        adapter.adapt_sample(sample)


def test_rejects_invalid_transition(adapter, sample):
    sample["transition_description"] = ""

    with pytest.raises(ValueError, match="transition_description"):
        adapter.adapt_sample(sample)


def test_adapts_batch(adapter, sample):
    batch = {
        "state_descriptions": [
            sample["state_descriptions"],
            sample["state_descriptions"],
        ],
        "transition_description": [
            sample["transition_description"],
            sample["transition_description"],
        ],
    }

    result = adapter.adapt_batch(batch)

    assert len(result) == 2
    assert result[0]["before"] == "The drawer is partially open."
    assert result[1]["transition"] == "The drawer progressively opens."


def test_rejects_mismatched_batch_lengths(adapter, sample):
    batch = {
        "state_descriptions": [sample["state_descriptions"]],
        "transition_description": [],
    }

    with pytest.raises(ValueError, match="equal lengths"):
        adapter.adapt_batch(batch)


def test_rejects_missing_batch_fields(adapter):
    with pytest.raises(KeyError, match="missing fields"):
        adapter.adapt_batch({})


def test_rejects_non_list_batch_annotations(adapter):
    batch = {
        "state_descriptions": {},
        "transition_description": [],
    }

    with pytest.raises(TypeError, match="must be lists"):
        adapter.adapt_batch(batch)