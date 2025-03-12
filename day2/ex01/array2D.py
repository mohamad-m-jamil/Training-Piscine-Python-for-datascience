import numpy as nb


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (list of lists) while ensuring input validation.

    This function takes a list of lists representing a 2D array and slices it
    along the first dimension using the provided start and end indices. It also
    ensures that all rows have the same length before slicing.

    Args:
        family (list[list]): A 2D list where
        all rows must have the same length.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list[list]: A new sliced 2D list.

    Raises:
        TypeError: If `family` is not a list of lists.
        ValueError: If rows have inconsistent lengths.
        IndexError: If `start` or `end` indices are out of range.

    Example:
        family = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        slice_me(family, 0, 2)
        # Output:
        # My shape is : (3, 3)
        # My new shape is : (2, 3)
        # Returns: [[1, 2, 3], [4, 5, 6]]
    """
    if type(family) is not list:
        print("AssertionError: family must be a list of lists")
        exit()
    for row in family:
        if type(row) is not list:
            print("AssertionError: all elements in family must be lists")
            exit()
    row_length = len(family[0])
    for row in family:
        if len(row) != row_length:
            print("AssertionError: all rows must have the same length")
            exit()
    if type(start) is not int or type(end) is not int:
        print("AssertionError: start and end must be integers")
        exit()
    arr2d = nb.array(family)
    if not (0 <= abs(start) <= len(arr2d)):
        print("AssertionError: start or end index out of range")
        exit()
    if not (-len(arr2d) <= end <= len(arr2d)):
        print("AssertionError: start or end index out of range")
        exit()
    firstprint = arr2d.shape
    sliced_arr = arr2d[start:end]
    afterslied = sliced_arr.shape
    print(f"My shape is : {firstprint}")
    print(f"My new shape is : {afterslied}")
    return sliced_arr.tolist()


# family = [[1.80, 78.4],
# [2.15, 102.7],
# [2.10, 98.5],
# [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
