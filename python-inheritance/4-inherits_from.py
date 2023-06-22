#!/usr/bin/python3
"""function that returns True if the object is an
instance of a class that inherited
"""


def inherits_from(obj, a_class):
    '''return True if'''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
