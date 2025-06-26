
def square(x: int | float) -> int | float:
    '''Return square of x'''
    return x * x


def pow(x: int | float) -> int | float:
    '''Return x power x'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''Returns a function that applies the given function to x'''
    count = 0

    def inner() -> float:
        '''Applies the function to x'''
        try:
            nonlocal count
            count = function(count if count else x)
            return count
        except Exception as e:
            print(e)
        return None
    return inner
