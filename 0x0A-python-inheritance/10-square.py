#!/usr/bin/python3
"""
This contains a class that inherits from another class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class inherits from Base Geometry
    """
    def __init__(self, size):
        """
        This intializatiop use a function from the inherited class
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
