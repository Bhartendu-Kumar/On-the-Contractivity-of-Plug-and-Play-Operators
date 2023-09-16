# On-the-Contractivity-of-Plug-and-Play-Operators

#### This repository contains codes for the SPL paper: On the Contractivity of Plug-and-Play Operators

## 📄 Table of Contents

- [Directory Structure](#-directory-structure)
- [Prerequisites](#-prerequisites)
- [Setup](#-setup)
- [Running the Main Script](#-running-the-main-script)
- [Helper Scripts](#-helper-scripts)
- [Citation](#-citation)
- [Contact](#-contact)

## 📂 Directory Structure



```
On-the-Contractivity-of-Plug-and-Play-Operators/
│
├── images/                # Directory containing test images
│   ├── 1.png              # Sample images
│   ├── ...                # 12 images are from Set12
│   └── 16.png
│
├── denoisers/             # Denoisers scripts and utilities
│   ├── GMM_denoiser/      # GMM denoiser directory (details/contents not provided)
│   ├── bm3d_denoiser.py   # BM3D denoising algorithm
│   ├── mlp_denoiser.py    # MLP denoising algorithm
│   └── utility.py         # Utility functions for denoisers
│
├── results/               # Directory to save results
│
├── forward_models.py     # Script containing forward models
├── iterative_algorithms.py  # Script with iterative algorithms implementations
├── NLM.py                # Non-Local Means denoising implementation
├── main.py               # Main script to run the demo
└── utils.py              # General utility functions
└── config.py             # Experiment configuration and parameters

```

## 🛠 Prerequisites

- **Operating System**: Recommended: *Linux Ubuntu 20.04*
- **Python**: Version 3.8 or higher
- **Dependencies**: All required Python libraries are listed in `requirements.txt`

## 🚀 Setup


1. **Clone the Repository**:
   ```
   git clone https://github.com/Bhartendu-Kumar/On-the-Contractivity-of-Plug-and-Play-Operators.git
   ```
2. 🌐 Set Up a Virtual Environment (recommended)
```
cd On-the-Contractivity-of-Plug-and-Play-Operators
python3 -m venv venv
source venv/bin/activate
```
3. 📦 Install Dependencies
```
pip install -r requirements.txt
```
## 🎯 Running the Main Script

The `main.py` script is the primary entry point to run the demo. You can customize the execution using various command-line arguments.

### Arguments:

- `--image_path`: Path to the folder containing the images.  
  **Default**: `'images/'`
  
- `--output_path`: Path to the folder where the denoised results should be saved.  
  **Default**: `'results/'`
  
- `--image_num`: Specifies the number of the image to be denoised.  
  **Default**: `1`
  
- `--initialization`: The initialization method for the algorithm.  
  **Default**: `'median'`
  
- `--ITERATIVE_ALGORITHM`: The iterative algorithm to be employed for denoising.  
  **Default**: `'ISTA'`
  
- `--INVERSE_PROBLEM`: Specifies the inverse problem to solve.  
  **Default**: `'INPAINTING'`

### Example:

To run the `main.py` script using the default settings:

```
python3 main.py
```
## 🛠 Helper Scripts

This section provides a brief overview of the helper scripts included in the repository:

1. **config.py**:  
   Contains configurations required to run the demo and other scripts.

2. **forward_models.py**:  
   Implements various forward models:
   - Inpainting
   - Deblurring:
     - Uniform
     - Gaussian
   - Superresolution

3. **iterative_algorithms.py**:  
   Contains the implementations of:
   - ISTA
   - ADMM

4. **NLM.py**:  
   Provides the Non-Local Means (NLM) denoising method.

5. **contractive_factor.py**:  
   Contains the code to compute the contraction factor of operators \(P\) and \(R\) (refer to the paper) using power methods.

## 📝 Citation

If you find our work useful and wish to cite it, please use the following BibTeX:

```
@article{kumar2023contractivity,
    title={On the Contractivity of Plug-and-Play Operators},
    author={Kumar, Bhartendu and Chaudhury, Kunal N.},
    journal={IEEE Signal Processing Letters},
    year={2023},
    volume={xx},
    number={x},
    pages={xxx-xxx},
    doi={xx.xxxxx/xxxxx}
}
```
