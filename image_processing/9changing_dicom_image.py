import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import pydicom


# Carregar imagem
ds = pydicom.dcmread("image_processing/images/mammography.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
img = cv.normalize(pixel_data, None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)

# Make a rectangle
cv.rectangle(img, (1000, 1000), (1500, 1500), 255, 10)

plt.imshow(img, cmap="bone")
plt.show()

# Update the DICOM object with the normalized pixel data
ds.PixelData = img.astype(np.uint16).tobytes()

ds.save_as("image_processing/images/mammography_modified.dcm")
