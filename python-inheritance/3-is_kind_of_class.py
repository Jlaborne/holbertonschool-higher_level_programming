#!/usr/bin/python3
"""Check if the object is an instance of, or if the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or its subclass.
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
    
    Returns:
        True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
