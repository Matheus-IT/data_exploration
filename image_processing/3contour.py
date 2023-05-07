import matplotlib.pyplot as plt
import numpy as np
import cv2
import pydicom


# Carregar imagem
ds = pydicom.dcmread("image_processing/images/dicom/mammography.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
img = cv2.normalize(pixel_data, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

_, thresh = cv2.threshold(img, np.mean(img), 255, cv2.THRESH_BINARY_INV)

edges = cv2.dilate(cv2.Canny(thresh, 0, 255), None)

plt.axis("off")
plt.imshow(edges)
plt.show()
