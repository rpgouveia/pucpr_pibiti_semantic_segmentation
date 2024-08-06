# Dictionary of RGB colors and their corresponding elements
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


# Function to convert RGB to Grayscale (I need review this idea)
def rgb_to_gray(r, g, b):
    return int(0.299 * r + 0.587 * g + 0.114 * b)


# Dictionary of RGB colors to be converted. (I need review this idea)
# Color: (lower bound, upper bound) (I need rework this)
colors_to_gray = {
    'Yellow': (rgb_to_gray(255, 255, 0), rgb_to_gray(255, 255, 0)),
    'Aquamarine': (rgb_to_gray(106, 246, 195), rgb_to_gray(106, 246, 195)),
    'Light Teal': (rgb_to_gray(145, 255, 194), rgb_to_gray(145, 255, 194)),
    'Light Coral': (rgb_to_gray(255, 198, 188), rgb_to_gray(255, 198, 188)),
    'Light Amber': (rgb_to_gray(242, 211, 154), rgb_to_gray(242, 211, 154)),
    'Light Orange': (rgb_to_gray(231, 193, 155), rgb_to_gray(231, 193, 155)),
    'Green': (rgb_to_gray(0, 255, 0), rgb_to_gray(0, 255, 0)),
    'Light Blue': (rgb_to_gray(169, 199, 235), rgb_to_gray(169, 199, 235)),
    # 'Red': (rgb_to_gray(255, 0, 0), rgb_to_gray(255, 0, 0)),
    'Red': (76, 79),
    'Fuchsia': (rgb_to_gray(255, 0, 255), rgb_to_gray(255, 0, 255)),
    'Light Khaki': (rgb_to_gray(251, 240, 165), rgb_to_gray(251, 240, 165)),
    'Light Gray': (rgb_to_gray(205, 206, 197), rgb_to_gray(205, 206, 197)),
    'Light Olive': (rgb_to_gray(181, 217, 150), rgb_to_gray(181, 217, 150)),
    'Medium Purple': (rgb_to_gray(155, 122, 177), rgb_to_gray(155, 122, 177)),
    'Aqua': (rgb_to_gray(0, 255, 255), rgb_to_gray(0, 255, 255)),
    # 'Blue': (rgb_to_gray(0, 0, 255), rgb_to_gray(0, 0, 255)),
    'Blue': (29, 33),
    'Light Blue Violet': (rgb_to_gray(122, 141, 236), rgb_to_gray(122, 141, 236)),
    'Pale Aqua': (rgb_to_gray(195, 254, 245), rgb_to_gray(195, 254, 245))
}
