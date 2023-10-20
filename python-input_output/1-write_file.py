#!/usr/bin/python3
"""
module write to a file
"""


def write_file(filename="", text=""):
    """"
    a function tha writes a string to a text file
    and returrns the number of characters
    """
    with open(filename, 'w') as fd:
        return (fd.write(text))
