#!/usr/bin/python3
"""string to json"""


import json


def from_json_string(my_str):
    """fuction to convert json to string"""
    x = json.loads(my_str)
    return x
