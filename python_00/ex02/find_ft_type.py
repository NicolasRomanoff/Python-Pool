def all_thing_is_obj(object: any) -> int:
    try:
        dictionnary = {list: "List",
                       tuple: "Tuple",
                       set: "Set",
                       dict: "Dict",
                       str: f'{object} is in the kitchen'}
        typeOf = type(object)
        if typeOf not in dictionnary:
            raise TypeError
        response = dictionnary[typeOf]
        print(f'{response} : {typeOf}')
    except TypeError:
        print("Type not found")
    return 42
