
from __future__ import annotations

from collections import defaultdict

import torch
from transformers import AutoTokenizer

from src.sostd.data.load_dataset import DatasetLoader
from src.sostd.data.annotation_parser import OSCaRAnnotationParser
from src.sostd.data.temporal_sample_builder import TemporalSampleBuilder
from src.sostd.data.temporal_dataset import TemporalDataset
from src.sostd.data.frame_loader import RGBFrameLoader
from src.sostd.models.oscar_lite import OSCaRLite


def build_first_temporal_sample(loader: DatasetLoader):
    """Build one complete temporal sample using the existing data pipeline."""

    print("\nLoading training manifest...")
    train_data = loader.get_split("train")

    print("Loading metadata...")
    metadata_dataset = loader.load_metadata()

    metadata_by_image = {
        row["image_path"]: dict(row)
        for row in metadata_dataset
    }

    print(f"Metadata records: {len(metadata_by_image)}")

    parser = OSCaRAnnotationParser()
    annotations_by_clip = defaultdict(list)

    print("\nParsing training records...")

    for record in train_data:
        image_path = record["image"]
        metadata = metadata_by_image.get(image_path)

        if metadata is None:
            raise ValueError(f"Missing metadata for image: {image_path}")

        frame_annotation = parser.parse_training_record(
            dict(record),
            metadata,
        )

        annotations_by_clip[frame_annotation.clip_id].append(
            frame_annotation
        )

    print(f"Unique clips: {len(annotations_by_clip)}")

    print("\nBuilding clip annotations...")

    for clip_id, frame_annotations in annotations_by_clip.items():
        if len(frame_annotations) != 4:
            continue

        annotation = parser.build_training_clip_annotation(
            frame_annotations
        )

        return TemporalSampleBuilder.build_sample(annotation)

    raise RuntimeError("No complete four-record temporal clip found.")


def print_tensor_statistics(
    name: str,
    tensor: torch.Tensor,
) -> None:
    """Print numerical statistics for a tensor."""

    values = tensor.detach().float()

    print(f"\n{name}")
    print("-" * 65)
    print("Shape:", tuple(values.shape))
    print("Dtype:", tensor.dtype)
    print("Device:", tensor.device)
    print("Mean:", values.mean().item())
    print("Std:", values.std().item())
    print("Min:", values.min().item())
    print("Max:", values.max().item())
    print("Finite:", torch.isfinite(values).all().item())


def inspect_encoder_representations(
    visual_embeddings: torch.Tensor,
    model: OSCaRLite,
) -> None:
    """Inspect visual embeddings and their resulting T5 encoder representations."""

    print("\n" + "=" * 65)
    print("VISUAL-LANGUAGE REPRESENTATION DIAGNOSTICS")
    print("=" * 65)

    decoder = model.language_decoder

    embeddings, attention_mask = decoder._prepare_visual_inputs(
        visual_embeddings,
        None,
    )

    print_tensor_statistics(
        "Visual embeddings before T5",
        embeddings,
    )

    print("\nAttention mask:")
    print("Shape:", tuple(attention_mask.shape))
    print("Dtype:", attention_mask.dtype)
    print("Unique values:", torch.unique(attention_mask).tolist())

    with torch.inference_mode():
        encoder_outputs = decoder.backbone.encoder(
            inputs_embeds=embeddings,
            attention_mask=attention_mask,
            return_dict=True,
        )

    encoder_hidden = encoder_outputs.last_hidden_state

    print_tensor_statistics(
        "T5 encoder output",
        encoder_hidden,
    )

    # Compare the representation magnitudes before and after T5.
    input_rms = embeddings.float().square().mean().sqrt()
    encoder_rms = encoder_hidden.float().square().mean().sqrt()

    print("\nRepresentation magnitude comparison:")
    print("Visual embedding RMS:", input_rms.item())
    print("Encoder output RMS:", encoder_rms.item())

    if not torch.isfinite(encoder_hidden).all():
        raise RuntimeError(
            "T5 encoder produced non-finite representations."
        )

    print("\nEncoder representation inspection completed.")


def print_generation_diagnostics(
    outputs: dict[str, torch.Tensor],
    tokenizer,
    model: OSCaRLite,
) -> None:
    """Print raw token IDs and decoded generation outputs."""

    config = model.language_decoder.backbone.config

    print("\n" + "=" * 65)
    print("RAW GENERATION DIAGNOSTICS")
    print("=" * 65)

    print(f"Tokenizer EOS token ID: {tokenizer.eos_token_id}")
    print(f"Tokenizer PAD token ID: {tokenizer.pad_token_id}")
    print(
        "Decoder start token ID:",
        config.decoder_start_token_id,
    )

    print("\nSpecial tokens:")
    print("EOS token:", tokenizer.eos_token)
    print("PAD token:", tokenizer.pad_token)
    print("UNK token:", tokenizer.unk_token)

    # ---------------------------------------------------------
    # Frame-level state generation
    # ---------------------------------------------------------

    state_tokens = outputs["state_tokens"].detach().cpu()

    print("\n" + "-" * 65)
    print("STATE GENERATION")
    print("-" * 65)

    print("State tensor shape:", tuple(state_tokens.shape))

    for frame_index, tokens in enumerate(state_tokens[0]):
        token_ids = tokens.tolist()

        print(f"\nFrame {frame_index + 1}")
        print("Raw token IDs:")
        print(token_ids)

        print("Decoded with special tokens:")
        print(
            tokenizer.decode(
                token_ids,
                skip_special_tokens=False,
            )
        )

        print("Decoded without special tokens:")
        print(
            tokenizer.decode(
                token_ids,
                skip_special_tokens=True,
            )
        )

        print("Token strings:")
        print(tokenizer.convert_ids_to_tokens(token_ids))

    # ---------------------------------------------------------
    # Transition generation
    # ---------------------------------------------------------

    transition_tokens = (
        outputs["transition_tokens"].detach().cpu()
    )

    print("\n" + "-" * 65)
    print("TRANSITION GENERATION")
    print("-" * 65)

    print(
        "Transition tensor shape:",
        tuple(transition_tokens.shape),
    )

    for batch_index, tokens in enumerate(transition_tokens):
        token_ids = tokens.tolist()

        print(f"\nSample {batch_index + 1}")
        print("Raw token IDs:")
        print(token_ids)

        print("Decoded with special tokens:")
        print(
            tokenizer.decode(
                token_ids,
                skip_special_tokens=False,
            )
        )

        print("Decoded without special tokens:")
        print(
            tokenizer.decode(
                token_ids,
                skip_special_tokens=True,
            )
        )

        print("Token strings:")
        print(tokenizer.convert_ids_to_tokens(token_ids))

    print("\n" + "=" * 65)
    print("END OF GENERATION DIAGNOSTICS")
    print("=" * 65)



def print_model_parameter_diagnostics(model: OSCaRLite) -> None:
    """Report trainable/frozen parameter counts by model component."""

    print("\\n" + "=" * 65)
    print("MODEL PARAMETER DIAGNOSTICS")
    print("=" * 65)

    total_parameters = 0
    trainable_parameters = 0
    component_stats: dict[str, dict[str, int]] = {}

    for name, parameter in model.named_parameters():
        count = parameter.numel()
        total_parameters += count

        status = "trainable" if parameter.requires_grad else "frozen"
        if parameter.requires_grad:
            trainable_parameters += count

        component = name.split(".", 1)[0]
        stats = component_stats.setdefault(
            component,
            {"total": 0, "trainable": 0, "frozen": 0},
        )
        stats["total"] += count
        stats[status] += count

    print(f"{'Component':<28} {'Total':>14} {'Trainable':>14} {'Frozen':>14}")
    print("-" * 74)

    for component, stats in component_stats.items():
        print(
            f"{component:<28} "
            f"{stats['total']:>14,} "
            f"{stats['trainable']:>14,} "
            f"{stats['frozen']:>14,}"
        )

    frozen_parameters = total_parameters - trainable_parameters
    trainable_percentage = (
        100.0 * trainable_parameters / total_parameters
        if total_parameters
        else 0.0
    )

    print("-" * 74)
    print(f"Total parameters:      {total_parameters:,}")
    print(f"Trainable parameters:  {trainable_parameters:,}")
    print(f"Frozen parameters:     {frozen_parameters:,}")
    print(f"Trainable percentage:  {trainable_percentage:.2f}%")

    if trainable_parameters == 0:
        print(
            "\\nWARNING: The model has no trainable parameters. "
            "Check the freeze settings before training."
        )


def main():
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is unavailable.")

    device = torch.device("cuda")

    print("=" * 65)
    print("OSCaR-Lite: Real Dataset Integration Test")
    print("=" * 65)

    print(f"GPU: {torch.cuda.get_device_name(device)}")

    # ---------------------------------------------------------
    # 1. Load dataset and construct a real temporal sample
    # ---------------------------------------------------------

    loader = DatasetLoader(
        dataset_id="ali-vosoughi/oscar-dataset",
        streaming=False,
    )

    loader.load()

    temporal_sample = build_first_temporal_sample(loader)

    print(
        f"\nSelected clip: {temporal_sample.annotation.clip_id}"
    )

    # ---------------------------------------------------------
    # 2. Load actual RGB frames through TemporalDataset
    # ---------------------------------------------------------

    print("\nLoading temporal RGB frames...")

    frame_loader = RGBFrameLoader(token=loader.hf_token)

    dataset = TemporalDataset(
        samples=[temporal_sample],
        frame_loader=frame_loader,
    )

    sample = dataset[0]

    during_indices = sample["frame_indices"]["during"]

    if len(during_indices) != 1:
        raise ValueError(
            f"Expected one during frame, got {len(during_indices)}."
        )

    frames = torch.stack(
        [
            sample["before"],
            sample["during"][during_indices[0]],
            sample["after"],
        ],
        dim=0,
    ).unsqueeze(0)

    frames = frames.to(
        device=device,
        dtype=torch.float16,
    )

    print(f"Input tensor shape: {tuple(frames.shape)}")
    print(f"Frame indices: {sample['frame_indices']}")

    # ---------------------------------------------------------
    # 3. Inspect actual supervision
    # ---------------------------------------------------------

    print("\nObject:", sample["object"])
    print("Action:", sample["action"])

    print("\nGround-truth state descriptions:")

    for frame_key, description in sample["state_descriptions"].items():
        print(f"\n{frame_key}:")
        print(description)

    print("\nGround-truth transition description:")
    print(sample["transition_description"])

    # ---------------------------------------------------------
    # 4. Load pretrained OSCaR-Lite
    # ---------------------------------------------------------

    print("\nLoading OSCaR-Lite...")

    model = OSCaRLite().to(
        device=device,
        dtype=torch.float16,
    )

    model.eval()

    # Inspect trainable and frozen model components.
    print_model_parameter_diagnostics(model)

    tokenizer = AutoTokenizer.from_pretrained(
        "google/flan-t5-small"
    )

    # ---------------------------------------------------------
    # 5. Run actual visual pipeline
    # ---------------------------------------------------------

    print("\nRunning visual encoder and temporal pipeline...")

    torch.cuda.reset_peak_memory_stats(device)

    with torch.inference_mode():
        visual_embeddings = model.encode_visual(frames)

    print(
        f"Visual embeddings: {tuple(visual_embeddings.shape)}"
    )

    assert visual_embeddings.shape == (1, 3, 8, 512)
    assert torch.isfinite(visual_embeddings).all()

    # ---------------------------------------------------------
    # 6. Inspect visual and language representations
    # ---------------------------------------------------------

    inspect_encoder_representations(
        visual_embeddings=visual_embeddings,
        model=model,
    )

    # ---------------------------------------------------------
    # 7. Generate frame states and transition description
    # ---------------------------------------------------------

    print("\nGenerating descriptions...")

    with torch.inference_mode():
        outputs = model.generate(
            frames,
            max_state_tokens=64,
            max_transition_tokens=96,
            num_beams=1,
        )

    print("\nGenerated frame descriptions:")

    for index, tokens in enumerate(outputs["state_tokens"][0]):
        description = tokenizer.decode(
            tokens,
            skip_special_tokens=True,
        )

        print(f"\nFrame {index + 1}:")
        print(description)

    transition_description = tokenizer.decode(
        outputs["transition_tokens"][0],
        skip_special_tokens=True,
    )

    print("\nGenerated transition:")
    print(transition_description)

    # ---------------------------------------------------------
    # 8. Inspect raw generation tokens
    # ---------------------------------------------------------

    print_generation_diagnostics(
        outputs=outputs,
        tokenizer=tokenizer,
        model=model,
    )

    # ---------------------------------------------------------
    # 9. GPU memory statistics
    # ---------------------------------------------------------

    allocated = (
        torch.cuda.max_memory_allocated(device) / 1024**3
    )

    reserved = (
        torch.cuda.max_memory_reserved(device) / 1024**3
    )

    print("\nGPU memory:")
    print(f"Peak allocated: {allocated:.2f} GB")
    print(f"Peak reserved:  {reserved:.2f} GB")

    print("\n" + "=" * 65)
    print("REAL-SAMPLE INTEGRATION TEST PASSED")
    print("=" * 65)


if __name__ == "__main__":
    main()
