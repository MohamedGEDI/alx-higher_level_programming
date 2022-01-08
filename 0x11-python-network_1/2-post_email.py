#!/usr/bin/python3


"""add email param to url"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    query = parse.urlencode(params)
    with urllib.request.urlopen(sys.argv[1] + '?' + query) as responce:
        head = responce.read().decode("utf-8")
        print(head)

