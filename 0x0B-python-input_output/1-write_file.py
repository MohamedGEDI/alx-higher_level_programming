#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """function to write a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        text = f.write(text)
    return text
