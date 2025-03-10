def ft_filter(function, iterable):
    """
    Custom implementation of the built-in filter() function.

    This function iterates through the given iterable
    and applies the provided function
    to each element. If the function returns True,
    the element is added to the final list.

    Args:
        function (callable): A function that takes
        one argument and returns a boolean.
        iterable (iterable): A sequence (e.g., list, tuple) to be filtered.

    Returns:
        list: A list containing elements from the
        iterable for which the function returned True.

    Example:
        def is_even(n):
            return n % 2 == 0

        result = ft_filter(is_even, [1, 2, 3, 4, 5, 6])
        print(result)  # Output: [2, 4, 6]
    """
    i = 0
    finallist = []
    while i < len(iterable):
        if function(iterable[i]):
            finallist.append(iterable[i])
        i += 1
    return (finallist)
