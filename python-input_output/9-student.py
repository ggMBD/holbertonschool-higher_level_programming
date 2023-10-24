#!/usr/bin/python3
""" module
Student to JSON """


class Student:
    """ crate class student with:
        public instance attributes:
            first_name, last_name, age
        public method to_json:
            retrieves a dictionary representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
