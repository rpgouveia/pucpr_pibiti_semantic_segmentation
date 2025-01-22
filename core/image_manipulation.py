from core.colors import color_limits
from numpy import ndarray
import numpy as np
import cv2 as cv
import os


def image_resize(image: ndarray, input_size: int) -> ndarray:
    """
    Resizes an image while maintaining its aspect ratio.

    Parameters:
        image (ndarray): The input image to be resized, represented as a NumPy array.
        input_size (int): The desired height in pixels for the resized image. The width will be adjusted to maintain the original aspect ratio.

    Returns:
        The resized image as a NumPy array with the new dimensions.
    """
    # Modificação: Remoção do cálculo de proporção para viabilizar formato 256, 256, 18
    # Calculate image proportion for resize operation
    # height, width = image.shape[:2]
    # aspect_ratio = width / height
    # new_height = input_size
    # new_width = int(input_size * aspect_ratio)

    # Resize image
    # resized_img: ndarray = cv.resize(image, (new_width, new_height))
    resized_img: ndarray = cv.resize(image, (input_size, input_size))
    return resized_img


def image_segmentation(filename: str, base_mask_folder: str, output_folder: str) -> None:
    """
    Segments an image based on predefined color limits and saves the resulting masks as a NumPy array.

    Parameters:
        filename (str): The name of the image file to be segmented, including its extension (e.g., "image1.jpg").
        base_mask_folder (str): The directory containing the mask images with the same base name as the input image.
        output_folder (str): The directory where the resulting NumPy array with the combined masks will be saved.

    Procedure:
        1. Extracts the base name of the image (without extension) to locate the corresponding mask file.
        2. Loads the mask image and converts it from BGR to HSV color space.
        3. Resizes the HSV image to a specified height while maintaining its aspect ratio.
        4. Applies a series of color-based masks to the resized HSV image.
        5. Concatenates all masks along the channel dimension to form a combined mask.
        6. Saves the combined mask as a NumPy file (.npy) in the specified output folder.

    Returns:
        None. The function saves the combined mask directly to the output folder.
    """
    img_number = filename.split(".")[0]
    mask_path: str = os.path.join(base_mask_folder, f"{img_number}.png")

    # Load and Convert Images
    bgr_img: ndarray = cv.imread(mask_path, 1)
    hsv_img: ndarray = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)

    # Resize process
    # Modificação: Redimensionar máscara no formato 256,256,18
    resized_hsv_img = image_resize(hsv_img, input_size=256)

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
