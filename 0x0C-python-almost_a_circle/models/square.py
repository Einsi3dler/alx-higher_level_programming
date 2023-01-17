#!/usr/bin/python3
"""
This contains a single class
"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """
    This class inherits from another prewritten class named Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        does most of the ini from the super class
        """
        super(Square, self).__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        this returns the value for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates square value
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return 
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except:
            pass

    def to_dictionary(self):
        """
        this in tes
        """
        return {"id": getattr(self, "id"),
                "size": getattr(self, "width"),
                "x": getattr(self, "x"),
                "y": getattr(self, "y")}

    def __str__(self):
        """
        print a representation of the square like this\
                [Square] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
