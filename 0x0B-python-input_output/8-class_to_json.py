#!/usr/bin/python3
"""simple dictionary of objects"""


def class_to_json(obj):
    """func to turn a class dict to json """
    return obj.__dict__
