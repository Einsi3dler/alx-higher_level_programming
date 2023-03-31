#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -siLX OPTIONS "$1" | grep "Allow" | awk -F ':' '{print $2}'
