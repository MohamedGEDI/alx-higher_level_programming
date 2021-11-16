#!/usr/bin/python3
"""print #in square format """


def print_square(size):
    """function to print # in a square fashion
    arg:
       size of square
    result:
       size shaped square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print('#' * size)
