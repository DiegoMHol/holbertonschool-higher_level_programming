#!/usr/bin/python3
"""module doc"""


class Rectangle:
    """class doc"""
    def __init__(self, width=0, height=0):
        """init doc"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """width getter doc"""
        return self.__width

    @property
    def height(self):
        """height getter doc"""
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
