#!/usr/bin/python3


"""get header corresponding to the one searched usint requests"""


import requests
import sys


if __name__ == "__main__":
    with requests.get(sys.argv[1]) as responce:
        head = responce.headers['X-Request-Id']
        print(head)
