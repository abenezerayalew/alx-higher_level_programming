#!/usr/bin/node
// script that display the status code of a GET request
// const { argv } = require('process');
const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) throw err;
  else {
    console.log('code:', response && response.statusCode);
  }
});
