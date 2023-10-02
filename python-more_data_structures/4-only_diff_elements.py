#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    
    for i in set_1:
        if (i not in set_2) and (i not in diff):
            diff.add(i)
    return diff
