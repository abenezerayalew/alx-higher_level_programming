#!/usr/bin/node
// script that writes a string to a file.
const { argv } = require('process');
const request = require('request');
const fs = require('fs');
const url = argv[2];

request(url, (err, response, body) => {
  if (err) throw err;
  else {
    const fInput = argv[3];
    fs.writeFile(fInput, body, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});
