#!/usr/bin/python3
def common_elements(set_1, set_2):
    com = set()

    for i in set_1:
        if (i in set_2) and (i not in com):
            com.add(i)
    return com
