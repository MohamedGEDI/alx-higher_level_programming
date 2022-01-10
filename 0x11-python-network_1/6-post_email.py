#!/usr/bin/python3


"""add email param to url"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    responce = requests.post(url, params=params)
    head = responce.text
    print(head)
