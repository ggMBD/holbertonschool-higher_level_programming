#!/usr/bin/python
"""
module for Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object with the specified
        width, height, x, y, and optional id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width of the rectangle.

        :return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The new width for the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        :return: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: The new height for the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
        Get the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x
        """
        self.__x = value

    @property
    def y(self):
        """
        Get the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y
        """
        self.__y = value
