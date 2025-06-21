import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    '''
    Load and return image info
    '''
    try:
        if type(path) is not str:
            raise ValueError("ValueError: path is not a string")
        if not path:
            raise ValueError("ValueError: path is None")
        with Image.open(path) as im:
            arr = np.array(im)
            print(f"The shape of image is: {arr.shape}")
            return arr
    except ValueError as e:
        print(e)
    except OSError as e:
        print(e)
