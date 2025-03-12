import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def trim(array, x, y, width, height, depth=3):
    return array[y:y+width, x:x+height, :depth]


def main():
    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        exit(1)
    print(image)
    image = trim(image, 450, 100, 400, 400, 1)
    print(f"new shape after slicing: {image.shape}", end='')
    print(f"or ({image.shape[0]}, {image.shape[1]})")
    print(image)

    image = np.squeeze(image)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title("Zoom animal")
    plt.show()


if __name__ == "__main__":
    main()
