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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must > 0")
