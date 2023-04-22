import pydicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
)
import cv2 as cv
from utils.image_normalization import normalize, denormalize
from icecream import ic
import numpy as np
from PIL import Image, ImageFilter
from image_processing_course.utils import compare_image_filter


img = Image.open("image_processing/images/mammography.png").convert("L")

compare_image_filter(img, lambda img: img.filter(ImageFilter.BLUR), gray=True)

# img = img.point(lambda x: 255 if x > 180 else 0)

# img.show()
