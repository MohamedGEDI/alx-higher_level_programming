#!/usr/bin/python3


"""add email param to url"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    query = parse.urlencode(params)
    query = query.encode('ascii')
    url = urllib.request.Request(argv[1], query)
    with urllib.request.urlopen(url) as responce:
        head = responce.read().decode("utf-8")
        print(head)
