#!/usr/bin/node
const number = ' My number: ';
const args = process.argv;
const parsei = parseInt(args[2], 10);
if (isNaN(parsei)) {
  console.log('Not a number');
} else {
  console.log(number + parsei);
}
