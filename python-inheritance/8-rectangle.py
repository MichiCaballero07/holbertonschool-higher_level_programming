#!/usr/bin/python3
"""Import class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Rectangle class"""


class Rectangle(BaseGeometry):
    '''Base class for Rectangles'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
