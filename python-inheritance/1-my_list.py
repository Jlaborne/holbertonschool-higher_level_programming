#!/usr/bin/python3
"""Define a class that inherits from list"""


class MyList(list):
    """
    Args: list
    """

    def print_sorted(self):
        print(sorted(self))
