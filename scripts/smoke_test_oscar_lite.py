
import torch
from transformers import AutoTokenizer

from src.sostd.models.oscar_lite import OSCaRLite


def main():
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is not available.")

    device = torch.device("cuda")

    print("=" * 60)
    print("OSCaR-Lite pretrained model smoke test")
    print("=" * 60)

    print(f"GPU: {torch.cuda.get_device_name(device)}")
    print(
        f"Total VRAM: "
        f"{torch.cuda.get_device_properties(device).total_memory / 1024**3:.2f} GB"
    )

    torch.cuda.reset_peak_memory_stats()

    print("\nLoading pretrained models...")

    model = OSCaRLite()

    model = model.to(
        device=device,
        dtype=torch.float16,
    )

    model.eval()

    print("Model loaded successfully.")

    print("\nLoading tokenizer...")

    tokenizer = AutoTokenizer.from_pretrained(
        "google/flan-t5-small"
    )

    print("Tokenizer loaded successfully.")

    print("\nCreating dummy video input...")

    frames = torch.rand(
        1, 3, 3, 224, 224,
        device=device,
        dtype=torch.float16,
    )

    print(f"Input shape: {tuple(frames.shape)}")

    print("\nRunning visual encoder...")

    with torch.inference_mode():
        visual_embeddings = model.encode_visual(frames)

    print(
        f"Visual embeddings: {tuple(visual_embeddings.shape)}"
    )

    assert visual_embeddings.shape == (1, 3, 8, 512)
    assert torch.isfinite(visual_embeddings).all()

    print("\nGenerating state and transition descriptions...")

    with torch.inference_mode():
        outputs = model.generate(
            frames,
            max_state_tokens=32,
            max_transition_tokens=48,
            num_beams=1,
        )

    state_tokens = outputs["state_tokens"]
    transition_tokens = outputs["transition_tokens"]

    print("\nGenerated state descriptions:")

    for frame_index, tokens in enumerate(state_tokens[0]):
        description = tokenizer.decode(
            tokens,
            skip_special_tokens=True,
        )
        print(f"Frame {frame_index + 1}: {description}")

    transition_description = tokenizer.decode(
        transition_tokens[0],
        skip_special_tokens=True,
    )

    print("\nGenerated transition description:")
    print(transition_description)

    allocated = torch.cuda.max_memory_allocated(device) / 1024**3
    reserved = torch.cuda.max_memory_reserved(device) / 1024**3

    print("\nGPU memory statistics:")
    print(f"Peak allocated: {allocated:.2f} GB")
    print(f"Peak reserved:  {reserved:.2f} GB")

    print("\nSmoke test completed successfully.")


if __name__ == "__main__":
    main()
