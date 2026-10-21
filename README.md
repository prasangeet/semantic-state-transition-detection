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

Initial experiments will investigate the CLEVRER dataset, with a manageable subset selected for pilot experiments and evaluation.

## Status

Currently in the dataset inspection and experimental setup phase. Model implementations and quantitative results will be added as experiments progress.

## Tech Stack

Python · PyTorch · OpenCV · Computer Vision · Deep Learning
