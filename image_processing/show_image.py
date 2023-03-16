import pydicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
)


img_path = "image_processing/images/mammography_modified.dcm"
ds = pydicom.dcmread(img_path)

# Get pixel data and metadata
img = ds.pixel_array

plt.imshow(img, cmap="gray")
plt.show()
