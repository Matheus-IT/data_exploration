import cv2 as cv
import numpy as np


def get_circular_kernel(size):
    return cv.getStructuringElement(cv.MORPH_ELLIPSE, (size, size))


def opening_filter(image, iter=1, kernel_size=3):
    kernel = get_circular_kernel(kernel_size)
    image = cv.erode(image, kernel, iterations=iter)
    return cv.dilate(image, kernel, iterations=iter)


def closing_filter(image, iter=1, kernel_size=3):
    kernel = get_circular_kernel(kernel_size)
    image = cv.dilate(image, kernel, iterations=iter)
    return cv.erode(image, kernel, iterations=iter)


def high_pass_filter(image):
    # Aplica o filtro de Sobel para detecção de bordas
    sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)

    # Calcula o gradiente aproximado da imagem
    gradient_image = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normaliza a imagem para o intervalo [0, 255]
    gradient_image = cv.normalize(
        gradient_image, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U
    )

    return gradient_image
