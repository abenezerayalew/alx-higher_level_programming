#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer
const { argv } = require('process');
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request(api, (err, body) => {
  if (err) throw err;
  else {
    console.log(JSON.parse(body).title);
  }
});
