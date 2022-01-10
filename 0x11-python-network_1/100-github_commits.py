#!/usr/bin/python3


"""Use github PAT to get id"""
import json

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    params = {
        'per_page': 10,
    }
    response = requests.get(f'https://api.github.com/repos/{user}/{repo}/'
                            f'commits', headers=headers, params=params)
    if response.status_code == 200:
        r_dict = response.json()
        for i in range(1, 10):
            print("{}: {}".format(r_dict[i]['sha'],
                                  r_dict['commit']['author']['name']))
    else:
        print("None")
