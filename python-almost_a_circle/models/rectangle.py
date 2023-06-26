#!/usr/bin/python3
"""import"""


from models.base import Base


"""Rectangle class"""


class Rectangle(Base):
    '''Base class for Rectangles'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.___width = width
        self.___height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
