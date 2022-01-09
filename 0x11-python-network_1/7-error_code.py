#!/usr/bin/python3


""" catch errors of url"""


import requests
import sys


if __name__ == "__main__":
    """Try except block to catch errors"""
    try:  
        with requests.get(sys.argv[1]) as response:
            html = response.content.decode('utf-8')
            print(html)
    except requests.exceptions.HTTPExceptions as e:
        print("Error code: {}".format(e))
