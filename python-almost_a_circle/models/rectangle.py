#!/usr/bin/python3
'''import the class base'''

from models.base import Base


'''Rectangle'''


class Rectangle(Base):
    '''Class Resctangle inherited from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    '''Access to width'''
    @property
    def width(self):
        return self.__width

    '''add value to width'''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    '''Access to height'''
    @property
    def height(self):
        return self.__height

    '''add value to height'''

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    '''Access to x'''

    @property
    def x(self):
        return self.__x

    '''add value to x'''

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    '''Access to y'''

    @property
    def y(self):
        return self.__y

    '''add value to y'''

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    ''' difine area'''
    def area(self):
        '''add value to area'''
        return self.__width * self.__height

    '''function that prints stdout'''
    def display(self):
        '''print stdout " # "'''
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    '''funtion that str'''
    def __str__(self):
        '''return str'''
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    '''funtion that Update'''
    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    '''funtion dictionary'''
    def to_dictionary(self):
        '''returns a dictionary'''
        return{
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
