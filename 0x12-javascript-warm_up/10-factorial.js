#!/usr/bin/node

const { argv } = require('process');

// script that computes and prints a factorial
const num = parseInt(argv[2]);
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else if (num < 0) {
    return -1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(num));
