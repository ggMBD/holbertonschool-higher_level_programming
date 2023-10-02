#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    tot = 0

    for num in my_list:
        if num not in unique:
            unique.append(num)
            tot += num
    return tot
