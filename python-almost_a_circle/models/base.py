#!/usr/bin/python3
"""
module Base class
"""


class Base:
    """
    This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = 0
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id
