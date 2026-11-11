
from src.sostd.data.load_dataset import DatasetLoader


def main():
    loader = DatasetLoader(
        dataset_id="ali-vosoughi/oscar-dataset",
        streaming=False,
    )

    print("Loading OSCaR dataset...")
    loader.load()

    train_data = loader.get_split("train")

    print("\nTraining split type:", type(train_data))

    sample = next(iter(train_data))

    print("\nSample fields:")
    for key, value in sample.items():
        print(f"  {key}: {type(value).__name__}")

    print("\nImage:")
    print(sample.get("image"))

    print("\nConversation:")
    conversations = sample.get("conversations", [])

    for message in conversations[:4]:
        print(message)

    print("\nTotal conversation messages:", len(conversations))


if __name__ == "__main__":
    main()
