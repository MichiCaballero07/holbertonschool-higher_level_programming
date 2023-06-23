#!/usr/bin/python3
"""Import the json"""


import json

def to_json_string(my_obj):
    """function that returns the JSON representation"""
    json_string = json.dumps(my_obj)
    return json_string
