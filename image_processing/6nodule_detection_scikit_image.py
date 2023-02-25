import numpy as np
import pydicom
from skimage.filters import threshold_otsu, gaussian
from skimage import exposure
from skimage.feature import canny
from skimage import measure
from skimage.color import label2rgb
import matplotlib.pyplot as plt

# Carregando a imagem DICOM
dcm = pydicom.dcmread("image_processing/images/image.dcm")

# Converter para imagem em tons de cinza
img = dcm.pixel_array

# Aplicando Filtro Gaussiano para suavizar a imagem
img_smooth = gaussian(img, sigma=5)

# Normalizando a imagem para valores entre 0 e 1
img_norm = exposure.rescale_intensity(img_smooth, out_range=(0, 1))

# Limiarizando a imagem com o método de Otsu
thresh = threshold_otsu(img_norm)
binary = img_norm > thresh

# Aplicando a detecção de bordas
edges = canny(binary, sigma=3)

# Encontrando os contornos dos objetos
contours = measure.find_contours(edges, 0.8)

# Desenhando contornos dos objetos na imagem original
image_label_overlay = label2rgb(
    np.zeros_like(img), image=img, bg_label=0, bg_color=[0, 0, 0]
)
for contour in contours:
    image_label_overlay[(contour[:, 0]).astype(int), (contour[:, 1]).astype(int), :] = [
        1,
        0,
        0,
    ]

# Exibindo a imagem com os contornos detectados
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(image_label_overlay)
plt.show()
