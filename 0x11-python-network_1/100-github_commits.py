#!/usr/bin/python3

import requests
import sys

# Extract repository name and owner name from command line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# GitHub API endpoint for retrieving commits
url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

# Send GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the list of commits from the response JSON
    commits = response.json()

    # Iterate over the 10 most recent commits
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    print("Failed to retrieve commits. Status code:", response.status_code)
