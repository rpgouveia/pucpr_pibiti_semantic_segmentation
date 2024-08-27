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

