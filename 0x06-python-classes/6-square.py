#!/usr/bin/python3
"""
This modules contains a single class
"""


class Square:
    """
    This class contains two function
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        this initializes the square and validates the value
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """
        This is a getter method
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        this a setter for position
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int) or (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """
        This is a getter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        this is meant to calculate the general area of a square
        """
        val = self.__size
        return val * val

    def my_print(self):
        """
        This file prints a representation of a square with #
        """
        val = self.__size
        bal = self.__position
        if val == 0:
            print()
            return
        for x in range(val):
            for z in range(bal[0]):
                if bal[1] < 0:
                    print(" ", end="")
                else:
                    print("_", end="")
            for y in range(val):
                print(f"#", end="")
            print()
