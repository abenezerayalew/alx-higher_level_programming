#!/usr/bin/node

const { argv } = require("process");

//script that prints x times “C is fun”
let x = parseInt(argv[2]);

if (isNaN(x))
{
    console.log("Missing number of occurrences");
}
else
{
    let i = 0;
    while (i < x)
    {
        console.log("C is fun");
        i++;
    }
}