#!/usr/bin/python3
""" module base geometry """


class BaseGeometry:
    """ create class geometry with Public instance method:
    1- area
    2- integer_validator
    """
    def area(self):
        """ raise exception error """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
