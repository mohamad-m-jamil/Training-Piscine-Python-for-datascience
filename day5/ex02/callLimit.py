def callLimit(limit: int):
    """Decorator factory to limit function calls."""
    count = 0

    def callLimiter(function):
        """Decorator to track function calls."""

        def limit_function(*args, **kwds):
            """Calls the function if within the limit, else prints an error."""
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)

        return limit_function

    return callLimiter


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()
