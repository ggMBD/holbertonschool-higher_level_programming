#!/usr/bin/python3
def uppercase(str):
    upp = ""
    for char in str:
        if 'a' <= char <= 'z':
            upchar = chr(ord(char) - 32)
        else:
            upchar = char
        upp += upchar
    print("{}".format(upp))
