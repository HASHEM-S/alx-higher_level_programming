#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys

# Extract URL and email from command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Encode the email as URL parameters
data = urllib.parse.urlencode({'email': email})
data = data.encode('ascii')  # Data should be bytes

# Send a POST request to the URL with email as parameter
req = urllib.request.Request(url, data)

# Retrieve the response
with urllib.request.urlopen(req) as response:
    # Read and decode the body of the response
    body = response.read().decode('utf-8')
    print(body)
