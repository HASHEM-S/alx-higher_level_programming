#!/bin/bash

# Check if a URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request using curl
response=$(curl -s -X DELETE "$1")

# Display the body of the response
echo "$response"
