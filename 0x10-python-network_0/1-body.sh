#!/bin/bash
#Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -w "\n" -o /dev/null -D - "$1"

