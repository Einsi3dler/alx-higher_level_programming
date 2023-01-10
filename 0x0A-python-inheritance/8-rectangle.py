#!/usr/bin/python3
"""
This contains a class that inherits from another class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this class inherits from Base Geometry
    """
    def __init__(self, width, height):
        """
        This intializatiop use a function from the inherited class
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
