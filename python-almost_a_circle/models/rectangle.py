#!/usr/bin/python3
"""import"""


from models.base import Base


"""Rectangle class"""


class Rectangle(Base):
    '''Base class for Rectangles'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.___width = width
        self.___height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    '''access to width'''
    @property
    def width(self):
        return self._width

    '''adding value to width'''
    @width.setter
    def width(self, value):
        self._width = value

    '''access to height'''
    @property
    def height(self):
        return self._height

    '''adding value to height'''
    @height.setter
    def height(self, value):
        self._height = value

    '''access to x'''
    @property
    def x(self):
        return self._x

    '''adding value to x'''
    @x.setter
    def x(self, value):
        self._x = value

    '''access to y'''
    @property
    def y(self):
        return self._y

    '''adding value to y'''
    @y.setter
    def y(self, value):
        self._y = value
