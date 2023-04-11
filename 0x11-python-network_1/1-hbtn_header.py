#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys
if __name__ == "__main__":
    link = sys.argv[1]
    with urllib.request.urlopen(link) as response:
        colInfo = response.info()
        print(colInfo['X-Request-id'])
