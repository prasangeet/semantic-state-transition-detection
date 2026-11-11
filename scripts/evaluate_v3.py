
"""CLI entry point for OSCaR-Lite V3 evaluation."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from src.sostd.evaluation.config import EvaluationConfig
from src.sostd.evaluation.pipeline import EvaluationPipeline


DEFAULT_CONFIG = Path("configs/oscar_lite_v3_evaluation.json")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate a trained OSCaR-Lite V3 checkpoint."
    )

    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help=(
            "Path to the V3 evaluation configuration JSON. "
            f"Defaults to {DEFAULT_CONFIG}."
        ),
    )

    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    if not args.config.is_file():
        raise FileNotFoundError(
            f"V3 evaluation config not found: {args.config}"
        )

    config = EvaluationConfig.from_json(args.config)

    # Prevent accidentally evaluating a V1/V2 checkpoint with this entry point.
    model_version = getattr(config, "model_version", "v2")

    if model_version.lower() != "v3":
        raise ValueError(
            "evaluate_v3 requires model_version='v3' in the "
            f"configuration. Received: {model_version!r}"
        )

    print("=" * 70)
    print("OSCaR-Lite V3 Evaluation")
    print("=" * 70)
    print(f"Configuration: {args.config}")
    print(f"Checkpoint: {config.checkpoint}")
    print(f"Feature directory: {config.feature_dir}")
    print(f"Feature dimension: {config.expected_feature_dim}")

    result = EvaluationPipeline(config).run()

    print("\nOSCaR-Lite V3 evaluation completed.")
    print(f"Model version: {result.get('model_version', 'v3')}")
    print(f"Split: {result['split']}")
    print(f"Samples evaluated: {result['num_samples']}")

    print("\nGenerated artifacts:")

    for name, path in result["artifacts"].items():
        print(f"  {name}: {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
