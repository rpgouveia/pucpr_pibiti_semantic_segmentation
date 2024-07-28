import cv2
import numpy as np
import os

# Função para converter RGB para HSV
def rgb_to_hsv(rgb):
    rgb = np.uint8([[rgb]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv[0][0]

# Dicionário de cores em RGB e seus elementos correspondentes
colors_rgb = {
    'Red': ([255, 0, 0], 'Passerby'),
    'Yellow': ([255, 255, 0], 'Buildings'),
    'Aquamarine': ([106, 246, 195], 'Motorized_Wheelchair'),
    'Light Teal': ([145, 255, 194], 'Crutch'),
    'Light Coral': ([255, 198, 188], 'Walker'),
    'Light Amber': ([242, 211, 154], 'Wheelchair'),
    'Light Orange': ([231, 193, 155], 'Orthopedic_Cane'),
    'Green': ([0, 255, 0], 'Grass'),
    'Light Blue': ([169, 199, 235], 'Trees_and_Plants'),
    'Fuchsia': ([255, 0, 255], 'Street_Furniture'),
    'Light Khaki': ([251, 240, 165], 'Fountain'),
    'Light Gray': ([205, 206, 197], 'Car_Bus'),
    'Light Olive': ([181, 217, 150], 'Bike'),
    'Medium Purple': ([155, 122, 177], 'Motorcycle_Scooter'),
    'Aqua': ([0, 255, 255], 'Street_Light_Pole'),
    'Blue': ([0, 0, 255], 'Streets'),
    'Light Blue Violet': ([122, 141, 236], 'Sign_Pole'),
    'Pale Aqua': ([195, 254, 245], 'Traffic_Light_Pole')
}

# Função para imprimir o dicionário de cores de forma legível
def print_colors_dict(colors_dict):
    print("Available colors and their corresponding elements:")
    for color_name, (rgb, element) in colors_dict.items():
        print(f"Color: {color_name}, RGB: {rgb}, Element: {element}")

# Exemplo de uso
print_colors_dict(colors_rgb)

# Converter o dicionário de cores RGB para HSV
colors_hsv = {k: (rgb_to_hsv(v[0]), v[1]) for k, v in colors_rgb.items()}

# Função para filtrar e salvar a imagem com base na cor e elemento especificado
def filter_and_save_image(image_path, element):
    # Carregar a imagem
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Encontrar a cor correspondente ao elemento
    for color_name, (hsv, elements) in colors_hsv.items():
        if element in elements:
            lower_bound = hsv - np.array([10, 100, 100])
            upper_bound = hsv + np.array([10, 255, 255])
            mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
            filtered_image = cv2.bitwise_and(image, image, mask=mask)
            
            # Extrair o número do nome do arquivo de entrada
            base_name = os.path.basename(image_path)
            number = os.path.splitext(base_name)[0]
            
            # Criar o caminho de saída com o número da imagem e a descrição
            output_path = f"/home/renato/Pictures/PIBIC/FilteredImage/{number}_{element.replace(' ', '_').lower()}.png"
            cv2.imwrite(output_path, filtered_image)
            return output_path

    return None

# Exemplo de uso
image_path = "/home/renato/Pictures/PIBIC/FinalImagePPM_Mask/000.png"
element = "Passerby"  # Especifique o elemento a ser filtrado
output_path = filter_and_save_image(image_path, element)
print(f"Imagem salva em: {output_path}")