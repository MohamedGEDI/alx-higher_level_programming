#!/usr/bin/python3
"""file to json file"""


import json


def load_from_json_file(filename=""):
    """normal file to json file """
    with open(filename, "r", encoding="utf-8") as f:
        text = json.load(f)
    return text
