#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me & get respond with a message containing You got me
curl -sL -X PUT -H "Origin: X-School" -d "user_id=98" 0.0.0.0:5000/catch_me
