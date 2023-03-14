#!/usr/bin/node
// class Square that defines a square and inherits from Square
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c = 'X') {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}
module.exports = Square;
