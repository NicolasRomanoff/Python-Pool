
def callLimit(limit: int):
    '''Return a decorator that limits
    the number of times a function can be called'''
    count = 0

    def callLimiter(function):
        '''Returns a function that calls the function'''
        def limit_function(*args, **kwds):
            '''Execute function or raise if limit is exceeded'''
            try:
                nonlocal count
                if count >= limit:
                    raise Exception(f"Error: {function} " +
                                    "call too many times")
                function()
                count += 1
                return count
            except Exception as e:
                print(e)
        return limit_function
    return callLimiter
