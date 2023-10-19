#!/usr/bin/python3
""" module square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ create square inheritance from\
        class Rectangle inheritance from class BaseGeometry"""
    def __init__(self, size):
        """ initialize new square with size """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ return the area of square """
        return self.__size ** 2
