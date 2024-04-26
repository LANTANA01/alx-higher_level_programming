#!/bin/bash
#Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -w "%{http_code}\n" -o /dev/null -D - "$1" | grep -q 200 && echo "Route 2"
