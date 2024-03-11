#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
let x = 0;
let line = '';
if (num) {
  for (let i = 0; i < num; i++) {
    line += 'X';
  }
  while (x < num) {
    console.log(line);
    x++;
  }
} else {
  console.log('Missing size');
}
