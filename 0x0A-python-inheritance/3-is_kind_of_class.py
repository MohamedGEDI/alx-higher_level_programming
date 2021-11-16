#!/usr/bin/python3
"""check if is sclass"""


def is_kind_of_class(obj, a_class):
    """check if is instance of """
    if isinstance(obj, a_class):
        return True
    else:
        return False
