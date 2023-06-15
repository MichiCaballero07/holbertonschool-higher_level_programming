#!/usr/bin/python3
"""
Module that have a function that adds 2 integers.

Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    """

    # 'a' and 'b' must be integers else show a error
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # 'a' and 'b' must be first casted to integers if they are float
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if (a + b) > 100000000000000:
        return 'Error'
    return a + b
