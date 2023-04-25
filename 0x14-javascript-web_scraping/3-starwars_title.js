#!/usr/bin/node
// script that prints the title of a Star Wars movie 
// where the episode number matches a given integer
const { argv } = require('process');
const request = require('request');
let api = 'https://swapi-api.alx-tools.com/api/films/' + argv[2]
request(api, (err, response, body) => {
  if (err) throw err;
  else {
    console.log(JSON.parse(body).title);
  }
});
