#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dict = a_dictionary.copy()
    for k, v in copy_dict.items():
        copy_dict[k] = v * 2
    return copy_dict
