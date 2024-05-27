#!/usr/bin/python3
"""Define a json to object function"""
import json


def from_json_string(my_str):
    """Return the python object representation"""
    return json.loads(my_str)
