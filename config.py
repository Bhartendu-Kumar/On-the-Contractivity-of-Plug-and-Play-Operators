import argparse
import importlib
import cv2

#denoiser
from denoisers import NLM
importlib.reload(NLM)
from denoisers.NLM import DSG_NLM

#hyperparameters--
noise_variance = 10.0/255.0
noise_mean = 0.0

step_size = 0.98
tolerance = 1e-3
max_iterations = 10 #100
iterations_to_fix_W = 0 #iterations to fix W# fixing W
power_method_max_iterations = 30
MAX_ITERS_CG = 100
CG_TOL = 1e-7
ADD_NOISE = False
calculate_contractive_factor = False

greayscale = True
#set opencv imread flag based on grayscale
if greayscale:
    imread_flag = cv2.IMREAD_GRAYSCALE
else:
    imread_flag = cv2.IMREAD_COLOR

#write a function to parse the arguments
def parse_args():
    #get the terminal arguments, argument parser
    parser = argparse.ArgumentParser()
    #store the arguments in variables
    parser.add_argument('--image_path', type=str, default='images/', help='path to the folder with the images')
    parser.add_argument('--output_path', type=str, default='results/', help='path to the folder where the results should be saved')
    parser.add_argument('--image_num', type=int, default=1, help='number of the image to be denoised: choose between 1 and 16')
    parser.add_argument('--initialization', type=str, default='median', help='initialization for the algorithm: median,  zero, ones, gaussian')
    parser.add_argument('--ITERATIVE_ALGORITHM', type=str, default='ISTA', help='iterative algorithm to be used')
    parser.add_argument('--INVERSE_PROBLEM', type=str, default='INPAINTING', help='inverse problem to be solved from : INPAINTING, SUPERRESOLUTION, UNIFORM-DEBLURRING, GAUSSIAN-DEBLURRING')
    #adding option for denoiser
    parser.add_argument('--denoiser', type=str, default='DSG_NLM', help='denoiser to be used: DSG_NLM, NLM')
    #return
    return parser.parse_args()