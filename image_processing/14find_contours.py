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
    original = cv.imread("image_processing/images/example.PNG")

    modified = original.copy()

    modified = cv.cvtColor(modified, cv.COLOR_BGR2GRAY)

    ret, modified = cv.threshold(modified, 0, 255, cv.THRESH_BINARY)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    modified = cv.erode(modified, kernel, iterations=10)
    modified = cv.dilate(modified, kernel, iterations=10)

    contours, hierarchy = cv.findContours(
        modified, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )
    modified = cv.drawContours(original, contours, -1, (255, 0, 0), 2)
    # largest_contour = max(contours[0], key=cv.contourArea)
    # modified = cv.drawContours(original, [largest_contour], -1, (255, 0, 0), 2)

    Image.fromarray(modified).show()
