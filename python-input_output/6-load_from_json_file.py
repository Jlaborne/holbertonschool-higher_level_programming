#!/usr/bin/python3
"""Define a function that create an object from a json_file"""
import json


def load_from_json_file(filename):
    """Create an object from a json_file"""
    with open(filename) as myFile:
        return json.load(myFile)
