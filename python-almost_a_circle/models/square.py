#!/usr/bin/python3
"""
module for square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return the representation of a square """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Get the size of the square.

        :return: The sire of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The new size for the square.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
