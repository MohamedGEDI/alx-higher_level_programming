#!/usr/bin/python3


"""add email param to url"""


if __name__ == '__main__':
    import requests
    import sys

    params = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=params)
    print(res.text)