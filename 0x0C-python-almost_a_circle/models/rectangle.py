#!/usr/bin/python3
"""
This module contains a single class
"""


from models.base import Base
class Rectangle(Base):
    """
    This class defines a rectangle and inherits id from a base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        intialization, id is from base(parent class) btw
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
