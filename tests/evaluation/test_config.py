from __future__ import annotations

import json

import pytest

from src.sostd.evaluation.config import EvaluationConfig
from pathlib import Path

def test_default_configuration() -> None:
    config = EvaluationConfig()

    assert config.checkpoint == Path(
        "checkpoints/oscar_lite/best.pt"
    )
    assert config.split == "validation"
    assert config.batch_size == 8
    assert config.device == "cuda"
    assert config.amp is True
    assert config.seed == 42


def test_custom_configuration() -> None:
    config = EvaluationConfig(
        batch_size=4,
        num_workers=2,
        device="cuda:0",
        amp=False,
    )

    assert config.batch_size == 4
    assert config.num_workers == 2
    assert config.device == "cuda:0"
    assert config.amp is False


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"split": "train"}, "split"),
        ({"batch_size": 0}, "batch_size"),
        ({"num_workers": -1}, "num_workers"),
        ({"max_state_tokens": 0}, "max_state_tokens"),
        ({"max_transition_tokens": 0}, "max_transition_tokens"),
        ({"num_beams": 0}, "num_beams"),
        ({"seed": -1}, "seed"),
        ({"limit": 0}, "limit"),
        ({"device": " "}, "device"),
    ],
)
def test_invalid_configuration(
    kwargs: dict,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        EvaluationConfig(**kwargs)


def test_load_json_configuration(tmp_path) -> None:
    config_path = tmp_path / "evaluation.json"

    config_path.write_text(
        json.dumps(
            {
                "checkpoint": "checkpoints/oscar_lite/best.pt",
                "output_dir": "outputs/evaluations",
                "split": "validation",
                "batch_size": 4,
                "device": "cuda:0",
                "amp": True,
            }
        ),
        encoding="utf-8",
    )

    config = EvaluationConfig.from_json(config_path)

    assert config.batch_size == 4
    assert config.device == "cuda:0"
    assert config.amp is True


def test_missing_config_file(tmp_path) -> None:
    with pytest.raises(FileNotFoundError):
        EvaluationConfig.from_json(
            tmp_path / "missing.json"
        )


def test_unknown_config_field(tmp_path) -> None:
    config_path = tmp_path / "evaluation.json"

    config_path.write_text(
        json.dumps({"unknown_option": True}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Unknown"):
        EvaluationConfig.from_json(config_path)


def test_to_dict_is_json_serializable() -> None:
    config = EvaluationConfig()

    serialized = json.dumps(config.to_dict())

    assert isinstance(serialized, str)


def test_configuration_is_immutable() -> None:
    config = EvaluationConfig()

    with pytest.raises(AttributeError):
        config.batch_size = 16