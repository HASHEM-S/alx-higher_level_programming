#!/usr/bin/python3

import requests
import sys

# Extract the URL from command line arguments
url = sys.argv[1]

# Send a request to the URL
response = requests.get(url)

# Check if the HTTP status code is greater than or equal to 400
if response.status_code >= 400:
    # Print error message with HTTP status code
    print("Error code:", response.status_code)
else:
    # Print the body of the response
    print(response.text)
