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

    modified = normalize(modified)

    height, width = modified.shape

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
    mask = np.zeros((height, width), dtype=np.uint8)
    cv.drawContours(mask, [big_contour], 0, 255, cv.FILLED)

    modified = cv.bitwise_and(original, original, mask=mask)

    kernel_size = (5, 5)
    modified = cv.GaussianBlur(modified, kernel_size, 0)

    # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
    # Convert to float type only for supporting cv.kmeans
    pixel_vals = modified.flatten().astype(np.float32)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 3  # Choosing number of clusters
    compactness, labels, centers = cv.kmeans(
        pixel_vals, k, None, criteria, 10, cv.KMEANS_PP_CENTERS
    )

    centers = np.uint8(centers)

    # Reshape the labels to match the image shape
    labels = labels.flatten()

    # Retrieve the segmented image by assigning each pixel to its corresponding cluster center
    segmented_image = centers[labels]

    # Reshape the segmented image to the original image shape
    segmented_image = segmented_image.reshape(original.shape)

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

    # mark roi with colormap
    modified = modified.astype(np.uint8)

    roi = cv.bitwise_and(original, original, mask=modified)

    roi = cv.applyColorMap(roi, cv.COLORMAP_HOT)
    original = cv.cvtColor(original, cv.COLOR_GRAY2BGR)

    ic(original.shape)
    ic(roi.shape)

    modified = cv.bitwise_or(original, roi)

    display_side_by_side(original, modified)
