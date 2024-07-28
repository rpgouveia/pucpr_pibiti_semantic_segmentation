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


def filter_color_and_save(mask: np.ndarray, color_bgr: list[int], output_path: str) -> np.ndarray:
    """
    Filters out elements of a specific color in a mask and saves the result as a new image.

    This function converts the mask image to the HSV color space and applies a filter to keep 
    only the elements of the specified color. The filtered elements are preserved on a black 
    background in the output image.

    Parameters:
        mask (np.ndarray): The input mask image in BGR format.
        color_bgr (list[int]): The target color to filter in BGR format (e.g., [0, 0, 255] for red).
        output_path (str): The path to save the output image.

    Returns:
        np.ndarray: The output image with the filtered color elements on a black background.
    """

    # Convert mask to HSV
    hsv_mask = cv.cvtColor(mask, cv.COLOR_BGR2HSV)

    # Define lower and upper bounds based on the target color
    lower_bound = np.array([color_bgr[0] - 10, 100, 100])
    upper_bound = np.array([color_bgr[0] + 10, 255, 255])

    # Create a binary mask for the color range
    color_mask = cv.inRange(hsv_mask, lower_bound, upper_bound)

    # Create the output image with the color elements on a black background
    output_image = cv.bitwise_and(mask, mask, mask=color_mask)

    # Convert non-color elements to black
    output_image[color_mask == 0] = [0, 0, 0]

    # Save the output image
    cv.imwrite(output_path, output_image)
    return output_image