#!/usr/bin/python3
"""
create a class
"""


class Square:
    """
    create a method
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            print("\n" * (self.__position[1] - 1))
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
