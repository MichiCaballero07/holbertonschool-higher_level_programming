#!/usr/bin/python3
'''import the class base'''

from models.base import Base
from models.rectangle import Rectangle


'''Square'''


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
