import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
from utils import compare_image_filter

img = Image.open("image_processing/images/cube.jpg")

compare_image_filter(img, lambda img: img.filter(ImageFilter.CONTOUR))

compare_image_filter(img, lambda img: img.filter(ImageFilter.DETAIL))

compare_image_filter(img, lambda img: img.filter(ImageFilter.EDGE_ENHANCE))

compare_image_filter(img, lambda img: img.filter(ImageFilter.EMBOSS))

compare_image_filter(img, lambda img: img.filter(ImageFilter.FIND_EDGES))

compare_image_filter(img, lambda img: img.filter(ImageFilter.SMOOTH))

compare_image_filter(img, lambda img: img.filter(ImageFilter.SHARPEN))
