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
    modified = original.copy()

    # Convert the new image to binary
    ret, modified = cv.threshold(original, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # erosion
    modified = cv.erode(modified, None, iterations=25)
    # dilation
    modified = cv.dilate(modified, None, iterations=25)

    modified = cv.bitwise_and(original, original, mask=modified)

    # # smoothing
    # modified = original.copy()
    # kernel_size = (5, 5)
    # modified = cv.GaussianBlur(modified, kernel_size, 0)

    # # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
    # # Convert to float type only for supporting cv.kmeans
    # pixel_vals = modified.flatten().astype(np.float32)

    # criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # k = 3  # Choosing number of clusters
    # retval, labels, centers = cv.kmeans(
    #     pixel_vals, k, None, criteria, 10, cv.KMEANS_PP_CENTERS
    # )

    # # centers = np.array(centers, dtype=np.uint8)

    # # Find the cluster with the highest intensity value
    # centers_max = np.max(centers, axis=1)
    # highest_intensity_cluster_idx = np.argsort(centers_max)[-1]

    # # Extract the pixels belonging to the highest intensity cluster
    # highest_intensity_pixels = pixel_vals[
    #     np.where(labels == highest_intensity_cluster_idx)[0]
    # ]

    # # Create a new image containing just the higher intensity pixels
    # img_high_intensity = np.zeros_like(pixel_vals)
    # img_high_intensity[
    #     np.where(labels == highest_intensity_cluster_idx)[0]
    # ] = highest_intensity_pixels
    # img_high_intensity = img_high_intensity.reshape(modified.shape)

    # # Convert the new image to binary
    # ret, modified = cv.threshold(img_high_intensity, 0, 255, cv.THRESH_BINARY)

    # # erosion
    # modified = cv.erode(modified, None, iterations=12)
    # # dilation
    # modified = cv.dilate(modified, None, iterations=12)

    # modified = modified.astype(np.uint8)

    # template = cv.bitwise_and(original, original, mask=modified)

    # # Extract the sub image from the masked image
    # x, y, w, h = cv.boundingRect(modified)
    # subimg = template[y : y + h, x : x + w]

    # # Apply template matching
    # result = cv.matchTemplate(original, subimg, cv.TM_CCOEFF_NORMED)

    # # Get the location of the template
    # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # # Define the coordinates of the red square
    # top_left = max_loc
    # bottom_right = (top_left[0] + subimg.shape[1], top_left[1] + subimg.shape[0])

    # # Draw the red square on the image
    # cv.rectangle(original, top_left, bottom_right, (0, 0, 255), 2)

    plt.imshow(modified, cmap="gray")
    plt.show()
