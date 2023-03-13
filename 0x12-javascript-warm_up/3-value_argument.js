#!/usr/bin/node
// script that prints the first argument passed to it
const { argv } = require('node:process');

if (typeof process.argv[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
