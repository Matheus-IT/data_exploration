import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import cv2
import pydicom


# Carregar imagem
ds = pydicom.dcmread("image_processing/images/mammography.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
image = cv2.normalize(pixel_data, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

# Threshold the image to create a binary image
threshold = 128
binary_image = image > threshold

# Label the connected components in the binary image
labels, num_labels = scipy.ndimage.label(binary_image)

# plotting image
f = plt.figure()

# original image
f.add_subplot(1, 2, 1)
plt.imshow(image, cmap="bone")
plt.title("Original image")
plt.axis("off")

# labeled Image
f.add_subplot(1, 2, 2)
plt.imshow(labels, cmap="bone")
plt.title("Labeled Image")
plt.axis("off")

plt.show(block=True)
