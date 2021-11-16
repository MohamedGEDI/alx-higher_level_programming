#!/usr/bin/python3
"""class student"""


class Student:
    """initiate the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return attr.__dict__
        except Exception:
            return attr.__dict__
        my_dict = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                my_dict[k] = v
        return my_dict
