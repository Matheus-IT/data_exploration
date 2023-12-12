import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
    display_side_by_side,
    show_image,
    show_rgb,
    show_hsv,
    show_lab,
    show_gray,
    show_ycrcb,
)
import cv2 as cv
from utils.image_normalization import normalize, denormalize
from utils.filters import opening_filter, closing_filter, high_pass_filter
from icecream import ic
import numpy as np
from utils.elapsed_time import Timer
from PIL import Image
import pydicom


image = cv.imread("image_processing/images/man.jpg")
show_ycrcb(image)
