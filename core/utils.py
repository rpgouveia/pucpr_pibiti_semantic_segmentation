# Função para imprimir o dicionário de cores de forma legível
def print_colors_dict(colors_dict):
    print("Available colors and their corresponding elements:")
    for color_name, (rgb, element) in colors_dict.items():
        print(f"Color: {color_name}, RGB: {rgb}, Element: {element}")
