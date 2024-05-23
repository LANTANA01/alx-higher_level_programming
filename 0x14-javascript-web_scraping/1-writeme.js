#!/usr/bin/node
/*Write a string into a file using argv */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (error) =>
	error ? console.error(`Error: ${error}`) : console.log('File written successfully!'));
