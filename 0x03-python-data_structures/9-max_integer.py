#!/usr/bin/python3
def max_integer(my_list=[]):
    m = 0
    l = len(my_list)
    for i in range(l):
        if m < my_list[i]:
            m = my_list[i]
    return m
