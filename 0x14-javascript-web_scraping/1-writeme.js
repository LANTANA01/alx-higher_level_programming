#!/usr/bin/node
/*Write a string into a file using argv */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
