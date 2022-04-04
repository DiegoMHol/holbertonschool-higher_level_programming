#!/usr/bin/node
const args = process.argv;
const counter = parseInt(args[2]);
if (isNaN(counter)) {
  console.log('Missing number of occurrences');
}
for (let index = 0; index < counter; index++) {
  console.log('C is fun');
}
