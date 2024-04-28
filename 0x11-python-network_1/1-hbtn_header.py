#!/usr/bin/python3

import urllib.request
import sys

# Extract the URL from command line arguments
url = sys.argv[1]

# Send a request to the URL
req = urllib.request.Request(url)

# Retrieve the response
with urllib.request.urlopen(req) as response:
    # Check if the 'X-Request-Id' header exists in the response
    if 'X-Request-Id' in response.headers:
        # Print the value of 'X-Request-Id' header
        print(response.headers['X-Request-Id'])
    else:
        print("X-Request-Id header not found in the response")
