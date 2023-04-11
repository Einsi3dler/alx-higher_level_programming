#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) """


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    link = argv[1]
    email = {'email':argv[2]}
    email = parse.urlencode(email)
    email = email.encode('ascii')
    link_req = request.Request(link, email)

    with request.urlopen(link_req) as response:
        link_info = response.read()
    val = link_info.decode('utf-8')
    print(val)
