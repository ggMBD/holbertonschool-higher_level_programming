#!/usr/bin/python3

def remove_char_at(str, n):
    new = ""
    for char in range(len(str)):
        if char != n:
            new += str[char]
    return new
