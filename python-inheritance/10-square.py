#!/usr/bin/python3
""" class impor"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
