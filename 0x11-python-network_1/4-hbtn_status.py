#!/usr/bin/python3

import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
else:
    print("Error: Failed to fetch URL (HTTP status code {})".format(response.status_code))
