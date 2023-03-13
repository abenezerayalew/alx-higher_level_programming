#!/usr/bin/node
// script that prints a square

const { argv } = require('process');

const size = parseInt(argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
