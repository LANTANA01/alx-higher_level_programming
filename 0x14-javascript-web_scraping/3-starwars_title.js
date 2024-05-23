#!/usr/bin/node
/* A script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.  */

const request = require('request');
const episodeNumb = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

request(URL + episodeNumb, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
