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
    
    def __str__(self):
        """
        print a representation of the square like this\
                [Square] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
