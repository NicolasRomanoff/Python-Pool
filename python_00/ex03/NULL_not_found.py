from types import NoneType


def NULL_not_found(object: any) -> int:
    if object == object and object:
        print("Type not found")
        return 1
    try:
        dictionnary = {NoneType: f'Nothing: {object}',
                       float: f'Cheese: {object}',
                       int: f'Zero: {object}',
                       str: "Empty:",
                       bool: f'Fake: {object}'}
        typeOf = type(object)
        response = dictionnary[typeOf]
        print(f'{response} {typeOf}')
    except TypeError:
        print("Type not found")
        return 1
    return 0
