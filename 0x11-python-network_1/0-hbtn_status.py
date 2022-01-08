#!/usr/bin/python3


""" Show body of url"""


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as responce
        html = responce.read()
        print(html)
