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

low = 10
high = 100

mask = cv2.inRange(img, low, high)

result = cv2.bitwise_and(img, img, mask=mask)

plt.axis("off")
plt.imshow(result)
plt.show()
