#!/usr/bin/node

const { argv } = require('process');
const argc = argv.length;

if (argc <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
