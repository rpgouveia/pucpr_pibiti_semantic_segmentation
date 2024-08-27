import os


def get_all_files(base_mask_folder: str) -> list[str]:
    directory: list[str] = os.listdir(base_mask_folder)
    files: list[str] = []
    for file in directory:
        if file.endswith(".png"):
            files.append(file)
    return files
