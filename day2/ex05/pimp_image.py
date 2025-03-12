import numpy as np
import matplotlib.pyplot as plt
# from load_image import ft_load


def ft_invert(array) -> np.ndarray:
    """Inverts the colors of the image."""
    print("The shape of image is:", array.shape)
    plt.imshow(array)
    plt.title("Original")
    plt.axis("off")
    plt.show()

    inverted = 255 - array
    plt.imshow(inverted)
    plt.title("Invert")
    plt.axis("off")
    plt.show()
    print(inverted)
    return inverted


def ft_red(array) -> np.ndarray:
    """Applies a red filter to the image."""
    red = array * np.array([1, 0, 0], dtype=np.uint8)
    plt.imshow(red)
    plt.title("Red")
    plt.axis("off")
    plt.show()
    print(red)
    return red


def ft_green(array) -> np.ndarray:
    """Applies a green filter to the image."""
    green = array - array * np.array([1, 0, 1], dtype=np.uint8)
    plt.imshow(green)
    plt.title("Green")
    plt.axis("off")
    plt.show()
    print(green)
    return green


def ft_blue(array) -> np.ndarray:
    """Applies a blue filter to the image."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.title("Blue")
    plt.axis("off")
    plt.show()
    print(blue)
    return blue


def ft_grey(array) -> np.ndarray:
    """Converts the image to grayscale."""
    r = array[:, :, 0] / 3
    g = array[:, :, 1] / 3
    b = array[:, :, 2] / 3
    grey = (r + g + b).astype(np.uint8)
    grey_img = np.stack([grey, grey, grey], axis=-1)
    plt.imshow(grey_img)
    plt.title("Grayscale")
    plt.axis("off")
    plt.show()
    print(grey_img)
    return grey_img


# array = ft_load("landscape.jpg")

# ft_invert(array)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)

# print(ft_invert.__doc__)
