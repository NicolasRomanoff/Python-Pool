
def ft_median(args):
    '''Calcul and return median'''
    sort_args = sorted(args)
    len_args = len(args)
    first_median = sort_args[len_args // 2]
    if len_args % 2:
        return first_median
    return (first_median + sort_args[(len_args // 2) - 1]) / 2


def ft_quartile(args):
    '''Calcul and return quartile'''
    sort_args = sorted(args)
    len_args = len(args)
    mid = len_args // 2
    return [float(ft_median(sort_args[:mid + len_args % 2])),
            float(ft_median(sort_args[mid:]))]


def ft_var(args):
    '''Calcul and return variance'''
    mean = sum(args) / len(args)
    return sum([(arg - mean) * (arg - mean) for arg in args]) / len(args)


def ft_statistics(*args, **kwargs) -> None:
    '''Print mean, median, quartile, standard deviance and/or variance'''
    try:
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("TypeError: not a number")
    except Exception as e:
        print(e)
        return None
    for val in kwargs.values():
        try:
            if not len(args):
                raise Exception("ERROR")
            match val:
                case "mean":
                    print(f"{val} : {sum(args) / len(args)}")
                case "median":
                    print(f"{val} : {ft_median(args)}")
                case "quartile":
                    print(f"{val} : {ft_quartile(args)}")
                case "std":
                    print(f"{val} : {ft_var(args) ** 0.5}")
                case "var":
                    print(f"{val} : {ft_var(args)}")
        except Exception as e:
            print(e)
