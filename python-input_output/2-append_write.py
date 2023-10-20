#!/usr/bin/python3
"""
module Append to a file
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of
    a text file and returns the number of charachters added
    """
    with open(filename, mode='a') as fd:
        return (fd.write(text))
