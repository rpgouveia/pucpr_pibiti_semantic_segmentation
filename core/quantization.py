from core.colors import colors_to_gray
import numpy as np
import cv2 as cv
import os


def process_image(image_path, output_folder, img_number):
    # Load image
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    
    # Check image
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return
    
    # Get image dimensions
    height, width = image.shape
    
    # Setup a list for layers
    layers = []
    
    # Divide image by layers based in colors
    for color, (lower_bound, upper_bound) in colors_to_gray.items():
        # Create mask for a layer
        layer = np.zeros((height, width), dtype=np.uint8)
        mask = (image >= lower_bound) & (image <= upper_bound)
        layer[mask] = image[mask]
        
        # Add layer to the list
        layers.append(layer)
        
        # Check output folder existance, if not create
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Save each layer as image
        output_path = os.path.join(output_folder, f"{img_number}_layer_{color}.png")
        cv.imwrite(output_path, layer)
    
    return layers

# Exemplo de uso
# image_path = "path/to/your/mask.jpg"
# output_folder = "my/output/folder/"
# img_number = 0
# layers = process_image(image_path, output_folder. img_number)
