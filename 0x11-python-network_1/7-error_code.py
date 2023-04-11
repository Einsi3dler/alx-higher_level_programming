#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
from sys import argv
import requests

if __name__ == "__main__":

    link = argv[1]
    r = requests.get(link)
    statCode = r.status_code
    if statCode >= 400:
        print(f"Error code: {statCode}")
    else:
        print(f"{r.content.decode()}")
