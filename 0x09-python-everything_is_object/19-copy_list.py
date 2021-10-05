#!/usr/bin/python3
"""Function to copy list"""
def copy_list(my_list):
    """copy list
       args:
            list - anytype
       result:
            new list
    """
    new_list = my_list[:]
    return new_list
