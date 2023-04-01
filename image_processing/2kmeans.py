import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pydicom
from utils.image_normalization import normalize, denormalize


# Carregar imagem
ds = pydicom.dcmread("image_processing/images/mammography.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
img = normalize(pixel_data)

# Resize image, or else it will be displayed too large
img = cv.resize(img, (0, 0), fx=0.1, fy=0.1)

# Reshaping the image into a 2D array of pixels and 3 color values (RGB)
pixel_vals = img.reshape((-1, 1))

# Convert to float type only for supporting cv2.kmean
pixel_vals = np.float32(pixel_vals)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.85)
k = 5  # Choosing number of cluster
retval, labels, centers = cv.kmeans(
    pixel_vals, k, None, criteria, 10, cv.KMEANS_PP_CENTERS
)

centers = np.array(centers, dtype=np.uint8)

labels[(labels != centers.argmax())] = 0

# Mapping labels to center points
segmented_data = centers[labels.flatten()]

# reshape data into the original image dimensions
segmented_image = segmented_data.reshape((img.shape))

images = cv.hconcat([img, segmented_image])
cv.imshow("images", images)
cv.waitKey(0)
cv.destroyAllWindows()
