def print_colors_dict(colors_dict):
    """
    Print the available colors and their corresponding elements.

    This function takes a dictionary of colors and their corresponding elements,
    and prints each color name, its RGB value, and the associated element in a
    readable format.

    Parameters:
        colors_dict (dict): A dictionary where the keys are color names (str)
                            and the values are tuples containing:
                            - list: The RGB value of the color (e.g., [255, 0, 0])
                            - str: The corresponding element associated with the color

    Example:
        >>> colors_dict = {
        ...     'Red': ([255, 0, 0], 'Passerby'),
        ...     'Yellow': ([255, 255, 0], 'Buildings')
        ... }
        >>> print_colors_dict(colors_dict)
        Available colors and their corresponding elements:
        Color: Red, RGB: [255, 0, 0], Element: Passerby
        Color: Yellow, RGB: [255, 255, 0], Element: Buildings
    """
    print("Available colors and their corresponding elements:")
    for color_name, (rgb, element) in colors_dict.items():
        print(f"Color: {color_name}, RGB: {rgb}, Element: {element}")
