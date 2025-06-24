from abc import ABC, abstractmethod


class Character(ABC):
    '''An abstract class for Character'''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Constructor for Character'''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Make the character die'''
        self.is_alive = False


class Stark(Character):
    '''A class for Stark Character'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor for Stark Character'''
        super().__init__(first_name, is_alive)
