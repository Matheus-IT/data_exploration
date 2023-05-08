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
    modified = original.copy()

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

    modified = cv.bitwise_and(original, original, mask=mask)

    Image.fromarray(modified).show()
