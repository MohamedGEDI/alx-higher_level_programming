#!/usr/bin/python3
"""create functin to read file """
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
