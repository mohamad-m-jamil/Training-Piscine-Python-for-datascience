import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def trim(array, x, y, width, height, depth=3):
    """
    Extracts a portion of the image array based
    on specified coordinates and dimensions.

    This function slices a NumPy image array to
    create a subarray. It extracts a region of the image
    starting from the given (x, y) coordinates,
    with the specified width, height, and depth.

    Args:
        array (np.ndarray): The original image array to be sliced.
        x (int): The x-coordinate of the top-left corner of
        the region to slice.
        y (int): The y-coordinate of the top-left corner of
        the region to slice.
        width (int): The width of the region to slice.
        height (int): The height of the region to slice.
        depth (int, optional): The number of color channels
        to retain (default is 3 for RGB).

    Returns:
        np.ndarray: A subarray of the original image based
        on the specified slice parameters.

    Example:
        trimmed_image = trim(image, 450, 100, 400, 400, 1)
        # Output:
        # A subarray from the original image with the
        # shape (400, 400, 1).
    """
    return array[y:y+width, x:x+height, :depth]


def main():
    """
    Loads an image, slices a region, transposes the
    image, and displays the result.

    This function performs the following steps:
    1. Loads an image from a file using `ft_load`.
    2. Slices the image using the `trim` function to zoom
    into a specific region.
    3. Prints the shape of the original and sliced image.
    4. Transposes the sliced image (swaps the height and width).
    5. Displays the transposed image using `matplotlib`
    and shows the zoomed-in section.

    Example:
        main()
        # Output:
        # The shape of image is: (original image shape)
        # New shape after Transpose: (new transposed shape)
        # A zoomed-in and transposed section of the image displayed.
    """
    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        exit(1)
    image = trim(image, 450, 100, 400, 400, 1)
    print(f"The shape of image is: {image.shape}", end='')
    print(f" or ({image.shape[0]}, {image.shape[1]})")
    print(image)
    t_image = np.transpose(image, (1, 0, 2))
    t_image = np.squeeze(t_image)
    print(f"New shape after Transpose: ({t_image.shape})")
    print(t_image)
    plt.imshow(t_image, cmap='gray')
    plt.axis('off')
    plt.title("Zoom animal")
    plt.show()


if __name__ == "__main__":
    main()
