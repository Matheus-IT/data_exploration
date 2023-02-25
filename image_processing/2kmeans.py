import numpy as np
import matplotlib.pyplot as plt
import cv2
import pydicom


# Carregar imagem
ds = pydicom.dcmread("image_processing/images/mammography.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
img = cv2.normalize(pixel_data, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

# Resize image, or else it will be displayed too large
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reshaping the image into a 2D array of pixels and 3 color values (RGB)
pixel_vals = img.reshape((-1, 3))

# Convert to float type only for supporting cv2.kmean
pixel_vals = np.float32(pixel_vals)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
k = 3  # Choosing number of cluster
retval, labels, centers = cv2.kmeans(
    pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
)

centers = np.uint8(centers)

# Mapping labels to center points( RGB Value)
segmented_data = centers[labels.flatten()]

# reshape data into the original image dimensions
segmented_image = segmented_data.reshape((img.shape))

plt.imshow(segmented_image)
plt.show()
