#!/usr/bin/python3


"""Use github PAT to get id"""


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    responce = requests.get('https://api.github.com/user',
                            auth=(username, password))
    if responce.status_code == 200:
        r_dict = responce.json()
        print(r_dict['id'])
    else:
        print("None")
