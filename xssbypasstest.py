#!/usr/bin/env python
"""
Test for mod_security bypass.
"""
# Standard Python libraries.
import requests

with open('/root/projects/fuzzdb.txt') as f:
    content = f.read().splitlines()

dict = {}
for x in content:
    url = 'http://127.0.0.1/login2.php'
    url = url
    payload = {'username': x, 'password': '1'}
    r = requests.post(url, data=payload)
    dict[x] = r.status_code

for k,v in dict.items():
    if v == 200:
        print(k)
        print('----------------------------------------------')
