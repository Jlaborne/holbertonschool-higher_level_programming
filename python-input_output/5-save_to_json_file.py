#!/usr/bin/python3
"""Define a json to file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file using json"""
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
