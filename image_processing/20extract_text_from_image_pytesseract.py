import pytesseract
from PIL import Image
import numpy as np


def main():
    img = Image.open("image_processing/images/skyrim_image.jpg")
    img.show()
    # img = np.array(img)
    # img[img < 150] = 0
    # Image.fromarray(img).show()

    # output = pytesseract.image_to_string(img)
    # print(output)


if __name__ == "__main__":
    main()
