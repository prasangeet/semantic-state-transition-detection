"""CLI entry point for OSCaR-Lite evaluation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from src.sostd.evaluation.config import EvaluationConfig
from src.sostd.evaluation.pipeline import EvaluationPipeline


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate a trained OSCaR-Lite checkpoint."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/oscar_lite_evaluation.json"),
        help="Path to the evaluation configuration JSON.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    if not args.config.is_file():
        raise FileNotFoundError(f"Evaluation config not found: {args.config}")

    config = EvaluationConfig.from_json(args.config)
    result = EvaluationPipeline(config).run()

    print("\nOSCaR-Lite evaluation completed.")
    print(f"Split: {result['split']}")
    print(f"Samples evaluated: {result['num_samples']}")
    print("\nGenerated artifacts:")

    for name, path in result["artifacts"].items():
        print(f"  {name}: {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())