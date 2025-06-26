from types import NoneType


def NULL_not_found(object) -> int:
    if object and object == object:
        print("Type not found")
        return 1
    try:
        dictionnary = {NoneType: f'Nothing: {object}',
                       float: f'Cheese: {object}',
                       int: f'Zero: {object}',
                       str: "Empty:",
                       bool: f'Fake: {object}'}
        typeOf = type(object)
        if typeOf not in dictionnary:
            raise TypeError
        response = dictionnary[typeOf]
        print(f'{response} {typeOf}')
    except TypeError:
        print("Type not found")
        return 1
    return 0
