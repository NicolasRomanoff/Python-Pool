class calculator:
    '''Basic Calculator class'''
    def __init__(self, object):
        '''Init calculator value'''
        self.value = object

    def __add__(self, object) -> None:
        '''Add value'''
        self.value = [v + object for v in self.value]
        print(self.value)

    def __mul__(self, object) -> None:
        '''Multiplicate value'''
        self.value = [v * object for v in self.value]
        print(self.value)

    def __sub__(self, object) -> None:
        '''Sub value'''
        self.value = [v - object for v in self.value]
        print(self.value)

    def __truediv__(self, object) -> None:
        '''Divide value'''
        try:
            self.value = [v / object for v in self.value]
            print(self.value)
        except ZeroDivisionError as e:
            print(e)
