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
from utils.elapsed_time import Timer
from PIL import Image
import pydicom


with Timer():
    MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography_datasets/nbia/manifest-1616439774456/CMMD/D1-1042/07-18-2011-NA-NA-47524/1.000000-NA-03751/"
    original = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm").pixel_array

    Image.fromarray(original).show()
