import pydicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
    display_side_by_side,
)
from utils.segmentation import get_high_intensity_cluster_kmeans
from utils.filters import opening_filter, closing_filter, high_pass_filter
import cv2 as cv
from utils.image_normalization import normalize, denormalize
from icecream import ic
import numpy as np
from utils.elapsed_time import Timer
from PIL import Image


with Timer():
    MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography-dataset/nbia/CMMD/D2-0001/07-18-2011-NA-NA-75485/1.000000-NA-12786/"
    original = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm").pixel_array

    modified = original.copy()

    # Normalizing image
    modified = normalize(modified)

    # Segmenting breast tissue
    kernel_size = (5, 5)
    modified = cv.GaussianBlur(modified, kernel_size, 0)

    # Convert the new image to binary
    ret, modified = cv.threshold(modified, 0, 255, cv.THRESH_OTSU)

    # get largest contour
    contours, hierarchy = cv.findContours(
        modified, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )
    big_contour = max(contours, key=cv.contourArea)

    # draw largest contour as white filled on black background as mask
    height, width = modified.shape
    mask = np.zeros((height, width), dtype=np.uint8)
    cv.drawContours(mask, [big_contour], 0, 255, cv.FILLED)

    modified = cv.bitwise_and(original, original, mask=mask)

    # Apply high pass filter
    modified = high_pass_filter(modified)

    # get the high intensity cluster using kmeans
    modified = get_high_intensity_cluster_kmeans(modified)

    # Convert the new image to binary
    ret, modified = cv.threshold(modified, 0, 255, cv.THRESH_BINARY)

    modified = modified.astype(np.uint8)

    roi = cv.bitwise_and(original, original, mask=modified)

    # Perform a morphological opening filter
    roi = closing_filter(roi)
    roi = opening_filter(roi, 3)

    # Detect contours of artifacts
    roi = cv.Canny(roi, 150, 200)
    # increase thickness
    roi = cv.dilate(roi, None, iterations=1)

    # Painting roi fragments in red
    roi = cv.cvtColor(roi, cv.COLOR_GRAY2BGR)
    # Set the red channel values to 255
    blue_channel = roi[:, :, 0]  # Extract the blue channel (channel index 0)
    green_channel = roi[:, :, 1]  # Extract the green channel (channel index 1)
    roi[0] = 255  # set red channel to maximum
    roi[green_channel > 0, 1] = 0  # Set green channel values to 0
    roi[blue_channel > 0, 2] = 0  # Set blue channel values to 0

    original = cv.cvtColor(original, cv.COLOR_GRAY2BGR)

    # Mark roi in original image
    modified = cv.bitwise_or(original, roi)

    display_side_by_side(original, modified)
