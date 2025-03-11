def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) for a list of individuals.

    This function takes two lists: one containing heights (in meters) and the
    other containing weights (in kilograms). It computes the BMI for each
    individual using the formula: BMI = weight / (height * height).

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list containing the calculated BMI values.

    Raises:
        SystemExit: If the input lists are not of the same length.

    Example:
        give_bmi([1.75, 1.60], [70, 50])
        # Output: [22.86, 19.53]
    """
    i = 0
    res = []
    if type(height) is not list or type(weight) is not list:
        print("Error: Both height and weight must be lists")
        exit()
    if len(height) != len(weight):
        print("error: lists must be of the same length")
        exit()
    while i < len(height):
        if (type(weight[i]) not in [int, float]):
            print("error")
            exit()
        if (type(height[i]) not in [int, float]):
            print("error")
            exit()
        cal = weight[i] / (height[i] * height[i])
        res.append(cal)
        i += 1
    return (res)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determines whether each BMI value exceeds a given limit.

    This function takes a list of BMI values and compares each one to a
    specified limit. If the BMI is greater than the limit, it returns True;
    otherwise, it returns False.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The threshold for determining if a BMI is high.

    Returns:
        list[bool]: A list of boolean values indicating whether each BMI
        exceeds the limit.

    Example:
        apply_limit([22.86, 19.53], 21)
        # Output: [True, False]
    """
    i = 0
    res = []
    if type(bmi) is not list:
        print("Error: bmi must be lists")
        exit()
    while i < len(bmi):
        if (type(bmi[i]) not in [int, float]):
            print("error")
            exit()
        if bmi[i] > limit:
            res.append(True)
        else:
            res.append(False)
        i += 1
    return (res)
