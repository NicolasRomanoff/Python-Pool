import sys
from ft_filter import ft_filter


def is_alphanumeric_space(s: str):
    '''
    Check if a string doesn't contains any other characters then a :
        - letters
        - numbers
        - spaces

    Args:
        param1 (str): The string need to be check

    Returns:
        bool:
    '''
    return len(list(ft_filter(lambda c: c.isalnum() or c == " ", s))) == len(s)


def main():
    '''
    Output a list of words from param1 that have a length greater than param2:

    Args:
        param1 (str): A string containing one or more words separated by spaces
        param2 (int): A number to sort words by if their size is greater

    Returns:
        list: A list of param1 words's larger than the number in param2
    '''
    try:
        assert len(sys.argv) == 3, \
            "AssertionError: the program needs only 2 parameters"
        assert type(sys.argv[1]) is str \
            and is_alphanumeric_space(sys.argv[1]), \
            "AssertionError: the first parameter is not a valid string"
        assert sys.argv[2].isdigit(), \
            "AssertionError: the second parameter is not a positive number"
        strList = sys.argv[1].split()
        nb = int(sys.argv[2])
        f_list = ft_filter(lambda word: len(word) > nb, strList)
        print(list(f_list))
        return list(f_list)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
