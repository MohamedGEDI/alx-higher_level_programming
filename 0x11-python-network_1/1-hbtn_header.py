#!/usr/bin/python3


"""get header corresponding to the one searched"""


import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as responce:
        head = responce.headers['X-Request-Id']
        print(head)
