#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Define class BaseGeometry
    """
    def area(self):
        """Define an exception for area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validate argument value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
