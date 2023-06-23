#!/usr/bin/python3
"""Import json"""


import json


def save_to_json_file(my_obj, filename):
    """permitions of  writing json files"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
