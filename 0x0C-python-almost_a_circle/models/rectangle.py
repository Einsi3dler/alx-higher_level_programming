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
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of the rect
        """
        return self.__width * self.__height

    def display(self):
        """
        representation of the rect in #
        """
        for val in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for num in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        updates the instance
        """
        
        flg = 0
        if (kwargs is not None):
            self.id = kwargs[id]
            self.width = kwargs[width]
            self.height = kwargs[height]
            self.x = kwargs[x]
            self.y = kwargs[y]
        else:
            for val in args:
                if flg == 0:
                    self.id = val
                if flg == 1:
                    self.width = val
                if flg == 2:
                    self.height = val
                if flg == 3:
                    self.x = val
                if flg == 4:
                    self.y = val
                flg = flg + 1


    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
