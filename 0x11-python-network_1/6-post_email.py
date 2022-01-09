#!/usr/bin/python3


"""add email param to url"""


import requests
import sys


if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    with requests.post(sys.argv[1], params=params) as responce:
        head = responce.content.decode("utf-8")
        print(head)
