#!/usr/bin/python3
"""Define a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square"""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): the size of the new square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        "return the area of the square"
        return self.__size * self.__size
