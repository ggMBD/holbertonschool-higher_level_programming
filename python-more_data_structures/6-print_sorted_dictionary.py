#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:

        sorted_dictionary = dict(sorted(a_dictionary.items()))

        for key, value in sorted_dictionary.items():
            print("{}: {}".format(key, value))
