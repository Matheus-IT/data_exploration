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
from PIL import Image


with Timer():
    # reading image
    original = cv.imread("image_processing/images/mammography2.png")
    original = cv.cvtColor(original, cv.COLOR_BGRA2GRAY)
    h, w = original.shape
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

    # opening morphological operation
    modified = cv.erode(modified, None, iterations=10)
    modified = cv.dilate(modified, None, iterations=10)

    # dilate mask to fill in the gaps
    modified = cv.dilate(modified, None, iterations=10)

    # get largest contour
    contours = cv.findContours(modified, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    big_contour = max(contours, key=cv.contourArea)

    # draw largest contour as white filled on black background as mask
    mask = np.zeros((h, w), dtype=np.uint8)
    cv.drawContours(mask, [big_contour], 0, 255, cv.FILLED)

    # trying adaptive threshold
    # modified = cv.adaptiveThreshold(
    #     modified, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 3
    # )

    # trying out some morphological operations
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # modified = cv.morphologyEx(modified, cv.MORPH_TOPHAT, kernel)
    # modified = cv.morphologyEx(modified, cv.MORPH_BLACKHAT, kernel)

    modified = cv.bitwise_and(original, original, mask=mask)

    Image.fromarray(modified).show()
