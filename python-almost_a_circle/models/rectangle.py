"""
This module imports Base class from the base module

"""

from models.base import Base
"""
from the module base we imported Base class
"""

class Rectangle(Base):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle's position.
            y: The y-coordinate of the rectangle's position.
            id: The ID of the rectangle.
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        

    @property
    def width(self):
        """
        This getter method is used to retrive values of the attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This setter method modifies the value of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        This getter method is used to retrive values of the attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This setter method modifies the value of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
        

    @property
    def x(self):
        """
        This getter method is used to retrive values of the attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This setter method modifies the value of the y
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        This getter method is used to retrive values of the attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This setter method modifies the value of the y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        this metohod calculates the area using the width and height defined
        """
        return self.__width * self.__height
    
    def display(self):
        """
        this method returns the number of "#" according to the width and height of a rectangle
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        this method overides the other methods above it
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """
        this method assigns an argument to each attribute 
        """
        args_length = len(args)
        kwargs_length = len(kwargs)

        for key, value in kwargs.items():
            if key == "id":
                self.id= value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value


        if args_length > 0:
            self.id = args[0]
        if args_length > 1:
            self.width = args[1]
        if args_length > 2:
            self.height = args[2]
         
        if args_length > 3:
            self.x = args[3]
        if args_length > 4:
            self.y = args[4]

    

