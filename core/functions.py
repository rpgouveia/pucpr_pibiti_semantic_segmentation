import numpy as np
import cv2 as cv


def resize_image(img: np.ndarray) -> np.ndarray:
    """
    Resize the given image to 45% of its original size using INTER_AREA interpolation.

    Parameters:
        img (np.ndarray): The image to be resized.

    Returns:
        np.ndarray: The resized image.
    """
    scale_percent = 45
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim: tuple[int, int] = (width, height)

    resized_image: np.ndarray = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    return resized_image

