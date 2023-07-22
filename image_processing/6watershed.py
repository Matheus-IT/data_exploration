import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import pydicom
from PIL import Image


MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography-dataset/nbia/CMMD/D1-0001/07-18-2010-NA-NA-79377/1.000000-NA-70244/"
ds = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
img = cv.normalize(pixel_data, None, 0, 255, cv.NORM_MINMAX, cv.CV_8UC1)

ret, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
# sure background area
sure_bg = cv.dilate(opening, kernel, iterations=3)
# Finding sure foreground area
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers + 1
# Now, mark the region of unknown with zero
markers[unknown == 255] = 0

# Replicate single-channel image into three channels
img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)

markers = cv.watershed(img, markers)
img[markers == -1] = [255, 0, 0]

# Resize image, or else it will be displayed too large
img = cv.resize(img, (0, 0), fx=0.2, fy=0.2)

# Mostrar o resultado
Image.fromarray(img).show()
# cv.imshow("Resultado", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
