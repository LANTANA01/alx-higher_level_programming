#!/usr/bin/node
/*a script that gets the contents of a webpage and stores it in a file.
The first argument is the URL to request
The second argument is the file path to store the body response */

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
