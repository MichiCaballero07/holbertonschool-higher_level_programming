#!/usr/bin/python3
"""data"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """data"""
    list_args = sys.argv[1:]

    if os.path.exists("add_item.json"):
        list_args = load_from_json_file("add_item.json") + list_args

    save_to_json_file(list_args, "add_item.json")


if __name__ == "__main__":
    main()
