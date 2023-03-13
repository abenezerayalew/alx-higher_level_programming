#!/usr/bin/node

const { argv } = require("process")

//script that prints My number: <first argument converted in integer> 
// if the first argument can be converted to an integer
let num = parseInt(argv[2]);

if (isNaN(num))
{
    console.log("Not a number");
}
else
{
    console.log("My number: " + num);
}
