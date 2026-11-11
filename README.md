# CSL7360: Computer Vision

## Semantic Object State Transition Detection

**OSCaR-Lite: Structured State Captioning and Semantic Transition Generation from Video**

**Instructor:** Prof. Deepak Mishra  
**Team:** Vision Bears

**Team members:**
- [Prasangeet Dongre](https://github.com/prasangeet) — B23CH1033
- [Mayuri R. Pujari](https://github.com/Mayu-infinite) — B23ES1026

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/) [![PyTorch](https://img.shields.io/badge/PyTorch-2.11%2B-ee4c2c.svg)](https://pytorch.org/) [![Dataset](https://img.shields.io/badge/Dataset-OSCaR-8A2BE2.svg)](https://huggingface.co/datasets/ali-vosoughi/oscar-dataset)

A research implementation for understanding what an object looks like, how its state evolves, and what semantic transition occurs across a short video sequence. Given three temporally ordered frames, the system generates descriptions for the before, during, and after stages, together with a video-level transition caption.

## Team and contributions

**Team Vision Bears** consists of two members who contributed equally to the project. The work is divided into complementary responsibilities, with **50% contribution from each member**.

| Team member | Roll number | Contribution |
|---|---|---|
| [Prasangeet Dongre](https://github.com/prasangeet) | B23CH1033 | **Model architecture and engineering:** design and implementation of the OSCaR-Lite model versions; DINOv2 and FLAN-T5 integration; temporal-fusion and query-based visual modules; training and evaluation pipeline development; model parameter analysis; experiment execution and reproducibility. |
| [Mayuri R. Pujari](https://github.com/Mayu-infinite) | B23ES1026 | **Research and experimental analysis:** literature review and task formulation; OSCaR dataset exploration and preparation; preprocessing and experiment planning; validation of model outputs; qualitative error analysis; metric consolidation and result visualization; research documentation and presentation. |

**Contribution share:** Prasangeet Dongre — **50%** · Mayuri R. Pujari — **50%**.

Both members collaborated on refining the problem formulation, reviewing experimental findings, and preparing the final course-project submission.

The repository retains four OSCaR-Lite model versions (V1–V4). **V1 and V2 are legacy model implementations:** their architecture definitions and archived validation results remain in the repository, but the current repository no longer supports their training and evaluation workflows. The maintained training/evaluation pipeline is for **V3 and V4**.

## Table of contents

- [Team and contributions](#team-and-contributions)
- [Motivation and task](#motivation-and-task)
- [Dataset](#dataset)
- [Backbone families](#backbone-families)
- [Model versions and support status](#model-versions-and-support-status)
- [Mathematical formulation](#mathematical-formulation)
- [Training setup](#training-setup)
- [Evaluation protocol](#evaluation-protocol)
- [Quantitative results](#quantitative-results)
- [Qualitative transition examples](#qualitative-transition-examples)
- [Comparison with original OSCaR](#comparison-with-original-oscar)
- [Limitations](#limitations)
- [Repository structure](#repository-structure)
- [Setup and usage](#setup-and-usage)
- [References](#references)

## Motivation and task

Image captioning describes a visual observation. Video understanding must additionally account for temporal relationships: what was true before an action, what is observed while it unfolds, and what is different afterward.

Given three ordered frames:

```python
F = [F_before, F_during, F_after]
```

the model generates four outputs:

| Output | Meaning |
|---|---|
| `C_before` | State/scene description associated with the first frame |
| `C_during` | State/scene description associated with the second frame |
| `C_after` | State/scene description associated with the third frame |
| `C_transition` | Video-level description of the evolution across the sequence |

Frame captions describe observations; the transition caption should connect those observations into a coherent temporal account. This system is not a physical simulator and does not directly estimate forces or hidden object properties that are not visually supported.

## Dataset

### OSCaR

Experiments use the [OSCaR dataset](https://huggingface.co/datasets/ali-vosoughi/oscar-dataset), introduced by Nguyen et al. (2024), *OSCaR: Object State Captioning and State Change Representation*, Findings of NAACL 2024.

OSCaR was curated from egocentric video collections, notably EPIC-KITCHENS and Ego4D. The paper introduces object-state captioning and object-state-change captioning as natural-language tasks and describes a benchmark with human-verified captions.

The repository's dataset exploration identified the following metadata characteristics for the dataset version used in this project:

| Property | Observed value |
|---|---:|
| Metadata records | 30,308 |
| Unique training clips | 7,077 |
| Training object classes | 305 |
| Frames per temporal sample | 3 |
| Temporal ordering | Before → During → After |

These counts describe the project's inspected metadata/split, not the full counts of every subset described in the OSCaR paper. The paper separately reports a curated collection of 14,084 annotated video segments and its own 500-video benchmark. Those totals should not be conflated.

### Visual preprocessing and cached features

The feature extraction pipeline uses DINOv2 at 224 × 224 resolution. With a patch size of 14, the patch grid is 16 × 16:

```python
patch_tokens = (224 // 14) * (224 // 14)  # 256
cls_tokens = 1
total_tokens = patch_tokens + cls_tokens  # 257
feature_dim = 1024  # DINOv2-Large
frames = 3

cached_sample_shape = (B, frames, total_tokens, feature_dim)
# (B, 3, 257, 1024)
```

Precomputing visual features avoids repeatedly running the frozen visual encoder during caption-model training. The final V3 and V4 experiments use `data/OSCaR/cached_features_v3_large`.

## Backbone families

The four model versions use different backbone sizes. V1 uses DINOv2-Small; V2 defaults to DINOv2-Base and its encoder module supports Small/Base; V3 and V4 use DINOv2-Large. The language decoders include FLAN-T5-Small and FLAN-T5-Base, with V1 defaulting to Small and V2–V4 defaulting to Base. The reported experiments use **DINOv2-Large + FLAN-T5-Base**.

### DINOv2 visual encoders

DINOv2 is a self-supervised vision Transformer family. The encoder's final hidden-state tokens are used as visual representations. With 224 × 224 inputs and 14 × 14 patches, the output contains one CLS token and 256 patch tokens.

| Variant | Hugging Face model ID | Hidden dimension | Transformer blocks | Patch size | Tokens at 224² |
|---|---|---:|---:|---:|---:|
| DINOv2-Small | `facebook/dinov2-small` | 384 | 12 | 14 | 257 |
| DINOv2-Base | `facebook/dinov2-base` | 768 | 12 | 14 | 257 |
| DINOv2-Large | `facebook/dinov2-large` | 1024 | 24 | 14 | 257 |

```python
small_features = (B, 257, 384)
base_features  = (B, 257, 768)
large_features = (B, 257, 1024)
```

The temporal fusion input dimension must match the selected encoder output dimension. In the checked-in V3/V4 encoder wrappers, `MODEL_NAME`, `HIDDEN_SIZE`, and the expected layer count are fixed to DINOv2-Large; using Small or Base requires adapting the encoder wrapper and downstream temporal dimensions.

### FLAN-T5 language decoders

Visual embeddings are projected into the language model's `d_model` dimension and passed through the `inputs_embeds` interface.

| Variant | Hugging Face model ID | `d_model` |
|---|---|---:|
| FLAN-T5-Small | `google/flan-t5-small` | 512 |
| FLAN-T5-Base | `google/flan-t5-base` | 768 |

The decoder implementation supports `google/flan-t5-small` and `google/flan-t5-base`, as well as frozen or selective fine-tuning configurations. The reported V3/V4 experiments use frozen FLAN-T5-Base.

### DINOv2 visual encoder and FLAN-T5 language model architecture

The diagram below shows the end-to-end visual-to-language path used by the reported experiments. DINOv2-Large extracts patch-level visual tokens; the V3/V4 modules add temporal reasoning and produce language-compatible visual embeddings; FLAN-T5-Base consumes those embeddings through its encoder input interface and generates the captions.

```mermaid
flowchart LR
  subgraph Vision["DINOv2-Large visual encoder"]
    A["Three ordered RGB frames<br/>Before · During · After"] --> B["Preprocessing<br/>Resize to 224 × 224<br/>ImageNet normalization"]
    B --> C["Patch embedding<br/>14 × 14 patch size<br/>16 × 16 patch grid"]
    C --> D["Add CLS and positional embeddings"]
    D --> E["24 ViT Transformer blocks<br/>hidden dimension = 1024"]
    E --> F["Per-frame visual tokens<br/>1 CLS + 256 patch tokens<br/>(257 × 1024)"]
  end

  subgraph Adapter["OSCaR-Lite temporal reasoning and visual-to-language adapter"]
    F --> G["Factorized spatiotemporal fusion<br/>4 blocks<br/>Spatial attention within each frame<br/>Temporal attention across frames"]
    G --> H["V3 readout<br/>Learned visual resampler<br/>32 queries per frame"]
    G --> I["V4 readout"]
    I --> I1["State queries<br/>16 queries per frame"]
    I --> I2["Transition queries<br/>32 queries across all frames"]
    H --> J["Visual projection<br/>1024 → 768"]
    I1 --> J
    I2 --> J
    J --> K["Visual embeddings<br/>passed through inputs_embeds"]
  end

  subgraph Language["FLAN-T5-Base language model"]
    K --> L["T5 encoder<br/>12 Transformer blocks<br/>Self-attention + feed-forward"]
    L --> M["Contextual encoder representations"]
    M --> N["T5 decoder<br/>12 Transformer blocks<br/>Masked self-attention<br/>Cross-attention + feed-forward"]
    N --> O["Autoregressive text generation"]
    O --> P["Before / During / After<br/>state captions"]
    O --> Q["Video-level transition caption"]
  end
```

**Reported configuration:** `facebook/dinov2-large` (24 layers, 1024-dimensional features, patch size 14) and `google/flan-t5-base` (`d_model = 768`, 12 encoder blocks, 12 decoder blocks). The visual embeddings are supplied to `T5ForConditionalGeneration` with `inputs_embeds`; they are therefore processed by the T5 encoder before the decoder generates caption tokens. FLAN-T5-Base is frozen in the reported V3/V4 experiments. The code also supports FLAN-T5-Small as an alternative, but the reported results use Base.

## Model versions and support status

**V1 and V2 are legacy/reference model implementations.** Their model definitions and archived validation results remain in the repository. However, the current repository no longer supports training or evaluation workflows for V1 and V2. The maintained training and evaluation pipeline is for **V3 and V4**; the historical V1/V2 results are included in the quantitative comparison below.

The next two sections describe the currently maintained model versions. Parameter-count breakdowns for all four model versions are provided separately below.

### V3 — factorized spatiotemporal fusion

V3 is the first model version reported here. It uses a frozen DINOv2-Large encoder, factorized spatial/temporal Transformer fusion, a learned visual resampler, a visual projection, and a frozen FLAN-T5-Base language model.

#### V3 architecture

```mermaid
flowchart TD
  A["Three ordered RGB frames<br/>Before · During · After"] --> B["DINOv2-Large<br/>frozen visual encoder"]
  B --> C["Per-frame tokens<br/>(B, 3, 257, 1024)"]
  C --> D["Input projection<br/>1024 → 1024"]
  D --> E["Learned temporal position embeddings"]
  E --> ENCODER_IN["Spatiotemporal encoder<br/>4 repeated blocks"]
  ENCODER_IN --> F1["Spatial self-attention<br/>within each frame"]
  F1 --> F2["Spatial residual + FFN"]
  F2 --> F3["Temporal self-attention<br/>same token position across frames"]
  F3 --> F4["Temporal residual + FFN"]
  F4 --> G["Fused token grid<br/>(B, 3, 257, 1024)"]
  G --> H["Visual resampler<br/>32 learned queries per frame"]
  H --> I["Visual projection<br/>1024 → 768"]
  I --> J["Frozen FLAN-T5-Base"]
  J --> K1["Before caption"]
  J --> K2["During caption"]
  J --> K3["After caption"]
  J --> K4["Transition caption"]
```

#### V3 processing details

1. **Visual encoding:** DINOv2-Large extracts one CLS token and 256 patch tokens for each frame.
2. **Spatial attention:** visual tokens within a frame attend to other tokens in that frame.
3. **Temporal attention:** at each token position, representations attend across the ordered frames.
4. **Visual resampling:** 32 learned queries independently retrieve information from each temporally fused frame representation.
5. **Projection:** the 1024-dimensional visual representation is mapped to FLAN-T5-Base's 768-dimensional embedding space.
6. **Language generation:** frame-specific visual tokens supervise the three state captions; the temporally fused visual representation also conditions transition-caption generation.

#### V3 configuration

| Parameter | Value |
|---|---:|
| Visual backbone | DINOv2-Large (frozen) |
| Input frames | 3 |
| Visual tokens per frame | 257 |
| Feature dimension | 1024 |
| Temporal hidden dimension | 1024 |
| Attention heads | 16 |
| Factorized blocks | 4 |
| Resampler queries | 32 per frame |
| Visual projection | 1024 → 768 |
| Language decoder | FLAN-T5-Base (frozen) |
| State target length | 128 tokens |
| Transition target length | 128 tokens |
| Dropout | 0.1 |

### V4 — hierarchical spatiotemporal captioner

V4 uses the same factorized spatiotemporal token encoder but replaces V3's single shared visual resampling path with **separate learned-query paths for state and transition captioning**:

- Frame-local state queries attend to tokens from each individual frame. Those frame tokens already contain temporal context from the shared encoder.
- Video-level transition queries attend to the concatenated visual-token memory from all frames.

This separates the representation used for a frame-level state description from the representation used for the sequence-level transition description.

#### V4 architecture

```mermaid
flowchart TD
  A["Three ordered RGB frames<br/>Before · During · After"] --> B["DINOv2-Large<br/>frozen visual encoder"]
  B --> C["Cached visual features<br/>(B, 3, 257, 1024)"]
  C --> D["Input projection / identity<br/>1024 → 1024"]
  D --> E["Learned frame-position embeddings"]
  E --> ENCODER_IN["Spatiotemporal encoder<br/>4 repeated blocks"]
  ENCODER_IN --> F1["Spatial self-attention<br/>tokens within each frame"]
  F1 --> F2["Spatial FFN + residual"]
  F2 --> F3["Temporal self-attention<br/>same token index across frames"]
  F3 --> F4["Temporal FFN + residual"]
  F4 --> G["Frame features<br/>(B, 3, 257, 1024)"]
  G --> SM["Frame-local memory<br/>(B × 3, 257, 1024)"]
  SQ["Learned state queries<br/>16 per frame"] --> SQB["2 × QueryCrossAttentionBlock"]
  SM --> SQB
  SQB --> SF["State features<br/>(B, 3, 16, 1024)"]
  SF --> SP["Shared visual projection<br/>1024 → 768"]
  SP --> SD["Frozen FLAN-T5-Base"]
  SD --> SC["Before / During / After captions"]
  G --> TM["Video memory<br/>(B, 3 × 257, 1024)"]
  TQ["Learned transition queries<br/>32 per video"] --> TQB["2 × QueryCrossAttentionBlock"]
  TM --> TQB
  TQB --> TF["Transition features<br/>(B, 32, 1024)"]
  TF --> TP["Shared visual projection<br/>1024 → 768"]
  TP --> TD["Frozen FLAN-T5-Base"]
  TD --> TC["Transition caption"]
  TF --> POOL["Mean pool over 32 queries"]
  POOL --> OH["Object classification head<br/>305 classes"]
  POOL -.-> AH["Optional action head<br/>disabled in reported run"]
```

#### V4 feature paths

**Shared spatiotemporal encoder.** Input features have shape `(B, 3, 257, 1024)`. Each of four blocks performs spatial multi-head self-attention independently within each frame, followed by temporal multi-head self-attention across frames for each token slot. Residual connections, layer normalization, and feed-forward networks are included. The result is `(B, 3, 257, 1024)`.

**Frame-level state path.** Frame features are reshaped to `(B × 3, 257, 1024)`. Each frame receives 16 learned state queries. Two query cross-attention blocks allow each frame's queries to retrieve information from its corresponding frame memory. The state representation is `(B, 3, 16, 1024)`, projected to 768 dimensions, and passed to FLAN-T5-Base for the three state captions.

Although the query memory is frame-local at this stage, its tokens already contain temporal context from the shared encoder.

**Video-level transition path.** Frame tokens are concatenated into a video memory of shape `(B, 3 × 257, 1024)`. Thirty-two learned transition queries retrieve information from this joint memory through two query cross-attention blocks. The resulting representation `(B, 32, 1024)` is projected to 768 dimensions and passed to FLAN-T5-Base to generate the transition caption.

**Auxiliary object classification.** The transition query representation is mean-pooled across 32 queries and passed to an object classification head. The reported training configuration uses 305 classes and an object loss weight of 0.05. The code also exposes an optional action head, but the reported configuration does not enable action classification; its presence in the API is not an action-recognition result.

#### V4 configuration

| Parameter | Value |
|---|---:|
| Visual backbone | DINOv2-Large (frozen) |
| Input frames | 3 |
| Visual tokens per frame | 257 |
| Feature dimension | 1024 |
| Spatiotemporal hidden dimension | 1024 |
| Attention heads | 16 |
| Spatiotemporal blocks | 4 |
| State queries | 16 per frame |
| Transition queries | 32 per video |
| Query cross-attention blocks | 2 per path |
| Visual projection | 1024 → 768 |
| Language decoder | FLAN-T5-Base (frozen) |
| Object classes | 305 |
| Object loss weight | 0.05 |
| State target length | 128 tokens |
| Transition target length | 128 tokens |
| Dropout | 0.1 |

## Model parameter counts

Each model has its own parameter table below. Counts describe the complete raw-frame-to-caption architecture: visual encoder + temporal/readout modules + visual projection + language model. Default freeze settings are shown; changing the encoder or decoder fine-tuning configuration changes the trainable/frozen split, but not the full architecture count.

### V1 — DINOv2-Small + FLAN-T5-Small

| Module | Configuration | Parameters | Default status |
|---|---|---:|---|
| DINOv2-Small visual encoder | 384 dimensions, 12 Transformer blocks | 22,056,576 | Frozen |
| Temporal fusion | 384 → 256; 2 Transformer layers, 4 heads | 1,679,360 | Trainable |
| Visual resampler | 8 learned queries, 4-head cross-attention | 791,808 | Trainable |
| Visual projection | LayerNorm + 256 → 512 linear projection | 132,096 | Trainable |
| FLAN-T5-Small | 512-dimensional encoder/decoder, 8 + 8 blocks | 76,961,152 | Frozen by default |
| **Full V1 architecture** | **All modules above** | **101,620,992** | **Full model** |
| **Trainable task-specific modules** | Temporal fusion + resampler + projection | **2,603,264** | **Trainable** |
| **Frozen modules** | DINOv2-Small + FLAN-T5-Small | **99,017,728** | **Frozen by default** |

### V2 — DINOv2-Base + FLAN-T5-Base

| Module | Configuration | Parameters | Default status |
|---|---|---:|---|
| DINOv2-Base visual encoder | 768 dimensions, 12 Transformer blocks | 86,580,480 | Frozen by default |
| Temporal fusion | 768 → 512; 3 Transformer layers, 8 heads | 9,853,440 | Trainable |
| Visual resampler | 16 learned queries, 8-head cross-attention | 3,160,576 | Trainable |
| Visual projection | LayerNorm + 512 → 768 linear projection | 395,008 | Trainable |
| FLAN-T5-Base | 768-dimensional encoder/decoder, 12 + 12 blocks | 247,577,856 | Frozen by default |
| **Full V2 architecture** | **All modules above** | **347,567,360** | **Full model** |
| **Trainable task-specific modules** | Temporal fusion + resampler + projection | **13,409,024** | **Trainable** |
| **Frozen modules** | DINOv2-Base + FLAN-T5-Base | **334,158,336** | **Frozen by default** |

### V3 — DINOv2-Large + FLAN-T5-Base

| Module | Configuration | Parameters | Default status |
|---|---|---:|---|
| DINOv2-Large visual encoder | 1024 dimensions, 24 Transformer blocks | 304,368,640 | Frozen; cached during caption training |
| Factorized spatiotemporal fusion | 4 blocks; spatial + temporal attention; 16 heads | 101,824,512 | Trainable |
| Learned visual resampler | 32 queries per frame; cross-attention + FFN | 12,628,992 | Trainable |
| Visual projection | LayerNorm + 1024 → 768 linear projection | 789,248 | Trainable |
| FLAN-T5-Base | 768-dimensional encoder/decoder, 12 + 12 blocks | 247,577,856 | Frozen |
| **Full V3 architecture** | **All modules above** | **667,189,248** | **Full model** |
| **Caption-training graph** | **Cached-feature encoder + V3 trainable modules + FLAN-T5-Base** | **362,820,608** | **DINOv2 excluded from this graph** |
| **Trainable task-specific modules** | Fusion + resampler + projection | **115,242,752** | **Trainable** |
| **Frozen modules in caption-training graph** | FLAN-T5-Base | **247,577,856** | **Frozen** |
| **Frozen modules in full architecture** | DINOv2-Large + FLAN-T5-Base | **551,946,496** | **Frozen** |

### V4 — DINOv2-Large + FLAN-T5-Base

| Module | Configuration | Parameters | Default status |
|---|---|---:|---|
| DINOv2-Large visual encoder | 1024 dimensions, 24 Transformer blocks | 304,368,640 | Frozen; cached during caption training |
| Hierarchical temporal/query module | 4 factorized blocks + 2 state-query blocks + 2 transition-query blocks; 16 state queries/frame; 32 transition queries/video | 168,023,040 | Trainable |
| Shared visual projection | LayerNorm + 1024 → 768 linear projection | 789,248 | Trainable |
| Object classification head | 305 classes | 683,313 | Trainable |
| FLAN-T5-Base | 768-dimensional encoder/decoder, 12 + 12 blocks | 247,577,856 | Frozen |
| **Full V4 architecture** | **All modules above** | **721,442,097** | **Full model** |
| **Caption-training graph** | **Cached-feature encoder + V4 trainable modules + FLAN-T5-Base** | **417,073,457** | **DINOv2 excluded from this graph** |
| **Trainable task-specific modules** | Temporal/query module + projection + object head | **169,495,601** | **Trainable** |
| **Frozen modules in caption-training graph** | FLAN-T5-Base | **247,577,856** | **Frozen** |
| **Frozen modules in full architecture** | DINOv2-Large + FLAN-T5-Base | **551,946,496** | **Frozen** |

## Total parameter comparison

The comparison below covers the currently maintained V3 and V4 caption-training pipelines. Each row is kept on its own line so GitHub renders this as a table rather than a wrapped block of raw Markdown.

| Model | Full architecture | Caption-training graph | Trainable in graph | Frozen in graph | Trainable share |
|---|---:|---:|---:|---:|---:|
| V3 | 667,189,248 (667.19M) | 362,820,608 (362.82M) | 115,242,752 (115.24M) | 247,577,856 (247.58M) | 31.76% |
| V4 | 721,442,097 (721.44M) | 417,073,457 (417.07M) | 169,495,601 (169.50M) | 247,577,856 (247.58M) | 40.64% |

### Parameter-counting methodology and caveats

- **DINOv2 positional embeddings:** the Hugging Face DINOv2 Small/Base/Large configs use a native 518 × 518 image size with 14 × 14 patches (37 × 37 patch positions). The project encoder resizes runtime frames to 224 × 224 and the model interpolates positional embeddings for that input, but the learned checkpoint position-embedding table remains at its configured size. Parameter totals therefore include that native learned table rather than counting only 257 positions.
- **DINOv2 count basis:** counts use the Hugging Face `Dinov2Model` topology, including patch projection, CLS/mask/position embeddings, Transformer blocks, LayerScale parameters, and final normalization. No optional register tokens are included.
- **FLAN-T5 count basis:** counts use the Hugging Face checkpoint configurations and `T5ForConditionalGeneration` topology, including encoder, decoder, shared token embedding, and the untied language-model head. FLAN-T5-Small has 76,961,152 parameters; FLAN-T5-Base has 247,577,856.
- **Project modules:** V1/V2/V3/V4 task-specific module counts are calculated from the declared PyTorch layer dimensions, query counts, and class counts in their respective implementations.
- **Training/evaluation support:** V1 and V2 are legacy implementations and do not have supported training/evaluation workflows in the current repository. Their tables therefore report full architecture counts, not current training-graph counts. V3/V4 caption training uses cached DINOv2 features, so the DINOv2 encoder is counted in each full architecture but is outside the caption-training graph.
- Counts exclude tokenizer objects, optimizer state, gradients, activations, datasets, and cached feature files. These are architecture parameter counts derived from the checkpoint configurations and module definitions; they are not GPU-memory or training-state estimates.

## Mathematical formulation

The expressions below use code-style notation for convenient copying into implementation notes.

### Input and feature extraction

```python
F = [F_before, F_during, F_after]
X = DINOv2(F)
# X: (B, T=3, N=257, D=1024) for DINOv2-Large
```

### Factorized spatial and temporal attention

```python
X_spatial = X + MultiHeadAttention(
    query=LayerNorm(X),
    key=LayerNorm(X),
    value=LayerNorm(X),
    attention_axis='spatial_tokens_within_each_frame',
)

X_temporal = X_spatial + MultiHeadAttention(
    query=LayerNorm(X_spatial),
    key=LayerNorm(X_spatial),
    value=LayerNorm(X_spatial),
    attention_axis='same_token_slot_across_frames',
)
```

Each block also contains residual feed-forward transformations and normalization. Four blocks are stacked in V3 and V4.

### V3 visual resampling

```python
Q = LearnedQueries(shape=(32, 1024))

for t in range(3):
    Z_state[t] = CrossAttention(
        query=Q,
        key=X_temporal[t],
        value=X_temporal[t],
    )
# Z_state: (B, 3, 32, 1024)
```

### V4 hierarchical query decoding

```python
Q_state = LearnedStateQueries(shape=(16, 1024))
Z_state = QueryDecoder(
    queries=Q_state,
    memory=X_temporal,
    memory_scope='separate_memory_per_frame',
    layers=2,
)
# Z_state: (B, 3, 16, 1024)

M_video = reshape(X_temporal, (B, 3 * 257, 1024))
Q_transition = LearnedTransitionQueries(shape=(32, 1024))
Z_transition = QueryDecoder(
    queries=Q_transition,
    memory=M_video,
    memory_scope='all_frames_jointly',
    layers=2,
)
# Z_transition: (B, 32, 1024)
```

### Visual-to-language projection and multi-task objective

```python
E_state = Linear(1024, 768)(Z_state)
E_transition = Linear(1024, 768)(Z_transition)

L_total = (
    1.00 * L_state
    + 1.00 * L_transition
    + 0.05 * L_object
)
```

`L_state` and `L_transition` are language-model caption generation losses. `L_object` is the auxiliary object-classification cross-entropy loss. V3 uses the two caption objectives without the V4 auxiliary object-classification term.

## Training setup

The reported V3 and V4 experiments use the following main optimization settings:

| Setting | Value |
|---|---:|
| Epochs | 50 |
| Random seed | 42 |
| Batch size | 8 |
| Optimizer | AdamW |
| Learning rate | 1e-4 |
| Weight decay | 1e-4 |
| Scheduler | ReduceLROnPlateau |
| Scheduler factor | 0.5 |
| Scheduler patience | 3 |
| Minimum learning rate | 1e-6 |
| Early-stopping patience | 8 |
| Gradient clipping | 1.0 |
| Mixed precision | Enabled |
| State loss weight | 1.0 |
| Transition loss weight | 1.0 |
| V4 object loss weight | 0.05 |

The visual encoder and FLAN-T5-Base decoder are frozen in the reported experiments. The trainable temporal and projection modules learn to map DINOv2 representations into the frozen language model's embedding space.

## Evaluation protocol

The repository contains archived validation reports for **V1, V2, V3, and V4.1**. Each report lists 500 validation samples. Since each sample has four caption outputs (before, during, after, and transition), each run contains up to 2,000 caption-level comparisons.

V1 and V2 are legacy model implementations: their historical evaluation artifacts remain available, but the current repository no longer supports their training and evaluation workflows. V3 and V4 are the versions supported by the maintained pipeline.

| Metric | Interpretation |
|---|---|
| BLEU-1 | Unigram overlap |
| BLEU-2 | Bigram overlap |
| BLEU-3 | Trigram overlap |
| BLEU-4 | Four-gram overlap |
| ROUGE-L | Longest-common-subsequence based overlap |
| Semantic similarity | Embedding-based semantic correspondence between generated and reference descriptions |
| Overall temporal score | Arithmetic mean of semantic alignment for before, during, after, and transition |

A caption is counted as low-similarity when its semantic similarity score is below `0.5`. Low-similarity counts are diagnostic flags for manual inspection, not automatically confirmed factual errors. Automatic metrics also do not directly guarantee correct object identity, physical validity, or causal correctness.

## Quantitative results

### Overall comparison: V1 through V4.1

The following summary is taken from the stored `results.json` and `report.md` files for each validation run.

| Model | Report date (UTC) | Validation samples | Overall temporal score | Low-similarity captions | Low-similarity rate |
|---|---|---:|---:|---:|---:|
| V1 | 2026-11-08 | 500 | 0.2021 | 1,985 / 2,000 | 99.25% |
| V2 | 2026-11-09 | 500 | 0.4051 | 1,560 / 2,000 | 78.00% |
| V3 | 2026-11-10 | 500 | 0.5660 | 715 / 2,000 | 35.75% |
| V4.1 | 2026-11-11 | 500 | **0.6257** | **462 / 2,000** | **23.10%** |

The temporal score improves at every version step. The low-similarity caption count also decreases at every step:

| Version transition | Temporal-score gain | Relative score gain | Fewer low-similarity captions | Relative reduction in low-similarity captions |
|---|---:|---:|---:|---:|
| V1 → V2 | +0.2030 | +100.45% | 425 | 21.41% |
| V2 → V3 | +0.1609 | +39.72% | 845 | 54.17% |
| V3 → V4.1 | +0.0597 | +10.55% | 253 | 35.38% |

Across the complete progression, V4.1 gains **0.4236** absolute temporal score over V1 (about **209.60%** relative to V1) and reduces low-similarity captions by **1,523** (about **76.73%**). These are comparisons between successive model versions, not controlled ablations; the table should not be interpreted as isolating the causal contribution of any single architectural component.

### Stage-wise caption metrics

#### V1

| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic similarity |
|---|---:|---:|---:|---:|---:|---:|
| Before | 0.1184 | 0.0379 | 0.0101 | 0.0032 | 0.1743 | 0.1896 |
| During | 0.1086 | 0.0396 | 0.0102 | 0.0025 | 0.1670 | 0.1818 |
| After | 0.1156 | 0.0414 | 0.0106 | 0.0029 | 0.1654 | 0.1806 |
| Transition | 0.0828 | 0.0317 | 0.0130 | 0.0060 | 0.1473 | 0.2565 |

#### V2

| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic similarity |
|---|---:|---:|---:|---:|---:|---:|
| Before | 0.2651 | 0.0992 | 0.0461 | 0.0219 | 0.2092 | 0.3736 |
| During | 0.2558 | 0.1032 | 0.0462 | 0.0231 | 0.2134 | 0.3977 |
| After | 0.2444 | 0.0983 | 0.0460 | 0.0240 | 0.2064 | 0.3884 |
| Transition | 0.2352 | 0.1013 | 0.0481 | 0.0275 | 0.2227 | 0.4607 |

#### V3

| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic similarity |
|---|---:|---:|---:|---:|---:|---:|
| Before | 0.3377 | 0.1659 | 0.0835 | 0.0435 | 0.2247 | 0.5528 |
| During | 0.3149 | 0.1624 | 0.0815 | 0.0416 | 0.2332 | 0.5553 |
| After | 0.3127 | 0.1609 | 0.0812 | 0.0423 | 0.2262 | 0.5548 |
| Transition | 0.3261 | 0.1788 | 0.0986 | 0.0589 | 0.2525 | 0.6012 |

#### V4.1

| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic similarity |
|---|---:|---:|---:|---:|---:|---:|
| Before | 0.3430 | 0.1743 | 0.0908 | 0.0484 | 0.2252 | 0.6167 |
| During | 0.3217 | 0.1738 | 0.0912 | 0.0496 | 0.2340 | 0.6185 |
| After | 0.3170 | 0.1715 | 0.0922 | 0.0502 | 0.2322 | 0.6092 |
| Transition | 0.3857 | 0.2104 | 0.1164 | 0.0705 | 0.2593 | 0.6583 |

### Semantic similarity by stage

| Stage | V1 | V2 | V3 | V4.1 |
|---|---:|---:|---:|---:|
| Before | 0.1896 | 0.3736 | 0.5528 | **0.6167** |
| During | 0.1818 | 0.3977 | 0.5553 | **0.6185** |
| After | 0.1806 | 0.3884 | 0.5548 | **0.6092** |
| Transition | 0.2565 | 0.4607 | 0.6012 | **0.6583** |

Semantic similarity increases monotonically across V1, V2, V3, and V4.1 for all four output stages. Transition captions have the highest semantic similarity within each version.

### Low-similarity cases by stage

| Stage | V1 count | V1 rate | V2 count | V2 rate | V3 count | V3 rate | V4.1 count | V4.1 rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Before | 496 | 99.2% | 402 | 80.4% | 205 | 41.0% | 133 | 26.6% |
| During | 498 | 99.6% | 406 | 81.2% | 183 | 36.6% | 114 | 22.8% |
| After | 497 | 99.4% | 420 | 84.0% | 191 | 38.2% | 122 | 24.4% |
| Transition | 494 | 98.8% | 332 | 66.4% | 136 | 27.2% | 93 | 18.6% |
| **Total** | **1,985** | **99.25%** | **1,560** | **78.00%** | **715** | **35.75%** | **462** | **23.10%** |

### Evaluation plots and reports

The archived reports and their associated figures are stored in the repository:

| Artifact | V1 | V2 | V3 | V4.1 |
|---|---|---|---|---|
| Stage metrics | [V1 plot](outputs/evaluations/oscar_lite/stage_metrics.png) | [V2 plot](outputs/evaluations/oscar_lite_v2/stage_metrics.png) | [V3 plot](outputs/evaluations/v3_frozen/stage_metrics.png) | [V4.1 plot](outputs/evaluations/v4/stage_metrics.png) |
| Temporal alignment | [V1 plot](outputs/evaluations/oscar_lite/temporal_alignment.png) | [V2 plot](outputs/evaluations/oscar_lite_v2/temporal_alignment.png) | [V3 plot](outputs/evaluations/v3_frozen/temporal_alignment.png) | [V4.1 plot](outputs/evaluations/v4/temporal_alignment.png) |
| Full report | [V1 report](outputs/evaluations/oscar_lite/report.md) | [V2 report](outputs/evaluations/oscar_lite_v2/report.md) | [V3 report](outputs/evaluations/v3_frozen/report.md) | [V4.1 report](outputs/evaluations/v4/report.md) |
| Raw metrics and predictions | [V1 results](outputs/evaluations/oscar_lite/results.json) | [V2 results](outputs/evaluations/oscar_lite_v2/results.json) | [V3 results](outputs/evaluations/v3_frozen/results.json) | [V4.1 results](outputs/evaluations/v4/results.json) |

The V3 and V4.1 directories also include HTML prediction/reference browsers. The V1 and V2 report and JSON artifacts remain available for historical comparison, although the current repository no longer supports rerunning their training/evaluation workflows.

## Qualitative transition examples

The following examples are copied from the V4 evaluation's prediction/reference browser. They are representative model outputs, not manually corrected captions.

### Input frame triplets

| Event | Before | During | After |
|---|---|---|---|
| Drawer opening | ![Drawer before](outputs/evaluations/v4/visual_comparison_assets/sample_0001_before.jpg) | ![Drawer during](outputs/evaluations/v4/visual_comparison_assets/sample_0001_during.jpg) | ![Drawer after](outputs/evaluations/v4/visual_comparison_assets/sample_0001_after.jpg) |
| Gas control knob | ![Gas before](outputs/evaluations/v4/visual_comparison_assets/sample_0002_before.jpg) | ![Gas during](outputs/evaluations/v4/visual_comparison_assets/sample_0002_during.jpg) | ![Gas after](outputs/evaluations/v4/visual_comparison_assets/sample_0002_after.jpg) |
| Bottle closing | ![Bottle before](outputs/evaluations/v4/visual_comparison_assets/sample_0003_before.jpg) | ![Bottle during](outputs/evaluations/v4/visual_comparison_assets/sample_0003_during.jpg) | ![Bottle after](outputs/evaluations/v4/visual_comparison_assets/sample_0003_after.jpg) |

### Example 1 — Opening a drawer

**Object/action metadata:** drawer · open drawer

**V4 transition prediction**

> Over the sequence of frames, the kitchen drawer undergoes a transition from being partially open to being fully open. Initially, the drawer is partially open, revealing a kitchen drawer with its contents in view. As the drawer's contents move through the frame, the person's hand interacts with it, indicating a deliberate action. By the final frame, there is a clearer understanding of the individual's interaction with the drawer, suggesting that the drawer may be open for a specific purpose.

**Reference transition**

> As the drawer opens progressively from the first to the third frame, there's a clear transition from partial visibility to full exposure of its contents. Initially, only a fraction of the drawer's items is visible, mainly knives and some cutlery. As the drawer opens further, more items are revealed, expanding the view to include a variety of kitchen tools. The final frame shows the drawer in its fully extended state, displaying an orderly arrangement of utensils, which reflects a well-stocked and systematically organized kitchen drawer. Throughout these transitions, the orderliness of the drawer's contents remains intact, suggesting a functional and well-maintained storage system.

**Observation:** The prediction identifies the main change—progressive drawer opening—but provides less detail about how the visible contents expand and introduces a speculative purpose.

### Example 2 — Turning a gas-stove control knob

**Object/action metadata:** gas · open gas

**V4 transition prediction**

> Over the course of these three frames, there's a clear progression from an inert state to a gas-free state. Initially, the gas burner is in a state of disintegration, indicating that the gas has been removed from the burner. As a result, the flame is reduced to its original state, suggesting that the burner has been turned off. As the sequence progresses, the hand's motion reveals a gradual reduction in the gas's output, implying that there is no longer enough gas in the burner for the desired effect. By the final frame, ...

**Reference transition**

> Throughout the sequence, there is a progressive motion of the gas knob from the off position towards what is assumed to be the ignition point. The individual's fingers adjust their grip and rotate the knob with increasing intent, but despite these actions, there is no visible sign of a flame, which indicates that the gas may be on but not lit, or the ignition is so subtle that it escapes notice from this perspective. The constant in the scene is the presence of kitchen items that remain static, emphasizing the focused action on the gas stove's control knob.

**Observation:** The prediction fails to preserve the reference's central temporal evidence: the control knob rotates while no flame is visible. It invents a gas-removal/turn-off interpretation.

### Example 3 — Closing a bottle

**Object/action metadata:** bottle · close bottle

**V4 transition prediction**

> Over the course of these three frames, there is a clear progression in the state of the water. Initially, the water is in a state of rest, with the glass still in place. As the frame progresses, it becomes more apparent that the water has been drained, indicating a deliberate action. By the final frame, the glass is still in its original state, and the water's surface is clearly visible. This sequence captures a moment when a person engages in something important, such as a drink, or a conversation. The transition from a static state to ...

**Reference transition**

> The sequence of these frames captures the progression of closing a bottle. Initially, the bottle stands open with the cap beside it, then transitions to the cap being guided towards the bottle's mouth, and finally, the cap makes contact with the bottle's neck as the hand prepares to twist it closed. Throughout the sequence, the hand's movements are deliberate and controlled, indicating a careful attempt to reseal the bottle without spillage. The subtle shift in the hand's position and the changing angle of the cap provide a clear visual narrative of the cap being secured back onto the bottle.

**Observation:** This prediction confuses the bottle/cap interaction with a water/glass event. Object identity and action-object grounding remain important failure modes.

More frame-level examples are available in the [V4 visual comparison browser](outputs/evaluations/v4/visual_comparison.html).

## Comparison with original OSCaR

This project is grounded in the problem formulation and dataset introduced by Nguyen et al. (2024). The original paper is the foundational reference, not an unrelated baseline.

### Original OSCaR method

The paper's reported OSCaR model fine-tunes LLaVA with OSCaR instruction data. Its experiments use CLIP ViT-Large-Patch14-336 as the visual encoder and Vicuna 7B/13B as the language model, with LoRA fine-tuning (rank 128, alpha 256). The paper studies a broader instruction-following setting that includes state captioning, state-change captioning, visual question answering, and visual dialogue.

### Architectural comparison

| Dimension | Original OSCaR paper | This project: V3 / V4 |
|---|---|---|
| Research task | Object-state captioning and state-change representation | Structured before/during/after and transition captioning |
| Visual backbone | CLIP ViT-Large-Patch14-336 | DINOv2-Large |
| Language model | Vicuna 7B / 13B | FLAN-T5-Base |
| Language model adaptation | LoRA fine-tuning | Frozen decoder in reported experiments |
| Temporal mechanism | LLaVA-style visual instruction conditioning over selected frames | Explicit factorized spatial/temporal attention |
| Learned query resampling | Not described as the same separate state/transition query design | V3 shared per-frame resampler; V4 separate state and transition query paths |
| Auxiliary object classification | Not reported as the same auxiliary training loss | V4 305-class auxiliary object head |
| Output interface | Broader visual instruction/QA/dialogue tasks | Four structured captions per temporal sample |
| Evaluation | Text metrics, GPT-4V judging, human preference and open-world evaluation | BLEU-1..4, ROUGE-L, semantic similarity and qualitative inspection |

### Original OSCaR reported text metrics

The paper's Table 2 reports these results on its benchmark:

| Model | BLEU | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---:|---:|---:|---:|
| OSCaR 13B (OSCaR data only) | 5.28 | 27.93 | 7.67 | 24.45 |
| OSCaR 7B (OSCaR data only) | 5.10 | 28.27 | 7.42 | 24.77 |
| OSCaR 13B (mixed data) | 5.76 | 29.26 | 8.24 | 25.78 |
| OSCaR 7B (mixed data) | 5.79 | 29.94 | 8.34 | 26.24 |

The paper's table uses its own reported BLEU/ROUGE scale and metric setup. These values must **not** be directly ranked against this repository's stage-specific BLEU-1 through BLEU-4 and ROUGE-L values. A defensible numerical comparison requires identical samples, references, tokenization, metric implementations, and aggregation.

The paper also reports human preference results: OSCaR received 73.93% favorable selections and GPT-4V received 82.5% in the study described in the paper. This repository has not conducted an equivalent human study. The original paper's reported text metrics and human-study percentages are contextual results, not directly comparable to the V3/V4 scores reported above.

### Positioning

The project does not claim to introduce object-state-change understanding or to outperform the original OSCaR system. Its investigation is architectural: it compares factorized temporal fusion (V3) with a hierarchical representation that separates frame-level state-query decoding from video-level transition-query decoding (V4). The V3-to-V4 improvement is internal to this project and uses its own evaluation pipeline.

## Novelty and research contribution

### Scope of the novelty claim

The project does **not** claim to introduce object-state captioning, state-change understanding, the OSCaR dataset, or the before/during/after plus transition-caption task. Nguyen et al. already introduced that task and benchmark in OSCaR. VidOSC (Xue et al., CVPR 2024) is also related work on object-state changes in videos, focusing on recognition/detection of initial, transitioning, and end states, including open-world settings.

The contribution of this repository is the **task-specific model architecture and its empirical investigation**: how to construct separate frame-level state representations and a sequence-level transition representation from a shared spatiotemporally contextualized visual-token sequence.

### Main architectural contributions

| Contribution | Implementation in this project | Research role |
|---|---|---|
| Factorized spatiotemporal token fusion (V3/V4) | Spatial attention mixes visual tokens within each frame; temporal attention then relates the same token slot across the ordered frames. The patch-token grid is retained instead of being immediately collapsed into one global vector. | Builds frame-aligned visual features that carry temporal context. |
| Hierarchical dual-query readout (V4) | A bank of 16 state queries is applied separately to each frame's temporally contextualized memory; a distinct bank of 32 transition queries reads the joint memory from all three frames. | Separates local state-description evidence from clip-level transition evidence. |
| Shared vision-to-language interface | Both readout paths are projected from 1024 to 768 dimensions and condition the same frozen FLAN-T5-Base decoder. | Keeps the language-generation backbone consistent while changing the visual representation supplied to it. |
| Auxiliary object-category supervision (V4) | The mean-pooled transition-query representation is supervised by a 305-class object head, with object loss weight 0.05. | Adds an object-identity learning signal alongside state and transition generation. |
| V3-to-V4 empirical comparison | Both versions are evaluated on 500 validation samples with the same four output stages and the same metrics. | Measures the effect of evolving from shared per-frame resampling to separate state/transition query paths plus object supervision. |

### Central novelty statement

> **OSCaR-Lite V4 investigates a multi-granularity visual readout for object-state understanding: frame-local learned queries generate before/during/after state descriptions, while a separate video-level query bank generates a transition description from the joint temporal memory. An auxiliary object-classification objective supplies an additional semantic identity signal to the video-level representation.**

### Empirical evidence and its limits

On the current 500-sample validation evaluation, V4 increases the overall temporal score from 0.5660 to 0.6257 (+0.0597 absolute, approximately 10.55% relative) and reduces captions below the 0.5 semantic-similarity threshold from 715 to 462 (approximately 35.4% fewer). This is evidence that the complete V4 configuration performs better than the V3 configuration in this experiment.

However, V4 changes several components together: the state/transition readout design, the query modules, and the auxiliary object-classification objective. There is not yet a controlled ablation that isolates each component's individual contribution. The results therefore support the **combined architecture**, not a causal claim that any one component alone produced the gain.

### Novelty boundary

- **Not claimed:** a new dataset, a new object-state-change task, the first use of temporal attention, the first use of learned queries, or state-of-the-art performance against OSCaR/VidOSC.
- **Claimed:** a concrete dual-granularity state/transition architecture for free-form multi-stage caption generation, plus an auxiliary object-supervision branch and a V3/V4 comparison on the OSCaR setup.
- **Still needed to strengthen the claim:** component-wise ablations (remove state queries, remove transition queries, remove object loss), multi-seed evaluation, an open-world evaluation, and human assessment.


## Limitations

1. **Three-frame temporal sampling.** Events with important intermediate steps, long duration, or delayed effects may be missed.
2. **Object identity errors.** Qualitative examples show confusion between objects, such as a bottle/cap event being described as a water/glass event.
3. **Action and transition hallucination.** The model may infer a cause, intention, or physical state that is not supported by the frames. The gas-knob example illustrates this.
4. **Generic descriptions.** Some predictions identify a broad scene change but omit the specific visual evidence that distinguishes the event.
5. **Auxiliary object-classification generalization.** V4 validation object accuracy was approximately 49.4% and macro-F1 approximately 0.465, despite much lower training loss. This indicates a generalization gap in the auxiliary classification branch.
6. **No equivalent human evaluation.** The original OSCaR paper includes human assessment; the reported V3/V4 comparison relies on automatic metrics and qualitative inspection.
7. **No project open-world evaluation.** Equivalent unseen-object and out-of-domain experiments have not been performed here.
8. **Metric limitations.** BLEU/ROUGE are wording-sensitive; embedding similarity can reward semantically related but visually incorrect descriptions. Neither directly measures physical validity or causal correctness.
9. **No controlled V4 component ablation.** V4 changes multiple connected elements relative to V3. Current results do not isolate each component's contribution.
10. **Single reported validation run.** The documented comparison uses 500 validation samples. Results across multiple random seeds and larger evaluation subsets are not reported.

### Research directions

- Object-centric region features or explicit tracking to improve identity consistency.
- Longer temporal windows or adaptive frame sampling.
- Temporal consistency constraints across before/during/after captions.
- Better grounding of action verbs and manipulated objects.
- Controlled ablations of query count, temporal depth, and auxiliary object supervision.
- Multi-seed evaluation and confidence intervals.
- Human evaluation and open-world testing using protocols comparable to the original OSCaR paper.

## Repository structure

```text
semantic-state-transition-detection/
├── configs/
│   ├── oscar_lite_v3_captioning.json
│   ├── oscar_lite_v3_evaluation.json
│   ├── oscar_lite_v4_captioning.json
│   └── oscar_lite_v4_evaluation.json
├── outputs/
│   └── evaluations/
│       ├── v3_frozen/
│       │   ├── report.md
│       │   ├── stage_metrics.png
│       │   ├── temporal_alignment.png
│       │   └── visual_comparison.html
│       └── v4/
│           ├── report.md
│           ├── stage_metrics.png
│           ├── temporal_alignment.png
│           └── visual_comparison.html
├── scripts/
│   ├── dataset_download.py
│   ├── precompute_dinov2_features.py
│   ├── evaluate.py
│   ├── evaluate_v3.py
│   └── inspect_oscar_temporal_samples.py
├── src/sostd/
│   ├── data/
│   ├── evaluation/
│   ├── models/
│   │   ├── v3/
│   │   └── v4/
│   └── training/
├── tests/
├── main.py
├── pyproject.toml
└── uv.lock
```

Large local datasets, cached features, and checkpoints may not be tracked in Git. Their paths are configurable.

## Setup and usage

### Requirements

- Python 3.11 or newer
- PyTorch/torchvision compatible with the target CUDA environment (the lockfile specifies the CUDA 12.8 PyTorch index)
- Sufficient GPU memory for the selected model and batch size
- Hugging Face access for model and dataset downloads

### Install

```bash
git clone https://github.com/prasangeet/semantic-state-transition-detection.git
cd semantic-state-transition-detection
uv sync
```

### Dataset and feature preparation

The dataset downloader retrieves OSCaR into `data/OSCaR/`. You must first accept the dataset's Hugging Face access conditions. The script optionally reads `HF_TOKEN` from a project-root `.env` file:

```bash
uv run python scripts/dataset_download.py
```

The DINOv2-Large feature-precomputation script uses CUDA device `cuda:0` and writes to `data/OSCaR/cached_features_v3_large`:

```bash
uv run python scripts/precompute_dinov2_features.py
```

The expected cached feature shape per sample is `(3, 257, 1024)`. The script skips cache files that pass its shape/content validation.

### Training

The V3/V4 captioning trainer is exposed by `src/sostd/training/captioning_main.py`. Select the corresponding JSON configuration explicitly:

```bash
# Train V3
uv run python -m src.sostd.training.captioning_main --config configs/oscar_lite_v3_captioning.json

# Train V4
uv run python -m src.sostd.training.captioning_main --config configs/oscar_lite_v4_captioning.json
```

Add `--resume` to resume from the latest checkpoint, or `--no-resume` to force a fresh run. The V4 trainer builds its object vocabulary from the training split and saves it in the checkpoint directory.

> **V3 config compatibility:** the checked-in `configs/oscar_lite_v3_captioning.json` currently declares top-level `version: "v3-frozen"`, but the trainer accepts only `"v3"` and `"v4"`. Before running the V3 command, change that field to `"v3"` (or make the same change in a copy of the config). The V4 config already declares `"v4"`.

> **Entrypoint note:** `uv run python main.py --train` currently routes to `src/sostd/training/main.py`, which is a dataset-inspection/annotation-statistics routine and explicitly notes that temporal training data construction is not implemented there. Use `src.sostd.training.captioning_main` for V3/V4 captioning training.

### Evaluation

Run the version-specific evaluation scripts with their explicit configurations:

```bash
# Evaluate V3
uv run python scripts/evaluate_v3.py --config configs/oscar_lite_v3_evaluation.json

# Evaluate V4
uv run python scripts/evaluate.py --config configs/oscar_lite_v4_evaluation.json
```

Both scripts write reports and visual-comparison artifacts under `outputs/evaluations/` as configured in the JSON files.

### Tests

```bash
uv run pytest
```

## Reproducibility notes

- Archived V1, V2, V3, and V4.1 evaluation reports each list 500 validation samples.
- Each sample yields four captions, giving 2,000 caption-level comparisons per model.
- The reported V3 and V4.1 runs use DINOv2-Large cached features with 257 tokens and 1024 dimensions per frame.
- V4 introduces dedicated state and transition query paths and an auxiliary object classification head.
- The overall temporal score is an aggregate defined by this project's evaluation implementation. It is not a standard metric reported by the original OSCaR paper.
- Stored evaluation reports and visual comparison files are the primary experiment artifacts.
- V1 and V2 are legacy architecture implementations retained in the repository. The current repository does not support rerunning their training or evaluation workflows; their archived quantitative results are summarized above and linked to the original reports and JSON files.

## References

1. Nguyen, N., Bi, J., Vosoughi, A., Tian, Y., Fazli, P., & Xu, C. (2024). **OSCaR: Object State Captioning and State Change Representation.** Findings of the Association for Computational Linguistics: NAACL 2024, pp. 3565–3576. [ACL Anthology](https://aclanthology.org/2024.findings-naacl.226/) · [PDF](https://aclanthology.org/2024.findings-naacl.226.pdf) · [Project repository](https://github.com/nguyennm1024/OSCaR).
2. Oquab, M. et al. (2023). **DINOv2: Learning Robust Visual Features without Supervision.** [arXiv:2304.07193](https://arxiv.org/abs/2304.07193) · [Official implementation](https://github.com/facebookresearch/dinov2).
3. Chung, H. W. et al. (2022). **Scaling Instruction-Finetuned Language Models.** [arXiv:2210.11416](https://arxiv.org/abs/2210.11416).
4. Raffel, C. et al. (2020). **Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.** JMLR, 21(140), 1–67. [JMLR](https://jmlr.org/papers/v21/20-074.html).
5. Damen, D. et al. (2018). **Scaling Egocentric Vision: The EPIC-KITCHENS Dataset.** [arXiv:1804.02748](https://arxiv.org/abs/1804.02748).
6. Grauman, K. et al. (2022). **Ego4D: Around the World in 3,000 Hours of Egocentric Video.** CVPR 2022. [Project website](https://ego4d-data.org/) · [CVF paper](https://openaccess.thecvf.com/content/CVPR2022/html/Grauman_Ego4D_Around_the_World_in_3000_Hours_of_Egocentric_Video_CVPR_2022_paper.html).
7. Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). **BLEU: a Method for Automatic Evaluation of Machine Translation.** ACL 2002. [ACL Anthology](https://aclanthology.org/P02-1040/).
8. Lin, C.-Y. (2004). **ROUGE: A Package for Automatic Evaluation of Summaries.** ACL 2004. [ACL Anthology](https://aclanthology.org/W04-1013/).
9. Xue, Z., Ashutosh, K., & Grauman, K. (2024). **Learning Object State Changes in Videos: An Open-World Perspective.** CVPR 2024, pp. 18493–18503. [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Xue_Learning_Object_State_Changes_in_Videos_An_Open-World_Perspective_CVPR_2024_paper.html) · [VidOSC code and dataset](https://github.com/facebookresearch/VidOSC).

## Acknowledgements

This project builds on the OSCaR dataset and research direction introduced by Nguyen et al. and uses publicly available DINOv2 and FLAN-T5 model families. Please cite the original dataset and relevant model papers when using this work.

## Citation

If you use this implementation, cite the original OSCaR work:

```bibtex
@inproceedings{nguyen2024oscar,
  title     = {OSCaR: Object State Captioning and State Change Representation},
  author    = {Nguyen, Nguyen and Bi, Jing and Vosoughi, Ali and Tian, Yapeng and Fazli, Pooyan and Xu, Chenliang},
  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},
  pages     = {3565--3576},
  year      = {2024}
}
```

**Project repository:** https://github.com/prasangeet/semantic-state-transition-detection