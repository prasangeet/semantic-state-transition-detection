
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="sostd",
        description="Semantic Object State Transition Detection",
    )

    parser.add_argument(
        "--train",
        action="store_true",
        help="Run the training pipeline",
    )

    args = parser.parse_args()

    if args.train:
        from src.sostd.training.main import main as train_main

        train_main()
    else:
        print("Hello from semantic-object-state-transition-detection!")
        parser.print_help()


if __name__ == "__main__":
    main()
