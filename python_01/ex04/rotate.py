import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import ft_load


def tranpose(img_arr: np.array):
    '''
    Tranpose and return image info
    '''
    try:
        if type(img_arr) is not np.ndarray:
            raise TypeError("TypeError: expected type for img_arr: np.array")
        img_arr = img_arr[:, ::-1]
        img = Image.fromarray(img_arr).rotate(90)
        plt.imshow(img, cmap='gray')
        plt.show()
        img_arr = np.array(img)
        print(f"New shape after Transpose: {img_arr.shape}")
        return img_arr
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
    print(tranpose(img_arr))
    pass


if __name__ == "__main__":
    main()
