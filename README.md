# On-the-Contractivity-of-Plug-and-Play-Operators

#### This repository contains codes for the SPL paper: On the Contractivity of Plug-and-Play Operators
---

This repository is solving linear inverse problems in image processing. At its core, a linear inverse problem aims to reconstruct an image that might contain corrupted or unobserved pixels. Our repository provides solutions for three primary reconstruction techniques:

1. **Image Inpainting**: In this scenario, a subset of the image's pixels is unobserved. The challenge is to reconstruct the entire image, including these unobserved pixels.
   
2. **Superresolution**: Here, the input is a downscaled version of the original image. The goal is to reconstruct the image back to its original resolution.
   
3. **Deblurring (Uniform and Gaussian)**: The objective of this method is to counteract the blur effect in an image, bringing back its original clarity and sharpness.

A cornerstone of the reconstruction methodology is the PnP-ISTA (Plug-and-play Iterative Shrinkage Thresholding Algorithm). ISTA due to Beck and Teboulle[^beck2009fast^] and ADMM by Boyd et.al [^admm^] as iterative algorithms for image reconstructions. Sreehari et al.[^sreehari2016plug^] showed using a powerful denoiser for ISTA/ADMM, i.e. PnP-ISTA/PnP-ADMM, are particularly effective for reconstructions. In our implementation, we've adopted the Non-Local Means denoiser (NLM) denoiser in PnP-ISTA/PnP-ADMM to get the reconstructions. These codes are for :
- Image reconstruction and computes the iterates of ISTA and ADMM.

- The contractivity of relevant operators, symbolized as \(P\) and \(R\) (as detailed in our paper).
   
- Changing to different initializations converges to the same reconstruction in both ISTA and ADMM.

---




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
│   ├── NLM.py                # Non-Local Means denoising implementation
│   ├── GMM_denoiser/      # GMM denoiser directory (details/contents not provided)
│   ├── bm3d_denoiser.py   # BM3D denoising algorithm
│   └── utility.py         # Utility functions for denoisers
│
├── results/               # Directory to save results
│
├── forward_models.py     # Script containing forward models
├── iterative_algorithms.py  # Script with iterative algorithms implementations
├── contractive_factor.py # To compute the contractive factors using the power method
├── main.py               # Main script to run the demo
├── utils.py              # General utility functions
├── config.py             # Experiment configuration and parameters
└── requirements.txt      # Install the libraries required
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
### References:

[^beck2009fast^]: Beck, A., & Teboulle, M. (2009). A fast iterative shrinkage-thresholding algorithm for linear inverse problems. SIAM journal on imaging sciences, 2(1), 183-202.
[^admm^]: Boyd, Stephen, et al. "Distributed optimization and statistical learning via the alternating direction method of multipliers." Foundations and Trends® in Machine learning 3.1 (2011): 1-122.

[^sreehari2016plug^]: Sreehari, S., Venkatakrishnan, S. V., Wohlberg, B., Buzzard, G. T., Drummy, L. F., Simmons, J. P., & Bouman, C. A. (2016). Plug-and-play priors for bright field electron tomography and sparse interpolation. IEEE Transactions on Computational Imaging, 2(4), 408-423.
