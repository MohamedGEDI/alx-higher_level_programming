#!/usr/bin/python3


"""Use github PAT to get id"""


import requests
import sys


if __name__ == "__main__":
    with requests.get(f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits',) as response:
        if response.status_code == 200:
            r_dict = response.json()

            for i in range(0, 10):
                print("{}: {}".format(r_dict[i]['sha'], r_dict[i]['commit']['author']['name']))
        else:
            print("None")
