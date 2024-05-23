#!/usr/bin/python3
"""Check if object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    Arg:
        obj: an object
        a_class: a class
    Return:
        True if obj is an instance of the class
        False if not
    """
    return type(obj) is a_class
