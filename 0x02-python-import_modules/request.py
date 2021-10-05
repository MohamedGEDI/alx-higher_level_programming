#!/usr/bin/python3
import urllib.request
url = "http://127.0.0.1:8082"
for x in range(5500, 5600):
    hdr = {"x-api-key": 'x'}
    req = urllib.request.Request(url, hdr)
    response = urllib.request.urlopen(req)
     
    print(response.read())
