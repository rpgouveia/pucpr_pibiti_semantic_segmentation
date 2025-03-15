from core.colors import class_parameters
from numpy import ndarray
import numpy as np
import cv2 as cv
import os
import collections


def image_resize(image: ndarray, input_size: int) -> ndarray:
    """
    Resizes an image while maintaining its aspect ratio to fit within a square.

    The image is resized such that the shorter side is scaled to `input_size`,
    and the longer side is scaled proportionally. The resulting image is then
    placed within a square canvas of size `input_size x input_size`.

    Parameters:
        image (ndarray): The input image to be resized, represented as a NumPy array.
        input_size (int): The desired size (height and width) in pixels for the square output image.

    Returns:
        ndarray: The resized image as a NumPy array with the new dimensions (input_size x input_size).
    """
    resized_img: ndarray = cv.resize(
        image, (input_size, input_size), interpolation=cv.INTER_AREA
    )
    return resized_img


def extract_color_mask(
    hsv_img: ndarray, lower_bound: ndarray, upper_bound: ndarray
) -> ndarray:
    """
    Extracts a color mask from an HSV image using specified color bounds.

    Parameters:
        hsv_img (ndarray): Input image in HSV color space.
        lower_bound (ndarray): Lower bound of the color range in HSV.
        upper_bound (ndarray): Upper bound of the color range in HSV.

    Returns:
        ndarray: Binary mask where pixels within the color range are 255, others are 0.
    """
    return cv.inRange(hsv_img, lower_bound, upper_bound)


def filter_contours(mask: ndarray, min_area: int = 0) -> ndarray:
    """
    Filters contours in a binary mask based on their area.

    Parameters:
        mask (ndarray): Binary input mask.
        min_area (int, optional): Minimum contour area to keep. Defaults to 0.

    Returns:
        ndarray: Filtered binary mask with contours of area >= min_area.
    """
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Create empty mask
    filtered_mask = np.zeros_like(mask)

    # Filter by area and preserve structure
    for contour in contours:
        area = cv.contourArea(contour)
        if area >= min_area:
            # Create mask for this specific contour
            temp_mask = np.zeros_like(mask)
            cv.drawContours(temp_mask, [contour], -1, (255), -1)

            # Preserve original pixels within outline
            contour_region = cv.bitwise_and(mask, temp_mask)
            filtered_mask = cv.bitwise_or(filtered_mask, contour_region)

    return filtered_mask


def apply_region_growing(
    filtered_mask: ndarray, hsv_img: ndarray, growth_conditions: dict
) -> ndarray:
    """
    Applies region growing algorithm to a binary mask based on HSV color conditions.
    Supports both normal ranges and circular ranges for the H component.

    Parameters:
        filtered_mask (ndarray): Initial binary mask for starting the region growing.
        hsv_img (ndarray): Input image in HSV color space.
        growth_conditions (dict): Dictionary with h_type, h_range, s_range, v_range defining the
                                acceptable ranges for region growing.

    Returns:
        ndarray: Binary mask after region growing.
    """
    # A region growing mask is created. Initially, it contains the extraction
    region_mask = np.zeros_like(filtered_mask, dtype=np.uint8)
    region_mask[filtered_mask == 255] = 255

    # Queue for region growing
    queue = collections.deque()

    # Add initial pixels from extraction
    indexes = np.column_stack(np.where(filtered_mask == 255))
    for index in indexes:
        queue.append(tuple(index))

    # Unpack growth conditions
    h_type = growth_conditions["h_type"]
    h_range = growth_conditions["h_range"]
    s_range = growth_conditions["s_range"]
    v_range = growth_conditions["v_range"]

    # Define boundary condition for region growing, with support for circular H ranges
    def fulfill_condition(H, S, V):
        # Check S and V ranges (always normal ranges)
        s_condition = s_range[0] <= S <= s_range[1]
        v_condition = v_range[0] <= V <= v_range[1]

        # Check H range depending on the type
        if h_type == "normal":
            # Normal continuous range
            h_condition = h_range[0] <= H <= h_range[1]
        elif h_type == "circular":
            # Circular range that crosses 0/180
            if h_range[0] > h_range[1]:  # Example: 151 to 18
                h_condition = (H >= h_range[0]) or (H <= h_range[1])
            else:
                h_condition = h_range[0] <= H <= h_range[1]
        else:
            h_condition = False

        return h_condition and s_condition and v_condition

    # Perform region growing
    while queue:
        i, j = queue.popleft()
        # For 8 Neighbors
        for di, dj in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            ni, nj = i + di, j + dj
            # Check that the neighbor is within the image
            if 0 <= ni < hsv_img.shape[0] and 0 <= nj < hsv_img.shape[1]:
                # If the neighbor is not yet part of the growth region
                if region_mask[ni, nj] == 0:
                    H, S, V = hsv_img[ni, nj]
                    if fulfill_condition(H, S, V):
                        region_mask[ni, nj] = 255
                        queue.append((ni, nj))

    return region_mask


def apply_morphology(
    mask: ndarray, kernel_size: tuple = (2, 2), operation: int = cv.MORPH_CLOSE
) -> ndarray:
    """
    Applies morphological operations to a binary mask.

    Parameters:
        mask (ndarray): Binary input mask.
        kernel_size (tuple, optional): Size of the kernel for morphological operation.
        operation (int, optional): OpenCV morphological operation. Defaults to cv.MORPH_CLOSE.

    Returns:
        ndarray: Binary mask after morphological operation.
    """
    kernel = np.ones(kernel_size, np.uint8)
    return cv.morphologyEx(mask, operation, kernel)


def resize_binary_mask(mask: ndarray, target_size: tuple = (512, 512)) -> ndarray:
    """
    Resizes a mask to the target size and ensures it's binary.

    Parameters:
        mask (ndarray): Binary input mask.
        target_size (tuple, optional): Target size (width, height). Defaults to (512, 512).

    Returns:
        ndarray: Resized binary mask.
    """
    resized = cv.resize(mask, target_size, interpolation=cv.INTER_AREA)
    return np.where(resized > 0, 255, 0).astype(np.uint8)


def process_class_mask(
    hsv_img: ndarray, class_param: dict, target_size: tuple = (512, 512)
) -> ndarray:
    """
    Process a single class mask through the entire pipeline: extraction, filtering,
    region growing, morphology, and resizing.

    Parameters:
        hsv_img (ndarray): Input image in HSV color space.
        class_param (dict): Parameters for this class including color_limits, min_area, and growth_conditions.
        target_size (tuple, optional): Target size for the output mask. Defaults to (512, 512).

    Returns:
        ndarray: Processed binary mask for this class.
    """
    # Extract parameters
    lower_bound, upper_bound = class_param["color_limits"]
    min_area = class_param["min_area"]
    growth_conditions = class_param["growth_conditions"]
    kernel_size = class_param.get("kernel_size", (2, 2))

    # 1. Extract color mask
    color_mask = extract_color_mask(hsv_img, lower_bound, upper_bound)

    # 2. Filter contours with class-specific min_area
    filtered_mask = filter_contours(color_mask, min_area)

    # 3. Apply region growing with class-specific conditions
    region_mask = apply_region_growing(filtered_mask, hsv_img, growth_conditions)

    # 4. Apply morphological operations with class-specific kernel
    morphed_mask = apply_morphology(region_mask, kernel_size)

    # 5. Resize mask
    resized_mask = resize_binary_mask(morphed_mask, target_size)

    return resized_mask


def image_segmentation(
    filename: str, base_mask_folder: str, output_folder: str
) -> None:
    """
    Segments an image based on class-specific parameters, applies tailored processing
    for each class, and saves the resulting masks as a NumPy array.

    Parameters:
        filename (str): The name of the image file to be segmented, including its extension (e.g., "image1.jpg").
        base_mask_folder (str): The directory containing the mask images with the same base name as the input image.
        output_folder (str): The directory where the resulting NumPy array with the combined masks will be saved.

    Procedure:
        1. Extracts the base name of the image (without extension) to locate the corresponding mask file.
        2. Loads the mask image and converts it from BGR to HSV color space.
        3. For each class:
            a. Processes the class-specific mask with tailored parameters.
            b. Adds the processed mask to the collection.
        4. Concatenates all processed masks along the channel dimension.
        5. Saves the combined mask as a NumPy file (.npy) in the specified output folder.

    Returns:
        None. The function saves the combined mask directly to the output folder.
    """
    img_number = filename.split(".")[0]
    mask_path: str = os.path.join(base_mask_folder, f"{img_number}.png")

    # Load and Convert Images
    bgr_img: ndarray = cv.imread(mask_path, 1)

    if bgr_img is None:
        print(f"ERROR: Unable to read image {mask_path}")
        return

    hsv_img: ndarray = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)

    # Create and process masks for each class with class-specific parameters
    processed_masks: list[ndarray] = []

    for class_param in class_parameters:
        # Process the mask for this class with its specific parameters
        mask = process_class_mask(hsv_img, class_param)

        # Add new axis for each binary mask
        binary_mask = mask[..., np.newaxis]
        processed_masks.append(binary_mask)

    # Concatenate processed masks along the channel dimension Z
    combined_mask: ndarray = np.concatenate(processed_masks, axis=2)

    # Save combined mask as a NumPy file
    output_file: str = os.path.join(output_folder, f"{img_number}.npy")
    np.save(output_file, combined_mask)
