from core.colors import color_limits
from numpy import ndarray
import numpy as np
import cv2 as cv
import os


def image_resize(image, input_size: int):
    # Calculate image proportion for resize operation
    height, width = image.shape[:2]
    aspect_ratio = width / height
    new_height = input_size
    new_width = int(input_size * aspect_ratio)

    # Resize image
    resized_img = cv.resize(image, (new_width, new_height))
    return resized_img


def image_segmentation(filename, base_mask_folder, output_folder):
    img_number = filename.split(".")[0]
    mask_path: str = os.path.join(base_mask_folder, f"{img_number}.png")

    # Load and Convert Images
    bgr_img: ndarray = cv.imread(mask_path, 1)
    hsv_img: ndarray = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)

    # Resize process
    resized_hsv_img = image_resize(hsv_img, input_size=512)

    # Create masks for each color and concatenate them
    masks: list[ndarray] = []
    for lower_bound, upper_bound in color_limits:
        mask: ndarray = cv.inRange(resized_hsv_img, lower_bound, upper_bound)
        # Add new axis for each mask binary mask
        mask = mask[..., np.newaxis]
        masks.append(mask)

    # Concatenate masks along the channel dimension Z
    combined_mask: ndarray = np.concatenate(masks, axis=2)

    # Save combined mask as a NumPy file
    output_file: str = os.path.join(output_folder, f"{img_number}.npy")
    np.save(output_file, combined_mask)
