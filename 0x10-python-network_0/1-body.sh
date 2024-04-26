#!/bin/bash
#Takes in a URL, sends a GET request to the URL, and displays the body of the response
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1") && [ "$status_code" -eq 200 ] && echo "Route 2" && curl -s "$1"
