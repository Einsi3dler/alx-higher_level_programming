#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -X 'POST' -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
