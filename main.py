from dotenv import load_dotenv
from core.utils import get_all_files
from core.image_manipulation import image_segmentation
from tqdm import tqdm
import os


### Setup ###
# Load variables from .env file
load_dotenv()

# Base Path for image folder
base_img_folder: str = os.getenv("BASE_IMG_FOLDER")
base_mask_folder: str = os.getenv("BASE_MASK_FOLDER")
output_folder: str = os.getenv("OUTPUT_FOLDER")

def main() -> None:
    ### Image Processing ###
    files: list[str] = get_all_files(base_mask_folder)

    for file in tqdm(files, desc="Processing Images"):
        image_segmentation(file, base_mask_folder, output_folder)

if __name__ == "__main__":
    main()
