#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(link) as response:
        html = response.read()
        print("Body response:")
        print(f"    -type: {type(html)}")
        print(f"    -content: {html}")
        print(f"    -utf8 content: {html.decode('utf-8')}")
