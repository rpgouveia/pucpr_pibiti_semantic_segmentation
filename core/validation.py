import numpy as np
import sys


def get_valid_image_number() -> str:
    """
    Function to validate if the input is a number within the valid range [000 - 5035].

    Parameters:
        None: This function does not take any parameters.
    
    Returns:
        str: A valid image number as a zero-padded string of length 3.
    """
    while True:
        img_number: str = input("Type the number of image [000 - 5035] for treatment: ")
        if img_number.isdigit() and 0 <= int(img_number) <= 5035:
            # Fill with leading zeros if necessary
            return img_number.zfill(3)  
        else:
            print("Invalid value! Please type a number between 000 and 5035.")


def validate_image(image: np.ndarray, img_path: str, mask: np.ndarray, mask_path: str) -> None:
    """
    Function to validate if the images and masks are loaded correctly.

    Parameters:
        image (np.ndarray): Loaded image.
        img_path (str): Path to the image.
        mask (np.ndarray): Loaded mask.
        mask_path (str): Path to the mask.

    Returns:
        None
    """
    if image is None:
        print(f"Could not read the image at {img_path}")
        sys.exit()

    if mask is None:
        print(f"Could not read the mask at {mask_path}")
        sys.exit()

