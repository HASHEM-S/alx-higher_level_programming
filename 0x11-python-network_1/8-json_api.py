#!/usr/bin/python3

import requests
import sys

# Set the default value of q to an empty string if no argument is given
q = sys.argv[1] if len(sys.argv) > 1 else ""

# Create a dictionary with the letter parameter
data = {'q': q}

# Send a POST request to the specified URL with the letter as a parameter
response = requests.post("http://0.0.0.0:5000/search_user", data=data)

# Check if the response body is properly JSON formatted and not empty
try:
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
