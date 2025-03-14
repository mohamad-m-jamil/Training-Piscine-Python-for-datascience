def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a function that applies `function` to `x` and updates `x`."""

    def inner() -> float:
        """Applies the function to x and stores the result."""
        nonlocal x
        result = function(x)
        x = result
        return result

    return inner
