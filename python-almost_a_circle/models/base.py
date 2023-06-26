#!/usr/bin/python3
"""fuction"""


class Base:
    '''construct'''
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = Base.__nb_objects
        if id is not None:
            self.id = id

        Base.__nb_objects += 1
