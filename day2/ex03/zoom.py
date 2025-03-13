import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def trim(array, x, y, width, height, depth=3):
    """
    Extracts a portion of the image array based on specified
    coordinates and dimensions.

    This function slices a NumPy image array to create a subarray.
    It extracts a region of the image
    starting from the given (x, y) coordinates, with the specified
    width, height, and depth.

    Args:
        array (np.ndarray): The original image array to be sliced.
        x (int): The x-coordinate of the top-left corner of the region
        to slice.
        y (int): The y-coordinate of the top-left corner of the region
        to slice.
        width (int): The width of the region to slice.
        height (int): The height of the region to slice.
        depth (int, optional): The number of color
        channels to retain (default is 3 for RGB).
    """
    return array[y:y+width, x:x+height, :depth]


def main():
    """
    Loads an image, applies slicing, and displays the zoomed-in section.
    This function loads an image from a file, slices
    a portion of the image using
    the `trim` function, and then displays the zoomed-in
    section using matplotlib.
    It also prints the shape of the original and sliced
    images for reference.
    Steps:
    1. Load the image from a file path using `ft_load`.
    2. Slice the image using `trim` to extract a region.
    3. Display the sliced region and show its shape using matplotlib.
    4. Print out the original and new shape after slicing.

    Example:
        main()
        # Output:
        # The shape of image is: (original image shape)
        # new shape after slicing: (new shape after slicing)
        # A zoomed-in section of the image displayed.
    """
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
