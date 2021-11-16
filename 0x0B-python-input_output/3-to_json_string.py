#!/usr/bin/python3
"""string to json"""


import json


def to_json_string(my_obj):
    """fuction to convert string to json"""
    x = json.dumps(my_obj)
    return x
