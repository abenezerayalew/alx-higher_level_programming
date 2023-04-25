#!/usr/bin/node
// script that prints the number of movies
//  where the character “Wedge Antilles” is present
const { argv } = require('process');
const request = require('request');
const api = argv[2];
request(api, (err, response, body) => {
  if (err) throw err;
  else {
    const id = JSON.parse(body).results.filter((elem) => {
      return elem.characters.filter((url) => { return url.includes('18'); }).length;
    }).length;
    console.log(id);
  }
});
