from dotenv import load_dotenv
from core.validation import get_valid_image_number
from core.quantization import process_image
import os


### Setup ###
# Load variables from .env file
load_dotenv()

# Base Path for image folder
base_img_folder: str = os.getenv("BASE_IMG_FOLDER")
base_mask_folder: str = os.getenv("BASE_MASK_FOLDER")
output_folder: str = os.getenv("OUTPUT_FOLDER")

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Choose image for treatment
img_number: str = get_valid_image_number()
mask_path: str = os.path.join(base_mask_folder, f"{img_number}.png")

### Quantization Process ###
layers = process_image(mask_path, output_folder, img_number)

# Logs
print(f"Processamento concluído para a imagem {img_number}. Camadas salvas em {output_folder}.")
