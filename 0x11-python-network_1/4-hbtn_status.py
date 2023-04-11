#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    link_res = requests.get(link)
    raw_data = link_res.content
    data = raw_data.decode()
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
