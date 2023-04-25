#!/usr/bin/node
// script that reads and prints the content of a file.
const { argv } = require('process');

    const fs = require('fs')
    fs.readFile(argv[2], 'utf-8',(err, inputD) => {
       if (err) throw err;
          console.log(inputD.toString());
    })
