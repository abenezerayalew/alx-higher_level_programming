#!/usr/bin/node
// script that prints the addition of 2 integers
const { argv } = require('process');

// script that prints the addition of 2 integers
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  return a + b;
}
if (isNaN(num1) || isNaN(num2)) {
  console.log(NaN);
} else {
  console.log(add(num1, num2));
}
