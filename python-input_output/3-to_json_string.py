#!/usr/bin/python3
"""Define a string to json function"""
import json


def to_json_string(my_obj):
    """Return the json representation"""
    return json.dumps(my_obj)
