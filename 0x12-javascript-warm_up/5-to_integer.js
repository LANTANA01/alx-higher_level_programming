#!/usr/bin/node
// Print a number if argv is a num, else print NaN

if (process.argv[2] == null || isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:',parseInt(process.argv[2]));
}
