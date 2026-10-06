import torch
from diffusers import StableDiffusionPipeline

print("Loading AI model...")

pipe = StableDiffusionPipeline.from_pretrained(
    "segmind/tiny-sd",
    torch_dtype=torch.float32
)

print("Model loaded!")

image = pipe(
    "a beautiful wedding decoration with flowers and lights",
    num_inference_steps=8
).images[0]

image.save("generated_images/test_event.png")

print("Image generated successfully!")