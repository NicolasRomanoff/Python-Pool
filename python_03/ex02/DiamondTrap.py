from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Long live the king !'''
    def __init__(self, first_name, is_alive=True):
        '''Initiator'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        '''Set eyes color'''
        self.eyes = color

    def set_hairs(self, color):
        '''Set hairs color'''
        self.hairs = color

    def get_eyes(self):
        '''Get eyes color'''
        return self.eyes

    def get_hairs(self):
        '''Get hairs color'''
        return self.hairs
