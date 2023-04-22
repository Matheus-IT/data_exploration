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
from timeit import default_timer as timer


ds = pydicom.dcmread(
    "image_processing/images/dicom/ex1/DICOM/09266278/7CF888A1/73F2A227.dcm"
)

# Get pixel data and metadata
img = ds.pixel_array

img = normalize(img)

plt.hist(img.flatten())
plt.show()

# img = cv.resize(img, (0, 0), fx=0.15, fy=0.15)

# # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
# pixel_vals = img.reshape((-1, 1))

# # Convert to float type only for supporting cv2.kmean
# pixel_vals = np.float32(pixel_vals)

# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.85)
# k = 5  # Choosing number of cluster
# retval, labels, centers = cv.kmeans(
#     pixel_vals, k, None, criteria, 10, cv.KMEANS_PP_CENTERS
# )

# centers = np.array(centers, dtype=np.uint8)

# labels[(labels != centers.argmin() + 1)] = 1

# # Mapping labels to center points
# segmented_data = centers[labels.flatten()]

# # reshape data into the original image dimensions
# segmented_image = segmented_data.reshape((img.shape))

# denormalize(img)

# segmented_image = img.copy()
# segmented_image[segmented_image >= 248] = 0

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# ax1.imshow(img, cmap="gray")
# ax2.imshow(segmented_image, cmap="gray")
# plt.show()
