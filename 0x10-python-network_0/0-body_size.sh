#!/usr/bin/python3

# Check if the user provided a URL as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and get the response body size in bytes
response=$(curl -sI "$1" | grep -i Content-Length)
size=$(echo "$response" | awk '{print $2}')

# Check if Content-Length header exists
if [ -z "$size" ]; then
    echo "Error: Content-Length header not found in the response."
else
    echo "Size of the response body: $size bytes"
fi
