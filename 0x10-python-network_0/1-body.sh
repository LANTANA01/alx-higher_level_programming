#!/bin/bash
#Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o - -w '%{http_code}' -X GET "$1" 2>/dev/null | awk '/^2[0-9][0-9]/ {print}'
