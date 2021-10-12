#!/usr/bin/python3
import json
"""string to json"""


def to_json_string(my_obj):
    """fuction to convert string to json"""
    x = json.dumps(my_obj)
    return x
