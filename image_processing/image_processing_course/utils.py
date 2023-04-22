import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


def compare_image_filter(img: Image, operation: callable):
    fig = plt.figure(figsize=(8, 5))
    fig.add_subplot(1, 2, 1)

    plt.imshow(img)
    plt.title("Original")

    fig.add_subplot(1, 2, 2)

    filtered = operation(img)
    plt.imshow(filtered)
    plt.title("Filtered")
    plt.show()
