#!/usr/bin/node
// class Square that defines a square and inherits from Square
const SquareP = require('./5-square');

class Square extends SquareP {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    let i = 0;
    while (i < this.size) {
      console.log(c.repeat(this.size));
      i++;
    }
  }
}
module.exports = Square;
