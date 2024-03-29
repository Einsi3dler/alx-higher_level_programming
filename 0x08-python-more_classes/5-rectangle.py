#!/usr/bin/python3
"""
This module contains a single class
"""


class Rectangle:
    """
    This class defines a rectangle by width and height
    """
    def __init__(self, width=0, height=0):
        """
        This instantiates the attribuutes of a class
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Gettter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        returns a string def of the class
        """
        a = self.height
        b = self.width
        res = []
        for y in range(a):
            res.append(b * '#')
        return '\n'.join(str(v)for v in res)

    def __repr__(self):
        """
        returns a represenentation of the class
        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")

    def area(self):
        """
        Calculates area of a rectanlge instance
        """
        return (self.height * self.width)

    def perimeter(self):
        """"
        calculates perimeter of a rectangle instance
        """
        for x in [self.height, self.width]:
            if x == 0:
                return 0
        return (2 * (self.height + self.width))
