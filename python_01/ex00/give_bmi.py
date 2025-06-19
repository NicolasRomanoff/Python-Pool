import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''
    Output a list of words from param1 that have a length greater than param2:

    Args:
        param1 (list[int | float]): A list of numbers that define the height
        param2 (list[int | float]): A list of numbers that define the weight

    Returns:
        list[int | float]: A list of BMIs calculated by param1 and param2
    '''
    try:
        if len(height) != len(weight):
            raise ValueError("ValueError: both lists aren't the same size")
        if not all(isinstance(h, int | float) for h in height):
            raise TypeError("TypeError: expected type for height: " +
                            "list[int | float]")
        if not all(isinstance(h, int | float) for h in weight):
            raise TypeError("TypeError: expected type for weight: " +
                            "list[int | float]")
        height_arr = np.array(height)
        weight_arr = np.array(weight)
        bmi = []
        for i in range(len(height_arr)):
            bmi.append((weight_arr[i] / (height_arr[i] ** 2)).tolist())
        return bmi
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    Output a list of boolean:
    True if number of param1 is greater than limit or False

    Args:
        param1 (list[int | float]): A list of numbers that define the BMIs
        param2 (int): A number that will serve as a limit for BMIs

    Returns:
        list[bool]: A list of bool: True if BMI is greater than limit
    '''
    try:
        if not all(isinstance(b, int | float) for b in bmi):
            raise TypeError("TypeError: expected type for bmi: " +
                            "list[int | float]")
        if not isinstance(limit, int):
            raise TypeError("TypeError: expected type for limit: int")
        return list(True if b > limit else False for b in bmi)
    except TypeError as e:
        print(e)
    return None
