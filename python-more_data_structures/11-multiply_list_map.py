#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    by2 = lambda x : x * number
    new = list(map(by2, my_list))
    return new
