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

    '''funtion update'''
    def update(self, *args, **kwargs):
        '''conditional update'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    '''function'''
    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
