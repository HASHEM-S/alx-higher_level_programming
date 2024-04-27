#!/usr/bin/python3

# Check if a URL is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and get the size of the response body in bytes
response=$(curl -sI "$1")
size=$(echo "$response" | grep -i Content-Length | awk '{print $2}')

# Check if Content-Length header exists
if [ -z "$size" ]; then
    echo "Error: Content-Length header not found in the response."
else
    echo "Size of the response body: $size bytes"
fi
