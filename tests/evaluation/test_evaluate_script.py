import json

import pytest

from scripts import evaluate


def test_parse_args_uses_default_config():
    args = evaluate.parse_args([])

    assert str(args.config) == "configs/oscar_lite_evaluation.json"


def test_parse_args_accepts_custom_config(tmp_path):
    config_path = tmp_path / "custom.json"

    args = evaluate.parse_args(["--config", str(config_path)])

    assert args.config == config_path


def test_main_rejects_missing_config(tmp_path):
    missing_config = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError, match="Evaluation config not found"):
        evaluate.main(["--config", str(missing_config)])


def test_main_runs_pipeline(monkeypatch, tmp_path, capsys):
    config_path = tmp_path / "evaluation.json"
    config_path.write_text(
        json.dumps({"split": "validation"}),
        encoding="utf-8",
    )

    class FakeConfig:
        @classmethod
        def from_json(cls, path):
            assert path == config_path
            return cls()

    class FakePipeline:
        def __init__(self, config):
            self.config = config

        def run(self):
            return {
                "split": "validation",
                "num_samples": 10,
                "artifacts": {
                    "results": tmp_path / "results.json",
                    "report": tmp_path / "report.md",
                },
            }

    monkeypatch.setattr(evaluate, "EvaluationConfig", FakeConfig)
    monkeypatch.setattr(evaluate, "EvaluationPipeline", FakePipeline)

    exit_code = evaluate.main(["--config", str(config_path)])

    output = capsys.readouterr().out

    assert exit_code == 0
    assert "Split: validation" in output
    assert "Samples evaluated: 10" in output
    assert "results.json" in output
    assert "report.md" in output