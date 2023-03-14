#!/usr/bin/node
// function that returns the number of occurrences in a list
const nbOccurences = (list, searchElement) => list.filter((element) => searchElement === element).length;

module.exports = { nbOccurences };
