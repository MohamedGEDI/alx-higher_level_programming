#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """function to write a file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        text = f.write(text)
    return text
