import sys
from ft_filter import ft_filter


def is_alphanumeric_space(s: str):
    '''
    If only alphanumeric and space characters
    '''
    return len(list(ft_filter(lambda c: c.isalnum() or c == " ", s))) == len(s)


def filterstring():
    '''
    Output a list of words greater than number
    '''
    try:
        assert len(sys.argv) == 3, \
            "AssertionError: the program needs 2 parameters"
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
    filterstring()
