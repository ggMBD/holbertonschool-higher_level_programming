#!/usr/bin/python3
""" module my list"""


class MyList(list):
    """ create a list """
    def print_sorted(self):
        """ prit list sorted without change the original"""
        tmp = sorted(self)
        print(tmp)
