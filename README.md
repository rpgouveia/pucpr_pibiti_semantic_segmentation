# pucpr_pibiti_semantic_segmentation
PIBITI - Development of Semantic Segmentation for the MetaTwinSynth Project

# First Steps
Please follow these steps to use this tool.

## Prerequisites
Make sure you have the following prerequisites installed in your environment:
- Python (version 3.12.4 or superior): [Download Python](https://www.python.org/downloads/)
- Anaconda 3: [Download Anaconda](https://www.anaconda.com/download)
- Images and Masks

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/rpgouveia/pucpr_pibic_semantic_segmentation.git
    ```
2. Navigate to the root directory.
3. Use anaconda to create a new environment using the environment.yml:
    ```bash
    conda env create -f environment.yml
    ```
4. Activate the environment to use the tool:
    ```bash
    conda activate opencv-env
    ```

## Setup
1. Create a .env file using the .env.example;
2. Type the path for base_img_folder, base_mask_folder and output_folder at .env file.
