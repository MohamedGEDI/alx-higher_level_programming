#!/usr/bin/python3
"""Simple addition function"""


def add_integer(a, b=98):
    """THis fucntion takes one mandatory argument and one optional
    arguments can be int or float, if float change to int
    args:
        a (union[int, flot]): first number
        b (union[int, flot]): second number
    result:
        summation of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
