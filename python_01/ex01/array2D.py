import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
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
        if not isinstance(family, list):
            raise TypeError("TypeError: expected type for family: list")
        if not isinstance(start, int):
            raise TypeError("TypeError: expected type for start: int")
        if not isinstance(end, int):
            raise TypeError("TypeError: expected type for end: int")
        if len(family):
            for f in family:
                if len(f) != len(family[0]):
                    raise ValueError("ValueError: size of family is incorrect")
        else:
            raise ValueError("ValueError: size of family is incorrect")
        family_arr = np.array(family)
        print(f"My shape is : {family_arr.shape}")
        sliced_arr = family_arr[start:end]
        print(f"My new shape is : {sliced_arr.shape}")
        return sliced_arr.tolist()
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    return None
