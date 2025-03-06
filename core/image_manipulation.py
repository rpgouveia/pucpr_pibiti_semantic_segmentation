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
        input_size (int): The desired height in pixels for the resized image.

    Returns:
        The resized image as a NumPy array with the new dimensions.
    """
    # # Calculate image proportion for resize operation
    # height, width = image.shape[:2]
    # aspect_ratio = width / height
    # new_height = input_size
    # new_width = int(input_size * aspect_ratio)

    # # Resize image respecting the proportion (old version)
    # resized_img = cv.resize(image, (new_width, new_height))
    # resized_img: ndarray = cv.resize(image, (new_width, new_height), interpolation=cv.INTER_NEAREST)
    # return resized_img

    # Resize image (current version)
    resized_img: ndarray = cv.resize(image, (input_size, input_size), interpolation=cv.INTER_NEAREST)
    return resized_img


def image_segmentation(filename: str, base_mask_folder: str, output_folder: str) -> None:
    """
    Segments an image based on predefined color limits and saves the resulting masks as a NumPy array.
    The masks are resized after segmentation.

    Parameters:
        filename (str): The name of the image file to be segmented, including its extension (e.g., "image1.jpg").
        base_mask_folder (str): The directory containing the mask images with the same base name as the input image.
        output_folder (str): The directory where the resulting NumPy array with the combined masks will be saved.

    Procedure:
        1. Extracts the base name of the image (without extension) to locate the corresponding mask file.
        2. Loads the mask image and converts it from BGR to HSV color space.
        3. Applies a series of color-based masks to the HSV image.
        4. Concatenates all masks along the channel dimension.
        5. Resizes the combined mask to the specified dimensions.
        6. Saves the resized combined mask as a NumPy file (.npy) in the specified output folder.

    Returns:
        None. The function saves the combined mask directly to the output folder.
    """
    img_number = filename.split(".")[0]
    mask_path: str = os.path.join(base_mask_folder, f"{img_number}.png")

    # Load and Convert Images
    bgr_img: ndarray = cv.imread(mask_path, 1)
    hsv_img: ndarray = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)

    # Create masks for each color and concatenate them
    masks: list[ndarray] = []
    for lower_bound, upper_bound in color_limits:
        mask: ndarray = cv.inRange(hsv_img, lower_bound, upper_bound)
            # Pseudocódigo para refatoração:
            # Binarização
            # Morfologia (adicionar tamanho de kernel de acordo com a classe)
            # Filtragem por Contornos
            # Resize para 512x512 com Interpolação AREA
            # Binarização (Verificar o threshold na segmentação)

        # Add new axis for each mask binary mask
        mask = mask[..., np.newaxis]
        masks.append(mask)

    # Concatenate masks along the channel dimension Z
    combined_mask: ndarray = np.concatenate(masks, axis=2)

    # Resize the combined mask after segmentation
    # resized_combined_mask = image_resize(combined_mask, input_size=512)

    # Save resized combined mask as a NumPy file
    output_file: str = os.path.join(output_folder, f"{img_number}.npy")
    # np.save(output_file, resized_combined_mask)
    np.save(output_file, combined_mask)