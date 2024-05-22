#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        return int((self.__width) * 2) + int((self.__height) * 2)
