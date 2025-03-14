from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    #Mean (average)
    #Median (middle value)
    #Quartiles (25% and 75%)
    #Standard deviation (spread of data)
    #Variance (measure of variability)
    """

    total = 0.0
    values = []

    for arg in args:
        total += arg
        values.append(arg)

    num_args = len(values)

    if num_args == 0:
        for _ in kwargs.values():
            print("ERROR")
        return

    values.sort()
    mean = total / num_args
    median = _calculate_median(values, num_args)
    quartile = _calculate_quartiles(values, num_args)
    variance = sum((x - mean)**2 for x in values) / num_args
    std_deviation = variance**0.5

    results = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std_deviation,
        "var": variance
    }

    for stat_name in kwargs.values():
        if stat_name in results:
            print(f"{stat_name} : {results[stat_name]}")


def _calculate_median(values: list, length: int) -> float:
    """Calculate median value from sorted list."""
    mid = length // 2
    if length % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]


def _calculate_quartiles(values: list, length: int) -> list[float]:
    """Calculate first and third quartiles."""
    q1_index = length // 4
    q3_index = q1_index * 3
    return [float(values[q1_index]), float(values[q3_index])]

# def ft_statistics(*args: Any, **kwargs: Any) -> None:
#     """
#     Mean (average)
#     Median (middle value)
#     Quartiles (25% and 75%)
#     Standard deviation (spread of data)
#     Variance (measure of variability)
#     """
#     args_list = list(args)
#     total = 0
#     values = []
#     num_args = 0
#     for arg in args:
#         num_args += 1
#         total += arg
#         values.append(arg)

#     if num_args == 0:
#         for value in kwargs.items():
#             print("ERROR")
#         return

#     total = 0
#     for arg in args_list:
#         total += arg
#     mean = total / num_args
#     i = 0
#     while i < num_args - 1:
#         j = 0
#         while j < num_args - i - 1:
#             if values[j] > values[j + 1]:
#                 values[j], values[j + 1] = values[j + 1], values[j]
#             j += 1
#         i += 1

#     median_index = num_args // 2
#     if num_args % 2 == 0:
#         median = (values[median_index - 1] + values[median_index]) / 2
#     else:
#         median = values[median_index]

#     q1_index = num_args // 4
#     q3_index = q1_index * 3
#     quartile = [float(values[q1_index]), float(values[q3_index])]

#     variance_total = 0
#     for value in values:
#         variance_total += (value - mean) ** 2
#     variance = variance_total / num_args
#     std_deviation = (variance ** 0.5)

#     result = {"mean": mean, "median": median, "quartile": quartile,
#               "std": std_deviation, "var": variance}

#     for key, value in kwargs.items():
#         if value in result:
#             print(f"{value} : {result[value]}")
