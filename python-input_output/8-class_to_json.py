#!/usr/bin/python3
""" module class_to_json"""


def class_to_json(obj):
    """
    function that returns the dictionary
    description with simple data structure
    for JSON serialization.
    """
    return obj.__dict__
