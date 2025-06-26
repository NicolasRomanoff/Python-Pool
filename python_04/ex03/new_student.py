import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Return a random id'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Class about student'''
    name: str = field()
    surname: str = field()
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        '''Init value not yet init'''
        self.login = self.name[0] + self.surname
