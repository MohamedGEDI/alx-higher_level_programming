#!/usr/bin/python3


""" Show body of url using requests"""


import requests


if __name__ == "__main__":
    with requests.get('https://intranet.hbtn.io/status') as response:
        html = response.content.decode('utf-8')
        print('''
Body response:
    - type: {}
    - content: {}
    - utf8 content: 0K'''.format(type(html), html))
