#!/usr/bin/python3

import requests
import sys

# Extract username and personal access token from command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Define the GitHub API endpoint for user information
url = 'https://api.github.com/user'

# Send a GET request to the GitHub API with Basic Authentication
response = requests.get(url, auth=(username, password))

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract and print the user ID from the response JSON
    user_id = response.json()['id']
    print("Your GitHub user ID is:", user_id)
else:
    print("Failed to retrieve user information. Status code:", response.status_code)
