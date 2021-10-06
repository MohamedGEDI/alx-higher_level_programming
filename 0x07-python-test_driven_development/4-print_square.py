#!/usr/bin/python3
"""print #in square format """
def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print('#' * size)
