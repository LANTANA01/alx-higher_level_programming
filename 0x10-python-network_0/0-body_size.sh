#!/bin/bash
#Displays size of body of the response.
curl -s "$1" | wc -c

