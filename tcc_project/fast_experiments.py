import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
    display_side_by_side,
)
import cv2 as cv
from utils.image_normalization import normalize, denormalize
from utils.filters import opening_filter, closing_filter, high_pass_filter
from icecream import ic
import numpy as np
from utils.elapsed_time import Timer
from PIL import Image
import pydicom


with Timer():
    # MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography-dataset/nbia/CMMD/D2-0001/07-18-2011-NA-NA-75485/1.000000-NA-12786/"
    # original = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm").pixel_array
    original = cv.imread("image_processing/images/mammography.png")
    Image.fromarray(original).show()
