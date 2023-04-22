import pydicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
import cv2 as cv
from icecream import ic
import numpy as np
from PIL import Image, ImageFilter
from utils import compare_image_filter


img = Image.open("image_processing/images/mammography.png").convert("L")

img = img.point(lambda x: 255 if x > 180 else 0)

img.show()
