from core.colors import colors_rgb
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


def rgb_to_hsv(rgb):
    """
    Convert an RGB color value to HSV color space.

    This function takes an RGB color value, converts it to an HSV (Hue, Saturation, Value) color space,
    and returns the HSV representation of the color.

    Parameters:
        rgb (list or tuple of int): A list or tuple containing three integer values representing the
                                    Red, Green, and Blue components of the color. Each value should be
                                    in the range [0, 255].

    Returns:
        numpy.ndarray:  A NumPy array containing three integer values representing the Hue, Saturation,
                        and Value components of the color. The values are in the ranges:
                        - Hue: [0, 179]
                        - Saturation: [0, 255]
                        - Value: [0, 255]

    Example:
        >>> rgb_color = [255, 0, 0]
        >>> hsv_color = rgb_to_hsv(rgb_color)
        >>> print(hsv_color)
        [0 255 255]
    """
    rgb = np.uint8([[rgb]])
    hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)
    return hsv[0][0]


def filter_color_and_save(img, element, img_number, output_folder):
    """
    Filter an image based on a specific color element and save the result.

    This function takes an image, filters it based on a specified color element,
    and saves the filtered image to a specified output folder. The function also
    returns the path to the saved image and the filtered image itself.

    Parameters:
        img (numpy.ndarray): The input image to be filtered.
        element (str): The color element to filter by (e.g., 'Street_Light_Pole').
        img_number (str): The image number, used for naming the saved file.
        output_folder (str): The path to the folder where the filtered image will be saved.

    Returns:
        tuple: A tuple containing:
            - str: The path to the saved filtered image.
            - numpy.ndarray: The filtered image.

        If the specified element is not found in the color dictionary, the function returns None.
    """
    # Convert the RGB color dictionary to HSV
    colors_hsv = {k: (rgb_to_hsv(v[0]), v[1]) for k, v in colors_rgb.items()}

    # Convert the image to HSV
    hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Find the corresponding color for the element
    for color_name, (hsv, elements) in colors_hsv.items():
        if element in elements:
            lower_bound = hsv - np.array([10, 100, 100])
            upper_bound = hsv + np.array([10, 255, 255])
            mask = cv.inRange(hsv_image, lower_bound, upper_bound)
            filtered_image = cv.bitwise_and(img, img, mask=mask)

            # Create the output path with the image number and description
            output_path = f"{output_folder}{img_number}_{element.replace(' ', '_').lower()}.png"
            cv.imwrite(output_path, filtered_image)
            return output_path, filtered_image

    return None
