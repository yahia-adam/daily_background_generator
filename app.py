import os
import torch
import random
from datetime import date
from diffusers import StableDiffusion3Pipeline

GET_SETTING_PATH = "/usr/bin/gsettings"
SAVE_IMAGE_PATH = "/home/adam/adam/daily_background_generator/images"

def generate_prompt():
    styles = [
        "in the style of Vincent van Gogh",
        "in the style of Claude Monet",
        "in the style of Pablo Picasso",
        "in the style of Jackson Pollock",
        "in the style of Frida Kahlo",
        "in the style of Salvador Dalí",
        "in the style of Georgia O'Keeffe",
        "in the style of Edvard Munch"
    ]
    
    subjects = [
        "a vibrant landscape painting",
        "a serene portrait",
        "a bustling cityscape",
        "a tranquil seascape",
        "an abstract composition",
        "a dramatic night sky",
        "a lively street scene",
        "a mysterious forest"
    ]
    
    style = random.choice(styles)
    subject = random.choice(subjects)
    
    prompt = f"{subject} {style}. Swirling brushstrokes, bold colors, and dramatic textures. Emphasize thick impasto and expressive, energetic brushwork. Capture the essence of {style.split('in the style of ')[-1]}’s emotional and dynamic approach."
    
    return prompt

def set_background(image_path):
    os.system(
        f'{GET_SETTING_PATH} set org.gnome.desktop.background picture-uri file:{image_path}')

def generate_image(prompt):
    pipe = StableDiffusion3Pipeline.from_pretrained(
        "stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
    # pipe = pipe.to("cuda")

    image = pipe(
        prompt,
        negative_prompt="",
        seed=0,
		width=1024,
		height=1024,
        num_inference_steps=28,
        guidance_scale=7.0,
    ).images[0]

    image_path = f"{SAVE_IMAGE_PATH}/{date.today()}.png"
    image.save(image_path)
    return image_path

if __name__ == "__main__":
    image_prompt = generate_prompt()
    print(image_prompt)
    image_path = generate_image(image_prompt)
    print(image_path)
    set_background(image_path)
