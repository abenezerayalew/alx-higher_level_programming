#!/usr/bin/node

const { parse } = require("path");
const { argv } = require("process");

//script that prints the addition of 2 integers
let num1 = parseInt(argv[2]);
let num2 = parseInt(argv[3]);

function add(a,b)
{
  return a + b;
}
if (isNaN(num1))
{
    return console.log(NaN);
}
else
{
    return console.log(add(num1,num2));
}