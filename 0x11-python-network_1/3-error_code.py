#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    link = argv[1]
    try:
        with request.urlopen(link) as response:
            raw = response.read()
            body = raw.decode('utf-8')
        print(body)
    except error.HTTPError as e:
        print(f"Error Code: {e.code}")
