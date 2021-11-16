#!/usr/bin/python3
def max_integer(my_list=[]):
    m = -10
    l = len(my_list)
    if l == 0:
        return None
    for i in range(l):
        if m <= my_list[i]:
            m = my_list[i]
    return m
