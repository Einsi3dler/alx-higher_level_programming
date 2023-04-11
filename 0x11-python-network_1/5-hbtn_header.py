#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
from sys import argv
import requests

if __name__ == "__main__":
    
    link = argv[1]
    link_req = requests.get(link)
    header = link_req.headers
    xReq = header.get('X-Request-Id')
    print(xReq)
