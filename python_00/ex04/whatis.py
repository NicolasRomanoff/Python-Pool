import sys

try:
    assert len(sys.argv) == 2, \
      "AssertionError: more than one argument is provided"
    nb = sys.argv[1]
    try:
        if int(nb) % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except ValueError:
        assert False, "AssertionError: argument is not an integer"
except AssertionError as e:
    print(e)
