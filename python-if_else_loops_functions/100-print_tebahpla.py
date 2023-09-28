#!/usr/bin/python3
for char in range(122, 98, -1):
    print("{}".format(chr(char) if char % 2 == 0 else chr(char - 32)), end="")
