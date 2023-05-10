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
    original = pydicom.dcmread(
        "image_processing/images/dicom/mammography2.dcm"
    ).pixel_array

    modified = normalize(original)

    h, w = modified.shape
    modified = modified.copy()

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

    kernel_size = (7, 7)
    modified = cv.GaussianBlur(modified, kernel_size, 0)

    # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
    # Convert to float type only for supporting cv.kmeans
    pixel_vals = modified.flatten().astype(np.float32)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 5  # Choosing number of clusters
    retval, labels, centers = cv.kmeans(
        pixel_vals, k, None, criteria, 10, cv.KMEANS_PP_CENTERS
    )

    centers = np.array(centers, dtype=np.uint8)

    ic(np.unique(labels))
    ic(centers)
    ic(retval)

    # Find the cluster with the highest intensity value
    centers_max = np.max(centers, axis=1)
    highest_intensity_cluster_idx = np.argsort(centers_max)[-1]

    # Extract the pixels belonging to the highest intensity cluster
    highest_intensity_pixels = pixel_vals[
        np.where(labels == highest_intensity_cluster_idx)[0]
    ]

    # Create a new image containing just the higher intensity pixels
    img_high_intensity = np.zeros_like(pixel_vals)
    img_high_intensity[
        np.where(labels == highest_intensity_cluster_idx)[0]
    ] = highest_intensity_pixels
    img_high_intensity = img_high_intensity.reshape(modified.shape)

    # Convert the new image to binary
    ret, modified = cv.threshold(img_high_intensity, 0, 255, cv.THRESH_BINARY)

    modified = cv.erode(modified, None, iterations=5)
    modified = cv.dilate(modified, None, iterations=5)

    modified = modified.astype(np.uint8)

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

    original = cv.cvtColor(original, cv.COLOR_GRAY2BGR)

    # Draw the red square on the image
    cv.rectangle(original, top_left, bottom_right, (0, 0, 255), 2)

    plt.imshow(original, cmap="gray")
    plt.show()
