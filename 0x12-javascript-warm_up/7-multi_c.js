#!/usr/bin/node
const process = require('process');
let num = parseInt(process.argv[2]);
const message2 = 'C is fun';
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num > 0) {
    console.log(message2);
    num--;
  }
}
