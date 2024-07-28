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


# Função para converter RGB para HSV
def rgb_to_hsv(rgb):
    rgb = np.uint8([[rgb]])
    hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)
    return hsv[0][0]


def filter_color_and_save(img, element, img_number, output_folder):
    # Converter o dicionário de cores RGB para HSV
    colors_hsv = {k: (rgb_to_hsv(v[0]), v[1]) for k, v in colors_rgb.items()}

    # Carregar a imagem
    hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Encontrar a cor correspondente ao elemento
    for color_name, (hsv, elements) in colors_hsv.items():
        if element in elements:
            lower_bound = hsv - np.array([10, 100, 100])
            upper_bound = hsv + np.array([10, 255, 255])
            mask = cv.inRange(hsv_image, lower_bound, upper_bound)
            filtered_image = cv.bitwise_and(img, img, mask=mask)

            # Criar o caminho de saída com o número da imagem e a descrição
            output_path = f"{output_folder}{img_number}_{element.replace(' ', '_').lower()}.png"
            cv.imwrite(output_path, filtered_image)
            return output_path, filtered_image

    return None