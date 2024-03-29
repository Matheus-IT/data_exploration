import numpy as np
import matplotlib.pyplot as plt
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import cv2 as cv
from utils.presentation import show_pixel_info, show_pixel_array_info
from utils.image_normalization import normalize, denormalize
from icecream import ic


# Read the original dicom file
ds = pydicom.dcmread("image_processing/images/mammography.dcm")

# Copy the original dicom file
ds_copy = ds.copy()

# Get the pixel array of the image
img = ds_copy.pixel_array

# Store min and max values of original image
min_val = np.min(img)
max_val = np.max(img)

# Normalizing the image
img = normalize(img)

# Draw a square on the image
cv.rectangle(img, (500, 500), (1000, 1000), color=255, thickness=20)

# Denormalize image using inverse formula
img = denormalize(img, min_val, max_val)

# Update the pixel array of the copy with the modified image
ds_copy.PixelData = img.tobytes()
ds_copy.Rows, ds_copy.Columns = img.shape

# Increment the instance number by one for the copy
ds_copy.InstanceNumber += 1
# Generate a new SOP Instance UID for the second file
ds_copy.SOPInstanceUID = pydicom.uid.generate_uid()  # type: ignore

# Save the modified dicom file as a new file name
ds_copy.save_as("image_processing/images/mammography_modified.dcm")

plt.imshow(ds_copy.pixel_array, cmap="gray")
plt.show()
