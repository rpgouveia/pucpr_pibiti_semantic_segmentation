from dotenv import load_dotenv
from core.validation import get_valid_image_number, validate_image
from core.functions import resize_image, filter_color_and_save
import cv2 as cv
import numpy as np
import os


# Load variables from .env file
load_dotenv()

# Base Path for image folder
base_img_folder: str = os.getenv("BASE_IMG_FOLDER")
base_mask_folder: str = os.getenv("BASE_MASK_FOLDER")
output_folder: str = os.getenv("OUTPUT_FOLDER")

# Choose image for treatment
img_number: str = get_valid_image_number()
img_path: str = os.path.join(base_img_folder, f"{img_number}.png")
mask_path: str = os.path.join(base_mask_folder, f"{img_number}.png")

# Load image and mask
image: np.ndarray = cv.imread(img_path)
mask: np.ndarray = cv.imread(mask_path)

# Image Validation
validate_image(image, img_path, mask, mask_path)

# Resize images for presentation
resized_image: np.ndarray = resize_image(image)
resized_mask: np.ndarray = resize_image(mask)

# Combine images side by side
combined_image: np.ndarray = np.hstack((resized_image, resized_mask))

# Show combined image for the user
cv.imshow("Image and Mask Side by Side", combined_image)

# Wait user press keys to close images
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()

# Filter Process
# Path to save the new image
output_image_path = os.path.join(output_folder, f"{img_number}_filtered.png")

# Filter the red color (in BGR format: [0, 0, 255])
red_color_bgr = [0, 0, 255]
filtered_image = filter_color_and_save(mask, red_color_bgr, output_image_path)

# Show the filtered image to the user
cv.imshow("Filtered Image", filtered_image)
cv.waitKey(0)
cv.destroyAllWindows()