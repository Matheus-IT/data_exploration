import pydicom
from pydicom import FileDataset
import cv2
import matplotlib.pyplot as plt


img_path = "image_processing/images/mammography.dcm"
ds = pydicom.dcmread(img_path)

# Get pixel data and metadata
img = ds.pixel_array

# Convert pixel data to 8-bit integer
# img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

plt.imshow(img, cmap="bone")
plt.show()
