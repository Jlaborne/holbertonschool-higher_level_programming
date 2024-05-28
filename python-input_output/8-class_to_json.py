#!/usr/bin/python3
"""Define a function that create an object from a json_file"""


def class_to_json(obj):
    """Return the dictionary description of an object"""
    return obj.__dict__
