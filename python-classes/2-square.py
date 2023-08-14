#!/usr/bin/env python3
"""
this code asigns the size of a square 0 unless the the user defines it
"""
class Square:
    """
    This class defines a square by a private instance attribute 'size'.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with the given size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """
        this method returns the area of a square once the user enters the size
        Args: 
           size which is a private attribute is taken in

        Returns:
           the value(size) is multiplied by itself 

        """
        return (self.__size * self.__size)
   
