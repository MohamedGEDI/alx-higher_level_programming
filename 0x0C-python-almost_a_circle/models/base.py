#!/usr/bin/python3
"""Base class """


import json


class Base:
    """contains private class attribute and constructor"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """constructor with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Encode dictionary to json string """
        if list_dictionaries is None:
            return "[]"
        json_string = json.JSONEncoder().encode(list_dictionaries)
        return json_string







