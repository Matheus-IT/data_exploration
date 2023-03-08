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

# Creating a new DICOM object to hold the modified image
new_image_ds = pydicom.Dataset()
new_image_ds.PixelData = img.tobytes()
new_image_ds.Rows, new_image_ds.Columns = img.shape
# Setting some attributes based on the existing image
new_image_ds.ImagePositionPatient = ds[0].ImagePositionPatient
new_image_ds.ImageOrientationPatient = ds[0].ImageOrientationPatient
new_image_ds.PixelSpacing = ds[0].PixelSpacing

# Add the new image to the series
new_image_ds.SeriesInstanceUID = ds.SeriesInstanceUID
new_image_ds.SOPInstanceUID = pydicom.uid.generate_uid()
new_image_ds.ReferencedSOPInstanceUID = [ds[0].SOPInstanceUID]
ds.ReferencedSOPInstanceUID.append(new_image_ds.SOPInstanceUID)


plt.imshow(img, cmap="bone")
plt.show()

ds.save_as("image_processing/images/mammography.dcm")
new_image_ds.save_as("image_processing/images/mammography_modified.dcm")
