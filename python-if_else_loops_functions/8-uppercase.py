#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str) - 1):
        print("{}".format(chr(ord(str[i]) - 32)if ord(str[i])
                          in range(97, 123) else str[i]), end='')
    print("{}".format(chr(ord(str[i+1]) - 32) if ord(str[i+1])
                      in range(97, 123) else str[i+1]), end="\n")
