#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL argument
url=$1

# Variables for POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request with curl, including email and subject variables
response=$(curl -s -X POST -d "email=$email&subject=$subject" $url)

# Display the body of the response
echo "$response"
