#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    else:
        n = len(my_list)
        for i in range(n-1, -1, -1):
            print("{:d}".format(my_list[i]))
