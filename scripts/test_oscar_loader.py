
from src.sostd.data.load_dataset import DatasetLoader
from dotenv import load_dotenv

load_dotenv()

def main():
    loader = DatasetLoader(streaming=True)

    dataset = loader.load()

    print("\n========== DATASET OVERVIEW ==========")
    loader.inspect()

    print("\n========== TRAINING SAMPLE ==========")
    train_sample = next(iter(loader.get_split("train")))
    print(train_sample)

    print("\n========== VALIDATION SAMPLE ==========")
    validation_sample = next(iter(loader.get_split("validation")))
    print(validation_sample)

if __name__ == "__main__":
    main()
