#!/bin/bash
#Displays size of body of the response.
curl -sI curl -sI https://example.com | awk '/Content-Length/ {print $2}'

