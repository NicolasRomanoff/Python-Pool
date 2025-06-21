import numpy as np
from PIL import Image


def ft_invert(array) -> np.array:
    '''Inverts the color of the image received.'''
    try:
        print(array)
        new_arr = array.copy()
        new_arr = ([255, 255, 255] - new_arr).astype(np.uint8)
        Image.fromarray(new_arr).show()
    except Exception as e:
        print(e)


def ft_red(array) -> np.array:
    '''Change the color to red of the image received.'''
    try:
        print(array)
        new_arr = array.copy()
        new_arr = ([1, 0, 0] * new_arr).astype(np.uint8)
        Image.fromarray(new_arr).show()
    except Exception as e:
        print(e)


def ft_green(array) -> np.array:
    '''Change the color to green of the image received.'''
    try:
        print(array)
        new_arr = array.copy()
        new_arr[:, :, 0] = new_arr[:, :, 2] = 0
        Image.fromarray(new_arr).show()
    except Exception as e:
        print(e)


def ft_blue(array) -> np.array:
    '''Change the color to blue of the image received.'''
    try:
        print(array)
        new_arr = array.copy()
        new_arr[:, :, 0] = new_arr[:, :, 1] = 0
        Image.fromarray(new_arr).show()
    except Exception as e:
        print(e)


def ft_grey(array) -> np.array:
    '''Change the color to grey of the image received.'''
    try:
        print(array)
        new_arr = array.copy()
        for y in new_arr:
            for x in y:
                x[0] = x[1] = x[2] = np.sort(x)[1]
        Image.fromarray(new_arr).show()
    except Exception as e:
        print(e)
