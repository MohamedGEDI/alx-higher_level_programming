#!/usr/bin/python3


""" Show body of url using requests"""


if __name__ == "__main__":
    import requests
    responce = requests.get('https://intranet.hbtn.io/status')
    html = responce.text
    print('''
Body response:
    - type: {}
    - content: {}'''.format(type(html), html))
