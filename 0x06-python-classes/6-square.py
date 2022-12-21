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
        self.size = size
        self.position = position

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
        err = "position must be a tuple of 2 positive integers"
        if type(value) == tuple:
            if len(value) == 2:
                if (type(value[0]) == int) and (type(value[1]) == int):
                    if (value[0] >= 0) and (value[1] >= 0):
                        self.__position = value
                    else:
                        raise TypeError(err)
                else:
                    raise TypeError(err)
            else:
                raise TypeError(err)
        else:
            raise TypeError(err)

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
