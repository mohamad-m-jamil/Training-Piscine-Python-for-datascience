import numpy as np
from PIL import Image


def main(path: str) -> np.ndarray:
    """
    Loads an image from a given file path and converts it to a NumPy array.

    This function opens an image file, checks if it is in JPG or JPEG format,
    converts it to an RGB image, and then transforms it into a NumPy array.

    Args:
        path (str): The file path of the image to be loaded.

    Returns:
        np.ndarray: A NumPy array representing the image's pixel data.
        None: If the file is not found or is in an unsupported format.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: If an unexpected error occurs.

    Example:
        img_array = ft_load("image.jpg")
        # Output:
        # The shape of image is: (height, width, 3)
    """
    try:
        img = Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            print("Error: Unsupported image format. Please use JPG or JPEG.")
            return None
        img = img.convert("RGB")
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array
    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
