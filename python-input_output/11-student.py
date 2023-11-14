#!/usr/bin/python3
""" module
Student to JSON """
import json as js

class Student:
    """ crate class student with:
        public instance attributes:
            first_name, last_name, age
        public method to_json:
            only attribute names contained in this list will be retrieved
            if atrrs is none: all attributes will be retrieved
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            filtered = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered

    def reload_from_json(self, json):
        """relode from json"""
        for k, v in json.items():
            setattr(self, k, v)
