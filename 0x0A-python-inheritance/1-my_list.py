#!/usr/bin/python3
"""create a class that inherits list"""


class MyList(list):
    """function to sort and print array"""
    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
