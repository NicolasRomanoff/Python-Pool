from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, first_name, is_alive=True):
        '''Init a Baratheon family member'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        '''Display info'''
        return f"{self.first_name} {self.family_name} have " \
            + f"{self.eyes} eyes, {self.hairs} hairs and he's " \
            + f"{"alive" if self.is_alive else "dead"} !"

    def __repr__(self):
        '''Display type'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    '''Representing the Lannister family.'''
    def __init__(self, first_name, is_alive=True):
        '''Init a Lannister family member'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        '''Display info'''
        return f"{self.first_name} {self.family_name} have " \
            + f"{self.eyes} eyes, {self.hairs} hairs and he's " \
            + f"{"alive" if self.is_alive else "dead"} !"

    def __repr__(self):
        '''Display type'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @staticmethod
    def create_lannister(first_name, is_alive):
        return Lannister(first_name, is_alive)
