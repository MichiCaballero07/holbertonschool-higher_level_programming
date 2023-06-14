#!/usr/bin/python3
"""
5. Printing a square
"""


class Square:
    """
    Class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set __size to value
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates area of square
        Returns: the square area
        """
        return (self.__size) ** 2

    def my_print(self):
        """
        print  square
        """
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.__size))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
