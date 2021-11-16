#!/usr/bin/python3
"""check if is sclass"""


def inherits_from(obj, a_class):
    """check if is instance of """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
