#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// class Square that defines a square and inherits
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
