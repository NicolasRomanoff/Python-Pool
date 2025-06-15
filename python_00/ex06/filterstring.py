import sys
from ft_filter import ft_filter


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
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        assert type(sys.argv[1]) is str, \
            "AssertionError: the arguments are bad"
        assert sys.argv[2].isdigit(), "AssertionError: the arguments are bad"
        strList = sys.argv[1].split()
        nb = int(sys.argv[2])
        fList = ft_filter(lambda word: len(word) > nb, strList)
        print(list(fList))
        return list(fList)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
