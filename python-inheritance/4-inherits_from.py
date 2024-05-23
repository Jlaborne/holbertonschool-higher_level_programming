#!/usr/bin/python3
"""Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: an object
        a_class: a specified class

    Return:
        True if the object is an instance of a class directly or not
        False otherwise
    """
    return isinstance(obj, a_class)
