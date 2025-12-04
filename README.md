# Semantic Segmentation for Urban Accessibility Using High-Fidelity Synthetic Data

[![Python](https://img.shields.io/badge/Python-3.12.4+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.17.0-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.10.0-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 Overview

This repository contains the implementation of semantic segmentation models for urban accessibility applications, focusing on the detection of mobility devices and accessibility infrastructure. The work is based on the research paper:

**"Enhancing Semantic Segmentation for Urban Accessibility Using High-Fidelity Synthetic Data"**  
*Luna-Romero, S.F., Gouveia, R., and Abreu de Souza, M.*

### Key Features

- **High-fidelity synthetic dataset (SYNTHUA-DT)**: 5,036 images with pixel-perfect annotations across 22 semantic classes
- **Focus on accessibility**: Explicit modeling of wheelchairs, walkers, canes, crutches, and urban infrastructure
- **State-of-the-art architectures**: Implementation of U-Net and DeepLabv3+ with custom preprocessing pipeline
- **Multiple loss functions**: BCE-Dice, Focal Loss, and Tversky Loss variants for class-imbalance handling
- **Comprehensive evaluation**: Global metrics (mIoU, precision, recall, F1-score) and per-class analysis

### Main Results

- **Global mIoU**: 0.84 (13.4× improvement over baseline U-Net)
- **All 22 classes** exceed deployment threshold (IoU ≥ 0.75)
- **Accessibility-critical classes**: Motorized wheelchairs (0.94 IoU), Sidewalks (0.78 IoU, 0.92 recall)
- **Calibration improvements**: 60% reduction in ECE and MCE after temperature scaling

---

## 📑 Table of Contents

- [Repository Structure](#️-repository-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Dataset](#-dataset)
- [Docker Setup (AMD GPU)](#-docker-setup-amd-gpu-with-rocm)
- [Usage](#-usage)
  - [Preprocessing Pipeline](#1-preprocessing-pipeline)
  - [Model Training](#2-model-training)
  - [Evaluation](#3-evaluation)
- [Experimental Results](#-experimental-results)
- [Citation](#-citation)
- [Related Publications](#-related-publications)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Additional Resources](#-additional-resources)

---

## 🗂️ Repository Structure

```
pucpr_pibiti_semantic_segmentation/
│
├── core/                           # Core processing modules
│   ├── __init__.py
│   ├── colors.py                   # Color encoding and class parameters (22 classes)
│   ├── image_manipulation.py       # Image processing and mask decomposition pipeline
│   ├── utils.py                    # Utility functions
│   └── validation.py               # Pipeline validation tools
│
├── tools/                          # Additional tools and scripts
│
├── deprecated/                     # Legacy code (archived)
│
├── study_color_conversion/         # Color space conversion experiments
├── study_img_reconstruction/       # Image reconstruction studies
├── study_tf/                       # TensorFlow model experiments
├── study_tf_models/                # Model architecture studies
│
├── logs_bce_dice_v3/               # Training logs: BCE-Dice loss v3
├── logs_bce_dice_v4/               # Training logs: BCE-Dice loss v4
├── logs_focal_v1/                  # Training logs: Focal loss v1
├── logs_focal_v2/                  # Training logs: Focal loss v2
├── logs_tversky_v5/                # Training logs: Tversky loss v5
│
├── results_unet_multilabel/        # U-Net baseline results
├── master_class/                   # Final model implementations
│
├── main.py                         # Main preprocessing script
├── environment.yml                 # Conda environment (OpenCV)
├── tf-cpu.yml                      # Conda environment (TensorFlow CPU)
├── .env.example                    # Environment configuration template
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.12.4+**: [Download Python](https://www.python.org/downloads/)
- **Anaconda 3**: [Download Anaconda](https://www.anaconda.com/download)
- **SYNTHUA-DT Dataset**: RGB images and semantic masks (see [Dataset](#-dataset) section)

> **Note**: For AMD Radeon GPU users, see the [Docker Setup](#-docker-setup-amd-gpu-with-rocm) section for GPU-accelerated training.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rpgouveia/pucpr_pibiti_semantic_segmentation.git
   cd pucpr_pibiti_semantic_segmentation
   ```

2. **Create the preprocessing environment** (OpenCV):
   ```bash
   conda env create -f environment.yml
   conda activate opencv-env
   ```

3. **Create the training environment** (TensorFlow):
   ```bash
   conda env create -f tf-cpu.yml
   conda activate tf-cpu
   ```

> **Choosing between Conda and Docker:**
> - **Conda** (`tf-cpu.yml`): Best for CPU-only training or NVIDIA GPUs with CUDA
> - **Docker + ROCm**: Required for AMD Radeon GPU acceleration
> - Both environments support the same training scripts and notebooks

### Configuration

1. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file** with your dataset paths:
   ```env
   BASE_IMG_FOLDER=/path/to/your/rgb/images
   BASE_MASK_FOLDER=/path/to/your/semantic/masks
   OUTPUT_FOLDER=/path/to/processed/output
   NUMPY_FOLDER=/path/to/numpy/tensors
   ```

---

## 📊 Dataset

### SYNTHUA-DT (Synthetic Urban Accessibility – Digital Twin)

The SYNTHUA-DT dataset was generated using Unreal Engine 5.1 and contains:

- **5,036 high-resolution images** (1920×1080 px, downsampled to 512×512 px for training)
- **22 semantic classes** with pixel-perfect ground-truth annotations
- **Domain randomization**: Varied illumination, weather, camera parameters, and textures
- **Focus on accessibility**: Multiple mobility device categories and sidewalk-level infrastructure

#### Semantic Classes (22 total)

| Category | Classes |
|----------|---------|
| **Building** | Buildings |
| **Mobility Devices** | Motorized Wheelchair, Wheelchair, Walker, Cane, Orthopedic Cane, Crutch, Orthopedic Crutch |
| **Nature** | Grass, Tree/Plants |
| **Passerby** | Humans, Dogs |
| **Street Furniture** | Benches, Trash Cans, Bollards, Advertising Panels, Tourist Spots, Monuments |
| **Transport** | Cars, Buses, Bikes, Motorcycles, Scooters |
| **Urban Infrastructure** | Streets, Sidewalks, Street Light Poles, Traffic Light Poles, Signposts |

For more details, see:
- Luna-Romero, S.F., Abreu de Souza, M., & Serpa Andrade, L. (2025). "SYNTHUA-DT: a methodological framework for synthetic dataset generation and automatic annotation from digital twins in urban accessibility applications." *Technologies*, 13(8), 359.

---

## 🐳 Docker Setup (AMD GPU with ROCm)

For users with AMD Radeon GPUs, Docker with ROCm provides GPU acceleration for TensorFlow training.

### Prerequisites
- AMD Radeon GPU with ROCm support
- Docker installed and configured
- ROCm drivers installed on host system

### Pull the TensorFlow ROCm Image

```bash
docker pull rocm/tensorflow:latest
```

### Run the Container with GPU Access

**Basic command** (without volume mounts):
```bash
docker run -it --network=host --device=/dev/kfd --device=/dev/dri \
  --ipc=host --shm-size 16G --group-add video --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined rocm/tensorflow:latest
```

**With project directories mounted**:
```bash
docker run -it --network=host --device=/dev/kfd --device=/dev/dri \
  --ipc=host --shm-size 16G --group-add video --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  -v /path/to/pucpr_pibit_semantic_segmentation:/workspace \
  -v /path/to/NumpyFiles:/data/numpy \
  -v /path/to/Images:/data/images \
  rocm/tensorflow:latest
```

**Parameters explained**:
- `--device=/dev/kfd --device=/dev/dri`: GPU device access
- `--shm-size 16G`: Shared memory for data loading
- `--group-add video`: Video group permissions
- `-v <host_path>:<container_path>`: Mount directories from host to container

### Setup Jupyter Notebook in Container

Once inside the container, install Jupyter and required packages:

```bash
# Install Jupyter and dependencies
pip install jupyter ipykernel matplotlib python-dotenv seaborn scikit-learn

# Register the kernel
python -m ipykernel install --name tf-docker

# Verify kernel installation
jupyter kernelspec list
```

### Launch Jupyter Notebook

```bash
# Navigate to workspace
cd /workspace

# Start Jupyter server
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

The terminal will display an access URL like:
```
http://127.0.0.1:8888/tree?token=YOUR_GENERATED_TOKEN_HERE
```

Copy this URL to your browser to access Jupyter Notebook with GPU acceleration.

### Verify GPU Access

In a Jupyter notebook, run:
```python
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.config.list_physical_devices('GPU'))
```

### Troubleshooting

**GPU not detected?**
1. Verify ROCm installation on host: `rocm-smi`
2. Check Docker has access to GPU devices: `ls -la /dev/kfd /dev/dri`
3. Ensure your GPU is supported by ROCm: [ROCm GPU Support](https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html)

**Out of memory errors?**
- Reduce batch size in training scripts
- Increase `--shm-size` parameter (e.g., `--shm-size 32G`)

**Jupyter connection issues?**
- Ensure port 8888 is not blocked by firewall
- Try using `--ip=127.0.0.1` instead of `0.0.0.0`

---

## 🔧 Usage

### 1. Preprocessing Pipeline

The preprocessing pipeline converts color-coded semantic masks into multi-channel binary tensors suitable for model training.

**Activate the OpenCV environment**:
```bash
conda activate opencv-env
```

**Run the main preprocessing script**:
```bash
python main.py
```

This script performs:
- **HSV-based color extraction** with class-specific thresholds
- **Region growing** with circular hue support (for red-spectrum classes)
- **Morphological operations** (closing, opening, dilation, erosion)
- **Contour filtering** by minimum area
- **Multi-channel mask generation** (512×512×22 tensors)

**Validate the pipeline** (single image test):
```python
from core.validation import validate_segmentation_pipeline
validate_segmentation_pipeline(base_mask_folder, output_folder)
```

### 2. Model Training

Training scripts are located in the `master_class/` and `study_tf_models/` directories. Example workflow:

**Activate the TensorFlow environment**:
```bash
conda activate tf-cpu
```

**Train DeepLabv3+ with BCE-Dice loss**:
```bash
python master_class/train_deeplabv3plus.py --loss bce_dice --epochs 100 --batch_size 8
```

**Available loss functions**:
- `bce_dice`: Binary Cross-Entropy + Soft Dice Loss (default)
- `focal`: Focal Loss (γ=2) + Soft Dice Loss
- `tversky`: Tversky Loss (α=0.3, β=0.7) + Soft Dice Loss

**Monitor training with TensorBoard**:
```bash
tensorboard --logdir logs_bce_dice_v4/
```

### 3. Evaluation

Results are saved in the respective `logs_*` directories with:
- Training/validation loss curves
- Per-class IoU, precision, recall, F1-score
- Confusion matrices
- Calibration metrics (ECE, MCE, NLL, Brier score)

---

## 📈 Experimental Results

### Global Performance (DeepLabv3+ vs. U-Net)

| Model | mIoU | Precision | Recall | F1-Score |
|-------|------|-----------|--------|----------|
| **U-Net (baseline)** | 0.0626 | 0.1328 | 0.0985 | 0.0872 |
| **DeepLabv3+ (synthetic pretraining)** | **0.8400** | **0.9085** | **0.9145** | **0.9106** |

**Improvements**: 13.4× mIoU, 6.8× precision, 9.3× recall, 10.4× F1-score

### Per-Class Performance (DeepLabv3+)

Selected accessibility-critical classes:

| Class | IoU | Precision | Recall | F1-Score |
|-------|-----|-----------|--------|----------|
| **Motorized Wheelchair** | 0.940 | 0.898 | 0.936 | 0.916 |
| **Wheelchair** | 0.781 | 0.876 | 0.921 | 0.898 |
| **Walker** | 0.870 | 0.952 | 0.918 | 0.935 |
| **Cane** | 0.762 | 0.927 | 0.976 | 0.951 |
| **Sidewalks** | 0.778 | 0.968 | 0.921 | 0.944 |
| **Streets** | 0.836 | 0.866 | 0.958 | 0.909 |

**All 22 classes achieved IoU ≥ 0.75** (deployment-ready threshold).

### Calibration Metrics (DeepLabv3+)

| Setting | ECE (%) | MCE (%) | NLL | Brier |
|---------|---------|---------|-----|-------|
| **Pre-calibration** | 8.5 ± 0.7 | 23.1 ± 1.9 | 0.693 ± 0.018 | 0.162 ± 0.004 |
| **Temperature scaling** | **3.3 ± 0.5** | **9.8 ± 1.3** | **0.612 ± 0.015** | **0.148 ± 0.003** |

**Improvements**: 61% reduction in ECE, 58% reduction in MCE

---

## 📄 Citation

If you use this code or dataset in your research, please cite:

```bibtex
@article{LunaRomero2025Semantic,
  author  = {Luna-Romero, Santiago Felipe and Gouveia, Renato and Abreu de Souza, Mauren},
  title   = {Enhancing Semantic Segmentation for Urban Accessibility Using High-Fidelity Synthetic Data},
  journal = {Ingenius - Revista de Ciencia y Tecnología},
  year    = {2025},
  volume  = {},
  pages   = {1--16},
  note    = {In press}
}

@article{romero2025synthua,
  author  = {Luna-Romero, Santiago Felipe and Abreu de Souza, Mauren and Serpa Andrade, Leonardo},
  title   = {{SYNTHUA-DT}: a methodological framework for synthetic dataset generation and automatic annotation from digital twins in urban accessibility applications},
  journal = {Technologies},
  year    = {2025},
  volume  = {13},
  number  = {8},
  pages   = {359},
  doi     = {10.3390/technologies13080359}
}
```

---

## 🔬 Related Publications

1. Luna-Romero, S.F., Abreu de Souza, M., & Serpa Andrade, L. (2025). "Artificial vision systems for mobility impairment detection: integrating synthetic data, ethical considerations, and real-world applications." *Technologies*, 13(5), 198.

2. Luna-Romero, S.F., Stempniak, C.R., Abreu de Souza, M., & Reynoso-Meza, G. (2023). "Urban digital twins for synthetic data of individuals with mobility aids in Curitiba, Brazil, to drive highly accurate AI models for inclusivity." In *International Conference on Science, Technology and Innovation for Society* (pp. 116–125). Springer.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

### Areas for Future Work

- Domain adaptation techniques for sim-to-real transfer
- Real-world dataset collection and evaluation
- Boundary-aware loss functions for improved curb detection
- Multi-task architectures (segmentation + depth estimation)
- Lightweight models for real-time inference
- Uncertainty quantification (Bayesian ensembling, Monte Carlo dropout)

---

## 📧 Contact

**Santiago Felipe Luna Romero**  
- Email: [santiago.romero@pucpr.br](mailto:santiago.romero@pucpr.br)

**Renato Pestana de Gouveia**
- Email: [gouveia.renato@pucpr.edu.br](mailto:gouveia.renato@pucpr.edu.br)
- GitHub: [@rpgouveia](https://github.com/rpgouveia)

**Mauren Abreu de Souza**  
- Email: [mauren.souza@pucpr.br](mailto:mauren.souza@pucpr.br)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **PUCPR** (Pontifícia Universidade Católica do Paraná) for institutional support
- **PIBITI** program for funding this research
- **SYNTHUA-DT** dataset generation team
- **AMD ROCm** for GPU acceleration support on AMD Radeon hardware
- All contributors and reviewers

---

## 📚 Additional Resources

- **Unreal Engine 5.1**: [https://www.unrealengine.com/](https://www.unrealengine.com/)
- **AMD ROCm Platform**: [https://www.amd.com/en/products/software/rocm.html](https://www.amd.com/en/products/software/rocm.html)
- **ROCm TensorFlow Docker**: [https://hub.docker.com/r/rocm/tensorflow](https://hub.docker.com/r/rocm/tensorflow)
- **DeepLabv3+ paper**: Chen et al. (2018). "Encoder-decoder with atrous separable convolution for semantic image segmentation"
- **U-Net paper**: Ronneberger et al. (2015). "U-Net: convolutional networks for biomedical image segmentation"

---

**Last updated**: December 2025