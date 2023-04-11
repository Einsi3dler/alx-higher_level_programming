#!/usr/bin/python3
"""
 a Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""
import requests
from sys import argv
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    link = f"https://api.github.com/users/{username}"
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": "Bearer " + password,
               "X-GitHub-Api-Version": "2022-11-28"}
    user_data = requests.get(link, headers=headers)
    api_data = user_data.json()
    api_data.keys()
    if "id" in api_data.keys():
        print(api_data["id"])
    else:
        print(None)
