#!/usr/bin/python3


""" catch errors of url"""


import requests
import sys


if __name__ == "__main__":
    """Try except block to catch errors"""
    res = requests.get(sys.argv[1])
    if res.status_code == 200:
        print(res.text)
    else:
        print(res.status_code)
