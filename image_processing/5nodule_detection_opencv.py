import cv2
import pydicom
import numpy as np
import matplotlib.pyplot as plt


# Carrega a imagem em formato DICOM
image_path = "image_processing/images/image.dcm"
dcm = pydicom.dcmread(image_path)

# Converter para imagem em tons de cinza
img = dcm.pixel_array.astype(np.uint16)

# Normalizando a imagem para valores entre 0 e 255
img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Aplicando Filtro Gaussiano para suavizar a imagem
img_smooth = cv2.GaussianBlur(img_norm, (5, 5), 0)

# Limiarizando a imagem com o método de Otsu
ret, thresh = cv2.threshold(img_smooth, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Aplicando a detecção de bordas
edges = cv2.Canny(thresh, 100, 200)

# Encontrando os contornos dos objetos
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Desenhando contornos dos objetos na imagem original
img_contours = cv2.drawContours(img_norm, contours, -1, (0, 255, 0), 3)

# Exibindo a imagem com os contornos detectados
plt.imshow(img_contours, cmap=plt.cm.bone)
plt.show()
