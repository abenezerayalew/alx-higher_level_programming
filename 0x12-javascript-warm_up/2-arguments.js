#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
const { argv } = require('process');
const argc = argv.length;

if (argc === 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
