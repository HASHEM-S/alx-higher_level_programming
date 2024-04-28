#!/usr/bin/python3

import requests
import sys

# Extract the URL from command line arguments
url = sys.argv[1]

# Send a request to the URL
response = requests.get(url)

# Check if the X-Request-Id header exists in the response
if 'X-Request-Id' in response.headers:
    # Print the value of the X-Request-Id header
    print(response.headers['X-Request-Id'])
else:
    print("X-Request-Id header not found in the response")
