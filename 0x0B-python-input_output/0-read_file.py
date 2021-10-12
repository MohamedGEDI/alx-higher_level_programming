#!/usr/bin/python3
"""create functin to read file """
def read_file(filename=""):
    """read file and print to stdout"""
    with open(filename) as f:
        text = f.read()
    print(text, end="")
