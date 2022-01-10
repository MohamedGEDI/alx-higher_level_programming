#!/usr/bin/python3


""" catch errors of url"""


import urllib.request
import sys


if __name__ == "__main__":
    """Try except block to catch errors"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
