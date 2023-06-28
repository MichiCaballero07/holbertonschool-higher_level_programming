#!/usr/bin/python3
"""import json"""
import json


class Base:
    '''construct'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''function to convert'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save to file'''
        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string(
            [obj.to_dictionary()for obj in list_objs] if list_objs else [])
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        '''from json'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
