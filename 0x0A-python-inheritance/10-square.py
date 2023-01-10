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
        super().__init__(size, size)
        self.__size = size
        self.area()
