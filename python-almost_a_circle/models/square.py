"""
This module imports the rectangle class
"""
from models.rectangle import Rectangle

"""
imported class rectangle
"""
class Square(Rectangle):
    """
    this class inherits the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This  method takes in the size and cordinate of a square
        """
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        """
        This method overides the other methods
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """
        This getter method is used to retrive values of the attribute width
        """
        return self.width
    @size.setter
    
    def size(self, value):
        """
        This setter method modifies the value of the width
        """
        self.width = value

