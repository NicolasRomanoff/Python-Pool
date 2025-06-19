import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def sos():
    '''
    Translate a sentence into Morse code
    '''
    try:
        assert len(sys.argv) == 2, \
            "AssertionError: more than one argument is provided"
        string = sys.argv[1].upper()
        assert all(c in NESTED_MORSE for c in string), \
            "AssertionError: the arguments are bad"
        morse_string = "".join(list(NESTED_MORSE[c] for c in string))
        print(morse_string)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    sos()
