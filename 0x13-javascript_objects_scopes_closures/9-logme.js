#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value
let count = 0;

const logMe = (item) => {
  console.log(`${count}: ${item}`);
  count++;
};
module.exports = { logMe };
