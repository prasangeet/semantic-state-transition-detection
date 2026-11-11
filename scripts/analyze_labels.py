from src.sostd.data.annotation_parser import AnnotationParser
from src.sostd.data.label_analyzer import AnnotationLabelAnalyzer
from src.sostd.data.load_dataset import DatasetLoader


def main() -> None:
    loader = DatasetLoader()
    loader.load()

    parser = AnnotationParser()
    annotations = parser.parse_split(loader.get_split("val"))

    statistics = AnnotationLabelAnalyzer.analyze(annotations)
    AnnotationLabelAnalyzer.display(statistics)


if __name__ == "__main__":
    main()
