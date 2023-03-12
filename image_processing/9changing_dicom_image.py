import numpy as np
import pydicom
from PIL import Image, ImageDraw


# Read the original dicom file
ds = pydicom.dcmread("image_processing/images/mammography.dcm")

# Copy the original dicom file
ds_copy = ds.copy()

# Get the pixel array of the image
img = ds_copy.pixel_array

# Convert the pixel array to a PIL image
img = Image.fromarray(img)

# Draw a square on the image using PIL
draw = ImageDraw.Draw(img)
draw.rectangle(
    [100, 100, 200, 200],  # Top-left and bottom-right coordinates of the square
    outline="red",
)

# Convert the PIL image back to a pixel array
img = np.array(img)

# Update the pixel array of the copy with the modified image
ds_copy.PixelData = img.tobytes()
ds_copy.Rows, ds_copy.Columns = img.shape

# Increment the instance number by one for the copy
ds_copy.InstanceNumber += 1
# Generate a new SOP Instance UID for the second file
ds_copy.SOPInstanceUID = pydicom.uid.generate_uid()

# Save the modified dicom file as a new file name
ds_copy.save_as("image_processing/images/mammography_modified.dcm")
