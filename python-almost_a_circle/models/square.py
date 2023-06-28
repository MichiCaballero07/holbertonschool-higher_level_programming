#!/usr/bin/python3
'''import the class base'''

from models.base import Base
from models.rectangle import Rectangle


'''Square'''


class Square(Rectangle):
    '''Square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    '''property'''
    @property
    def size(self):
        return self.width

    '''setter'''
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    '''function'''
    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
