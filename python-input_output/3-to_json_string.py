#!/usr/bin/python3
"""
json representation module
"""
import json


def to_json_string(my_obj):
    """"
    function that returs the JSON representation
    of an object(string)
    """
    return (json.dumps(my_obj))
