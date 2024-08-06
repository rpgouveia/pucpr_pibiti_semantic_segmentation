from core.colors import colors_to_gray
import numpy as np
import cv2 as cv
import os


def process_image(image_path, output_folder, img_number):
    # Carregar a imagem
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Verificar se a imagem foi carregada corretamente
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return
    
    # Obter as dimensões da imagem
    height, width = image.shape
    
    # Inicializar a lista para armazenar as camadas
    layers = []
    
    # Dividir a imagem em camadas com base nas cores
    for color, (lower_bound, upper_bound) in colors_to_gray.items():
        # Criar uma máscara para a camada
        layer = np.zeros((height, width), dtype=np.uint8)
        mask = (image >= lower_bound) & (image <= upper_bound)
        layer[mask] = image[mask]
        
        # Adicionar a camada à lista
        layers.append(layer)
        
        # Verificar se a pasta de saída existe, caso contrário, criar
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Salvar cada camada como uma imagem
        output_path = os.path.join(output_folder, f"{img_number}_layer_{color}.png")
        cv.imwrite(output_path, layer)
    
    return layers

# Exemplo de uso
# image_path = "path/to/your/mask.jpg"
# output_folder = "my/output/folder/"
# img_number = 0
# layers = process_image(image_path, output_folder. img_number)
