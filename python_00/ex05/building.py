import sys
import string


def building():
    '''
    Displays information about string
    '''
    if len(sys.argv) < 2:
        str = sys.stdin.read()
    else:
        str = sys.argv[1]
    try:
        assert len(sys.argv) <= 2, \
          "AssertionError: more than one argument is provided"
        print(f"The text contains {len(str)} characters:")
        print(f"{sum(map(lambda c: c.isupper(), str))} upper letters")
        print(f"{sum(map(lambda c: c.islower(), str))} lower letters")
        print(f"{sum(map(lambda c: c in string.punctuation, str))}",
              "punctuation marks")
        print(f"{sum(map(lambda c: c.isspace(), str))} spaces")
        print(f"{sum(map(lambda c: c.isdigit(), str))} digits")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    building()
