#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
from sys import argv
import requests

if __name__ == "__main__":

    link = argv[1]
    email = {'email': argv[2]}

    link_post = requests.post(link, data=email)
    print(link_post.text)
