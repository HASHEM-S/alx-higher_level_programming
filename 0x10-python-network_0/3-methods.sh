#!/bin/bash

# Check if a URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send an OPTIONS request to the URL using curl
response=$(curl -s -i -X OPTIONS "$1")

# Extract and display the Allow header from the response
allow_header=$(echo "$response" | grep -i "Allow:")
if [ -n "$allow_header" ]; then
    echo "Allowed HTTP Methods for $1:"
    echo "$allow_header" | sed 's/Allow: //i'
else
    echo "Error: Unable to retrieve Allow header from the server."
fi
