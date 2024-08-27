import os


def get_all_files(base_mask_folder: str) -> list[str]:
    """
    Retrieves all files with a ".png" extension from the specified directory.

    Parameters:
        base_mask_folder (str): The path to the directory where the files are located.

    Returns:
        list[str]: A list of filenames with a ".png" extension found in the specified directory.
    """
    directory: list[str] = os.listdir(base_mask_folder)
    files: list[str] = []
    for file in directory:
        if file.endswith(".png"):
            files.append(file)
    return files
