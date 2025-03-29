import os
import random
from PIL import Image

# Define paths
layers = {
    "background": "layers/backgrounds/",
    "base": "layers/base/",
    "eyes": "layers/eyes/",
    "mouth": "layers/mouths/",
    "accessories": "layers/accessories/"
}

# Output folder for generated NFTs
output_dir = "output_nfts"
os.makedirs(output_dir, exist_ok=True)

# Number of NFTs to generate
num_nfts = 10

# Generate NFTs
for i in range(num_nfts):
    # Select random trait for each layer
    selected_layers = {
        layer: random.choice(os.listdir(path)) for layer, path in layers.items()
    }

    # Open images
    final_image = Image.open(layers["background"] + selected_layers["background"]).convert("RGBA")
    base = Image.open(layers["base"] + selected_layers["base"]).convert("RGBA")
    eyes = Image.open(layers["eyes"] + selected_layers["eyes"]).convert("RGBA")
    mouth = Image.open(layers["mouth"] + selected_layers["mouth"]).convert("RGBA")
    accessories = Image.open(layers["accessories"] + selected_layers["accessories"]).convert("RGBA")

    # Merge layers
    final_image.paste(base, (0, 0), base)
    final_image.paste(eyes, (0, 0), eyes)
    final_image.paste(mouth, (0, 0), mouth)
    final_image.paste(accessories, (0, 0), accessories)

    # Save final NFT
    nft_path = f"{output_dir}/nft_{i+1}.png"
    final_image.save(nft_path)

    print(f"NFT {i+1} generated: {nft_path}")