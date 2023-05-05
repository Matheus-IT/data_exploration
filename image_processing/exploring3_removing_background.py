import pydicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
)
import cv2 as cv
from utils.image_normalization import normalize, denormalize
from icecream import ic
import numpy as np
from utils.elapsed_time import Timer


with Timer():
    # reading image
    original = cv.imread("image_processing/images/mammography2.png")
    original = cv.cvtColor(original, cv.COLOR_BGRA2GRAY)
    # original = cv.flip(original, 1)
    modified = original.copy()

    # # bottom right corner
    # x1 = int(0.9 * original.shape[0])
    # y1 = int(0.99 * original.shape[1])
    # # top right corner
    # x2 = int(0.9 * original.shape[0])
    # y2 = int(0.1 * original.shape[1])

    # thresh = (original[x1, y1] + original[x2, y2]) // 2

    kernel_size = (5, 5)
    modified = cv.GaussianBlur(modified, kernel_size, 0)

    # Convert the new image to binary
    ret, modified = cv.threshold(modified, 0, 255, cv.THRESH_OTSU)

    # erosion
    modified = cv.erode(modified, None, iterations=10)
    # dilation
    modified = cv.dilate(modified, None, iterations=10)

    # modified = cv.bitwise_and(original, original, mask=modified)

    plt.imshow(modified, cmap="gray")
    plt.show()
