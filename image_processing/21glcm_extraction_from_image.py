import matplotlib.pyplot as plt
from utils.presentation import (
    display_side_by_side,
    show_image,
    show_rgb,
    show_hsv,
    show_lab,
    show_gray,
    show_ycrcb,
)
import cv2 as cv
from icecream import ic
from PIL import Image
import pydicom
import numpy as np
import skimage.feature as feature


img = cv.imread("image_processing/images/man.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Param:
# source image
# List of pixel pair distance offsets - here 1 in each direction
# List of pixel pair angles in radians
glcm = feature.graycomatrix(
    img, [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256
)

# Find the GLCM properties
contrast = feature.graycoprops(glcm, "contrast")
dissimilarity = feature.graycoprops(glcm, "dissimilarity")
homogeneity = feature.graycoprops(glcm, "homogeneity")
energy = feature.graycoprops(glcm, "energy")
correlation = feature.graycoprops(glcm, "correlation")
ASM = feature.graycoprops(glcm, "ASM")

print(
    "contrast:",
    contrast,
    "\ndissimilarity:",
    dissimilarity,
    "\nhomogeneity:",
    homogeneity,
    "\nenergy:",
    energy,
    "\ncorrelation:",
    correlation,
    "\nASM:",
    ASM,
)
