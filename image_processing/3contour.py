import matplotlib.pyplot as plt
import numpy as np
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

_, thresh = cv2.threshold(img, np.mean(img), 255, cv2.THRESH_BINARY_INV)

edges = cv2.dilate(cv2.Canny(thresh, 0, 255), None)

plt.axis("off")
plt.imshow(edges)
plt.show()
