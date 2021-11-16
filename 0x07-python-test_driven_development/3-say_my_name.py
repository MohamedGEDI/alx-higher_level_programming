#!/usr/bin/python3
"""3-say_my_name function"""


def say_my_name(first_name, last_name=""):
    """This is function say_my_name
       args:
            first_name - type(str) mandatory
            last_name - type(str) optional
       result:
            print the name out
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
