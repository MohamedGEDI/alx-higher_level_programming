#!/usr/bin/python3
"""file to json file"""


import json


def save_to_json_file(my_obj, filename=""):
    """normal file to json file """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f, ensure_ascii=False)
