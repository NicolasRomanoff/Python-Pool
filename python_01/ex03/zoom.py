import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(img_arr: np.array) -> np.array:
    '''
    Zoom and return image info
    '''
    try:
        if type(img_arr) is not np.ndarray:
            raise TypeError("TypeError: expected type for img_arr: np.array")
        im = Image.fromarray(img_arr).convert("L")
        box = [0, 0, 400, 400]
        im = im.crop(box)
        arr = np.array(im)
        plt.imshow(arr, cmap='gray')
        plt.show()
        print(f"New shape after slicing: {arr.shape}")
        return arr
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except SystemError as e:
        print(e)
    except OSError as e:
        print(e)


def main():
    '''
    Run a program
    '''
    path = "animal.jpeg"
    img_arr = ft_load(path)
    print(img_arr)
    print(zoom(img_arr))


if __name__ == "__main__":
    main()
