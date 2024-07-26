from core.validation import get_valid_image_number, validate_image
from core.functions import resize_image
import cv2 as cv
import numpy as np
import os


# Base Path for image folder
base_img_folder: str = "/home/renato/Pictures/PIBIC/FinalImage/"
base_mask_folder: str = "/home/renato/Pictures/PIBIC/FinalImagePPM_Mask/"

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
