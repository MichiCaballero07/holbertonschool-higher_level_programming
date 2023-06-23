#!/usr/bin/python3
"""Import the json module"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        json_string = file.read()
        obj = json.loads(json_string)
        return obj
