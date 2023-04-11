#!/usr/bin/python3
"""  a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user"""
from sys import argv
import requests

if __name__ == "__main__":

    link = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    response = requests.post(link, data)
    infoDict = response.json()
    if type(infoDict == dict):
        if infoDict.__len__() > 0:
            print(f"[{infoDict['id']}] {infoDict['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
