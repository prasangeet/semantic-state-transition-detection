import json

from src.sostd.evaluation.config import EvaluationConfig


def test_evaluation_config_file_loads_correctly():
    config_path = "configs/oscar_lite_evaluation.json"

    config = EvaluationConfig.from_json(config_path)

    assert config.split == "validation"
    assert config.batch_size == 8
    assert config.device == "cuda"
    assert config.amp is True
    assert config.max_state_tokens == 64
    assert config.max_transition_tokens == 96
    assert config.num_beams == 4
    assert config.seed == 42
    assert config.limit is None


def test_evaluation_config_file_uses_expected_checkpoint():
    config = EvaluationConfig.from_json(
        "configs/oscar_lite_evaluation.json"
    )

    assert str(config.checkpoint) == "checkpoints/oscar_lite/best.pt"
    assert str(config.output_dir) == "outputs/evaluations"