#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Open the file in append mode"""
    with open(filename, 'a', encoding="utf-8") as file:
        start_pos = file.tell()
        file.write(text)
        end_pos = file.tell()
        num_characters_added =end_pos - start_pos
        
    return num_characters_added
