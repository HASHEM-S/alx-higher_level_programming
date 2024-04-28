#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Error: URL argument is missing"
    exit 1
fi

# Send a request to the URL and store the response in a temporary file
curl -s -o response.txt -w "%{http_code}" "$1" > /dev/null

# Read the status code from the temporary file and display it
status_code=$(cat response.txt)
echo "Status code: $status_code"

# Clean up the temporary file
rm response.txt
