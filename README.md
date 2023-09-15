# On-the-Contractivity-of-Plug-and-Play-Operators

#### This repository contains codes for the SPL paper: On the Contractivity of Plug-and-Play Operators

## 📄 Table of Contents

- [Directory Structure](#-directory-structure)
- [Prerequisites](#-prerequisites)
- [Setup](#-setup)
- [Running the Main Script](#-running-the-main-script)
- [Helper Scripts](#-helper-scripts)
- [Results](#-results)
- [Citation](#-citation)
- [Contact](#-contact)

## 📂 Directory Structure



On-the-Contractivity-of-Plug-and-Play-Operators/
│
├── images/ # Directory containing test images
│ ├── 1.png # Sample image
│ ├── ... # Other images
│ └── 16.png
│
├── denoisers/ # Denoisers scripts and utilities
│ ├── GMM_denoiser/ # GMM denoiser directory (details/contents not provided)
│ ├── bm3d_denoiser.py # BM3D denoising algorithm
│ ├── mlp_denoiser.py # MLP denoising algorithm
│ └── utility.py # Utility functions for denoisers
│
├── results/ # Directory to save results
│
├── forward_models.py # Script containing forward models
├── iterative_algorithms.py # Script with iterative algorithms implementations
├── NLM.py # Non-Local Means denoising implementation
├── main.py # Main script to run the demo
└── utils.py # General utility functions
