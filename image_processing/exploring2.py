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
from PIL import Image, ImageFilter
from utils.presentation import compare_image_filter
from utils.elapsed_time import Timer


with Timer():
    original = Image.open("image_processing/images/mammography.png").convert("L")
    # smoothing
    modified = original.copy()
    modified = modified.filter(ImageFilter.SMOOTH)
    # thresholding
    modified = modified.point(lambda x: 255 if x > 180 else 0)
    # erosion
    for _ in range(6):
        modified = modified.filter(ImageFilter.MinFilter)
    # dilation
    for _ in range(6):
        modified = modified.filter(ImageFilter.MaxFilter)

    original = np.asarray(original)
    modified = np.asarray(modified)

    template = cv.bitwise_and(original, original, mask=modified)

    # Extract the sub image from the masked image
    x, y, w, h = cv.boundingRect(modified)
    subimg = template[y : y + h, x : x + w]

    # Apply template matching
    result = cv.matchTemplate(original, subimg, cv.TM_CCOEFF_NORMED)

    # Get the location of the template
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Define the coordinates of the red square
    top_left = max_loc
    bottom_right = (top_left[0] + subimg.shape[1], top_left[1] + subimg.shape[0])

    # Draw the red square on the image
    cv.rectangle(original, top_left, bottom_right, (0, 0, 255), 2)

    plt.imshow(original, cmap="gray")
    plt.show()
