#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  const reversedArray = [];
  list.forEach((element) => reversedArray.unshift(element));
  return (reversedArray);
};
