import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Displays shape, new shape and result of slicing
    '''
    try:
        if type(family) is not list:
            raise TypeError("TypeError: expected type for family: list")
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
