#!/usr/bin/python3


""" Show body of url using requests"""


import requests


if __name__ == "__main__":
    responce = requests.get('https://intranet.hbtn.io/status')
    html = response.content.decode('utf-8')
    print('''
Body response:
    - type: {}
    - content: {}'''.format(type(html), html))
