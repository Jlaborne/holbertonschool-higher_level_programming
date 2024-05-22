#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Represent a Rectangle"""
    number_of_instance = 0

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
        """
        Rectangle.number_of_instance += 1
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
        """Area of the rectangle"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return int((self.__width) * 2) + int((self.__height) * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rep = "Rectangle(" + str(self.__width)
        rep += ", " + str(self.__height) + ")"
        return (rep)

    def __del__(self):
        Rectangle.number_of_instance -= 1
        print("Bye rectangle...")
