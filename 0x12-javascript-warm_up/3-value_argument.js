#!/usr/bin/node
// script that prints the first argument passed to it
const { argv } = require('node:process');

const len = 2;

if (process.argv.length <= 2)
{
    console.log("No argument");
}
else
{
    console.log(argv[2]);
}