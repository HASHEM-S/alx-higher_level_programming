#!/bin/bash

# Check if a URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request using curl
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Check if the response code is 200 (OK)
if [ "$response" == "200" ]; then
    # Display the body of the response
    curl -s "$1"
else
    echo "Error: HTTP $response"
fi
