# Semantic State Transition Detection for Video Understanding

A computer vision project focused on detecting and temporally localizing meaningful changes in the state of a scene from video.

Rather than treating video as a sequence of independent frames, the project aims to represent scenes in terms of objects, their attributes, and their relationships, then identify how these states change over time.

## Objectives

- Represent scene states using objects, attributes, and spatial relationships.
- Detect semantic transitions such as object movement, attribute changes, appearance, disappearance, and relationship changes.
- Localize transitions temporally and identify supporting evidence frames.
- Compare visual-difference baselines against object-aware approaches.
- Evaluate robustness to occlusion, camera motion, and other visual changes.

## Approach

The proposed pipeline combines video preprocessing, object-level perception, temporal state representation, and transition classification. Experiments will compare simple visual baselines with object-aware and relationship-aware methods.

## Dataset

Initial experiments use the [CLEVRER dataset](https://clevrer.csail.mit.edu/), which contains synthetic videos of moving objects, collision annotations for training and validation, and questions for the video splits.

### Download CLEVRER

Run the following commands from the repository root. They download the official CLEVRER videos, training/validation annotations, question JSON files, and optional derender proposals into `data/raw/clevrer/`.

Requirements: `wget` and `unzip`.

```bash
DATA_ROOT="data/raw/clevrer"
DOWNLOADS="$DATA_ROOT/downloads"

mkdir -p \
  "$DOWNLOADS" \
  "$DATA_ROOT/train" \
  "$DATA_ROOT/validation" \
  "$DATA_ROOT/test" \
  "$DATA_ROOT/annotations/train" \
  "$DATA_ROOT/annotations/validation" \
  "$DATA_ROOT/questions" \
  "$DATA_ROOT/derender_proposals"

# 1. Videos: train, validation, and test
wget -c -P "$DOWNLOADS" \
  http://data.csail.mit.edu/clevrer/videos/train/video_train.zip
wget -c -P "$DOWNLOADS" \
  http://data.csail.mit.edu/clevrer/videos/validation/video_validation.zip
wget -c -P "$DOWNLOADS" \
  http://data.csail.mit.edu/clevrer/videos/test/video_test.zip

# 2. Ground-truth annotations: train and validation
wget -c -P "$DOWNLOADS" \
  http://data.csail.mit.edu/clevrer/annotations/train/annotation_train.zip
wget -c -P "$DOWNLOADS" \
  http://data.csail.mit.edu/clevrer/annotations/validation/annotation_validation.zip

# 3. Questions: train, validation, and test
wget -O "$DATA_ROOT/questions/train.json" \
  http://data.csail.mit.edu/clevrer/questions/train.json
wget -O "$DATA_ROOT/questions/validation.json" \
  http://data.csail.mit.edu/clevrer/questions/validation.json
wget -O "$DATA_ROOT/questions/test.json" \
  http://data.csail.mit.edu/clevrer/questions/test.json

# 4. Optional: object derender proposals / attributes
wget -c -P "$DOWNLOADS" \
  http://data.csail.mit.edu/clevrer/derender_proposals.zip

# 5. Extract videos
unzip -oq "$DOWNLOADS/video_train.zip" -d "$DATA_ROOT/train"
unzip -oq "$DOWNLOADS/video_validation.zip" -d "$DATA_ROOT/validation"
unzip -oq "$DOWNLOADS/video_test.zip" -d "$DATA_ROOT/test"

# 6. Extract annotations
unzip -oq "$DOWNLOADS/annotation_train.zip" -d "$DATA_ROOT/annotations/train"
unzip -oq "$DOWNLOADS/annotation_validation.zip" -d "$DATA_ROOT/annotations/validation"

# 7. Extract optional derender proposals
unzip -oq "$DOWNLOADS/derender_proposals.zip" -d "$DATA_ROOT/derender_proposals"
```

The downloaded archives are kept in `data/raw/clevrer/downloads/`. Video and annotation archives may contain nested range directories; recursive file discovery is expected.

**Important:** CLEVRER provides collision annotations for train and validation, but not a corresponding ground-truth annotation archive for the test split. Use the annotated splits for collision evaluation. Derender proposals are optional and may require additional storage.

For source details and other dataset resources, see the [official CLEVRER project page](https://clevrer.csail.mit.edu/).

## Status

Currently in the dataset inspection and experimental setup phase. Model implementations and quantitative results will be added as experiments progress.

## Tech Stack

Python · PyTorch · OpenCV · Computer Vision · Deep Learning

## Citation

If you use CLEVRER, please cite the original paper:

> Yi, K., Gan, C., Li, Y., Kohli, P., Wu, J., Torralba, A., and Tenenbaum, J. B. (2020). *CLEVRER: Collision Events for Video Representation and Reasoning*. International Conference on Learning Representations (ICLR).
