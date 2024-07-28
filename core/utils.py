import cv2
import numpy as np
import os


# Função para converter RGB para HSV
def rgb_to_hsv(rgb):
    rgb = np.uint8([[rgb]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv[0][0]


# Função para imprimir o dicionário de cores de forma legível
def print_colors_dict(colors_dict):
    print("Available colors and their corresponding elements:")
    for color_name, (rgb, element) in colors_dict.items():
        print(f"Color: {color_name}, RGB: {rgb}, Element: {element}")


# Exemplo de uso
# print_colors_dict(colors_rgb)
