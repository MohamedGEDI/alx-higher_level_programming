#!/usr/bin/python3
"""create functin to read file """
def read_file(filename=""):
    with open(filename) as f:
        print(f.read())
