#!/bin/bash

# Check if the URL and filename arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

url=$1
filename=$2

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' not found"
    exit 1
fi

# Send a JSON POST request with the file contents as the body
response=$(curl -s -X POST -H "Content-Type: application/json" --data-binary "@$filename" "$url")

# Display the response body
echo "$response"
