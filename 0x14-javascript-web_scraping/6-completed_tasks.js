#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const { argv } = require('process');
const request = require('request');
const url = argv[2];

request(url, (err, response, body) => {
  if (err) throw err;
  else {
    const dict = JSON.parse(body).reduce((acc, elem) => {
      if (!acc[elem.userId]) {
        if (elem.completed) {
          acc[elem.userId] = 1;
        }
      } else {
        if (elem.completed) {
          acc[elem.userId] += 1;
        }
      }
      return acc;
    }, {});
    console.log(dict);
  }
});
