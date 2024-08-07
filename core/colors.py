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

# Dictionary of RGB colors to be converted.
# Color: (lower bound, upper bound)
# Maybe separate by colors first and convert to grayscale after is the right path
colors_to_gray = {
    'Yellow': (225, 225),
    'Aquamarine': (197, 198),
    'Light Teal': (191, 215), # sobreposição de intensidades (precisamos separar)
    'Light Coral': (204, 205), # sobreposição de intensidades (precisamos separar)
    'Light Amber': (210, 213), # sobreposição de intensidades (precisamos separar)
    'Light Orange': (190, 202), # sobreposição de intensidades (precisamos separar)
    'Green': (149, 149),
    'Light Blue': (193, 194), # sobreposição de intensidades (precisamos separar)
    'Red': (76, 76),
    'Fuchsia': (105, 105),
    'Light Khaki': (234, 235), # sobreposição de intensidades (precisamos separar)
    'Light Gray': (203, 204), # sobreposição de intensidades (precisamos separar)
    'Light Olive': (198, 199), # sobreposição de intensidades (precisamos separar)
    'Medium Purple': (137, 138),
    'Aqua': (178, 178),
    'Blue': (29, 29),
    'Light Blue Violet': (146, 148),
    'Pale Aqua': (234, 235) # sobreposição de intensidades (precisamos separar)
}
