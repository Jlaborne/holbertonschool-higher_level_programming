#!/usr/bin/python3
"""Function that return a list of available attributes/method of an object"""

def lookup(obj):
    """
    Args:
        obj: Object to return the list of attributes
    Return: 
        li: the list that contain attributes/method
    """
    li = dir(obj)
    return (li)
