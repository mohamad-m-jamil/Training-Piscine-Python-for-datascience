import sys
from ft_filter import ft_filter


def is_true(lst, number):
    """
    Checks if the length of a given list is greater than a specified number.

    Args:
        lst (list): The list to check.
        number (int): The threshold length.

    Returns:
        bool: True if the list length is greater
        than the number, otherwise False.
    """
    if len(list) > number:
        return True
    return False


def main():
    """
    Filters words from a given input string based on a specified length.

    This function takes two command-line arguments:
    - A string of words.
    - A number representing the minimum length a
    word must have to be included in the output.

    The function:
    1. Ensures exactly two arguments are provided.
    2. Converts the second argument to an integer.
    3. Splits the input string into a list of words.
    4. Uses a filtering function (`ft_filter`) to retain
    words longer than the specified length.
    5. Prints the filtered words.

    If the arguments are invalid (e.g., missing,
    incorrect types), an error message is displayed.

    Usage:
        python script.py "your text here" length

    Example:
        Input: python script.py "Hello world this is a test" 3
        Output: ['Hello', 'world', 'this', 'test']
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit()
    try:
        length = int(sys.argv[2])
    except IndexError:
        print("AssertionError: the arguments are bad")
        sys.exit()
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit()
    try:
        int(sys.argv[1])
        print("AssertionError: the arguments are bad")
        sys.exit()
    except ValueError:
        string = str(sys.argv[1])
    listofstr = string.split()
    result = ft_filter(lambda item: is_true(item, length), listofstr)
    print(result)


if __name__ == "__main__":
    main()
