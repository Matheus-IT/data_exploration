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

# Initiate ORB detector
orb = cv.ORB_create(nfeatures=10000)

# find the keypoints with ORB
kp = orb.detect(img, None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0), flags=0)
plt.imshow(img2), plt.show()
