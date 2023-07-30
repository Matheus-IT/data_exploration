import cv2 as cv
import numpy as np
from utils.filters import opening_filter, closing_filter, get_circular_kernel


def segment_breast_tissue(image, original_image):
    image = cv.GaussianBlur(image, (5, 5), 0)

    # Convert the new image to binary
    ret, image = cv.threshold(image, 0, 255, cv.THRESH_OTSU)

    # get largest contour
    contours, hierarchy = cv.findContours(
        image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )
    big_contour = max(contours, key=cv.contourArea)

    # draw largest contour as white filled on black background as mask
    height, width = image.shape
    mask = np.zeros((height, width), dtype=np.uint8)
    cv.drawContours(mask, [big_contour], 0, 255, cv.FILLED)

    image = cv.bitwise_and(original_image, original_image, mask=mask)

    return image


def enhance_contrast(image):
    return cv.equalizeHist(image)


def apply_global_threshold(image):
    ret, image = cv.threshold(image, 100, 255, cv.THRESH_BINARY)
    return image


def get_roi_from_mask(mask):
    # Perform a morphological opening filter to remove false positives
    mask = opening_filter(mask, iter=1, kernel_size=5)
    mask = closing_filter(mask, iter=3, kernel_size=8)
    mask = cv.dilate(mask, (5, 5), iterations=1)
    return mask


def detect_contours_of_artifacts(roi):
    # detect contours
    roi = cv.Canny(roi, 100, 200)
    # increase thickness
    kernel = get_circular_kernel(8)
    return cv.dilate(roi, kernel, iterations=1)


def paint_fragments_in_red(img):
    roi = img.copy()
    roi = cv.cvtColor(roi, cv.COLOR_GRAY2BGR)
    # Set the red channel values to 255
    blue_channel = roi[:, :, 0]  # Extract the blue channel (channel index 0)
    green_channel = roi[:, :, 1]  # Extract the green channel (channel index 1)
    roi[0] = 255  # set red channel to maximum
    roi[green_channel > 0, 1] = 0  # Set green channel values to 0
    roi[blue_channel > 0, 2] = 0  # Set blue channel values to 0
    return roi


def mark_roi_in_original_image(original, roi):
    # Mark roi in original image
    original = cv.normalize(original, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    original = cv.cvtColor(original, cv.COLOR_GRAY2BGR)
    modified = cv.bitwise_or(original, roi)
    return modified
