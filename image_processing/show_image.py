import pydicom
import cv2
import matplotlib.pyplot as plt

# Carregar imagem
ds = pydicom.dcmread("image_processing/images/mammography_modified.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
img = cv2.normalize(pixel_data, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

plt.imshow(img, cmap="bone")
plt.show()
