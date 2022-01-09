#!/usr/bin/python3


"""Use github PAT to get id"""


import requests
import sys


if __name__ == "__main__":
    with requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2])) as response:
        r_dict = response.json()
        print(r_dict['id'])
