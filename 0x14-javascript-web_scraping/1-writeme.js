#!/usr/bin/node
// script that writes a string to a file.
const { argv } = require('process');

const fs = require('fs');
const fInput = argv[3];
fs.writeFile(argv[2], fInput, 'utf-8', (err) => {
  if (err) throw err;
//   else {
//     console.log('The file is updated with the given data');
//   }
});
