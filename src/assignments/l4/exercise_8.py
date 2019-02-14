import math


# Exercise 8
def sample_mean(data_set: list) -> float:
    if not data_set:
        return 0.0

    # This will raise a TypeError if the list contains non-numeric values
    validate_input_number_list(data_set)

    sum_of_elements = 0

    for x in data_set:
        sum_of_elements += x

    return sum_of_elements / len(data_set)


def sample_standard_deviation(data_set: list) -> float:
    # We need at least 2 data points to calculate the standard deviation
    if not data_set or len(data_set) < 2:
        return 0.0

    # This will raise a TypeError if the list contains non-numeric values
    validate_input_number_list(data_set)

    mean = sample_mean(data_set)

    # Calculate the variance
    sum_of_elements = 0

    for x in data_set:
        sq_difference = (x - mean) ** 2
        sum_of_elements += sq_difference

    # Sample Std Deviation divides by n - 1
    variance = sum_of_elements / (len(data_set) - 1)

    # Take the square root of the variance
    sd = variance ** 0.5
    return sd


def median(input_list: list) -> float:

    if not input_list:
        return 0.0

    # This will raise a TypeError if the list contains non-numeric values
    validate_input_number_list(input_list)

    sorted_list = sorted(input_list)
    length = len(sorted_list)

    if length % 2 == 0:
        middle = (length // 2) - 1  # Lists in Python are 0-based so we need to offset it
        result = (sorted_list[middle] + sorted_list[middle + 1]) / 2
    else:
        middle = length // 2
        result = sorted_list[middle]

    return result


def nquartile(input_list: list) -> tuple:
    # Quartiles are just 3 percentiles that divide the group into 4 parts
    return npercentile(input_list, 25), npercentile(input_list, 50), npercentile(input_list, 75)


def npercentile(input_list: list, percentile: int) -> float:

    if not input_list:
        return 0.0

    # This will raise a TypeError if the list contains non-numeric values
    validate_input_number_list(input_list)

    if not 1 <= percentile <= 99:
        raise ValueError("Invalid percentile. Percentiles must be in the range [1,99]")

    sorted_list = sorted(input_list)
    index = ((len(sorted_list) + 1) * percentile) / 100

    if index.is_integer():
        index = int(index) - 1  # Lists are zero-based, so we should offset the index accordingly
        index = 0 if index < 0 else index

        result = sorted_list[index]
        return result

    else:
        mantissa = index - math.floor(index)
        index = int(math.floor(index)) - 1  # Lists are zero-based, so we should offset accordingly

        if index >= len(sorted_list) - 1:
            return sorted_list[-1]
        elif index < 0:
            index = 0

        result = sorted_list[index] + (mantissa * (sorted_list[index + 1] - sorted_list[index]))
        return result


def validate_input_number_list(input_list: list):

    if type(input_list) is not list:
        raise TypeError("The input is not a list")

    for x in input_list:
        if not (type(x) is int or type(x) is float):
            raise TypeError("Input list contains non-numeric values!")
