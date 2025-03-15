from core.image_manipulation import image_segmentation
from core.colors import class_parameters
from core.utils import get_all_files
import numpy as np
import os


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


def validate_segmentation_pipeline(base_mask_folder: str, output_folder: str) -> None:
    """
    Validates the segmentation pipeline by processing a single image and checking the results.
    
    Parameters:
        base_mask_folder (str): The directory containing the mask images.
        output_folder (str): The directory where the results will be saved.
        
    Returns:
        None: Only prints the test results to the screen.
    """
    
    # Check number of defined classes
    print(f"Number of classes in class_parameters: {len(class_parameters)}")
    print(f"Base mask folder: {base_mask_folder}")
    
    # Check if directories exist
    if not os.path.exists(base_mask_folder):
        print(f"ERROR: Mask directory not found: {base_mask_folder}")
        return False
    
    if not os.path.exists(output_folder):
        print(f"WARNING: Output directory not found, creating: {output_folder}")
        os.makedirs(output_folder, exist_ok=True)
    
    # Get files for processing
    files = get_all_files(base_mask_folder)
    if not files:
        print(f"ERROR: No files found in: {base_mask_folder}")
        return False
    
    print(f"Number of files to process: {len(files)}")
    print(f"First file for testing: {files[0]}")
    
    # Process only one file for testing
    sample_file = files[0]
    print(f"Processing test file: {sample_file}")
    
    try:
        image_segmentation(sample_file, base_mask_folder, output_folder)
    except Exception as e:
        print(f"ERROR during processing: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    # Check the result
    img_number = sample_file.split(".")[0]
    output_file = os.path.join(output_folder, f"{img_number}.npy")
    
    if not os.path.exists(output_file):
        print(f"ERROR: Output file was not generated: {output_file}")
        return False
    
    # Load and check the format of the generated file
    result = np.load(output_file)
    print(f"File generated successfully: {output_file}")
    print(f"File shape: {result.shape}")
    
    # Check if the number of channels corresponds to the number of classes
    if result.shape[2] != len(class_parameters):
        print(f"ERROR: Number of channels ({result.shape[2]}) does not match the number of classes ({len(class_parameters)})")
        return False
    
    print("Validation completed successfully!")
