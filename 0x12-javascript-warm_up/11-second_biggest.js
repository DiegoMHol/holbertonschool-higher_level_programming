#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < args.length; i++) {
    array[i] = parseInt(args[i]);
  }
	array.sort((a, b) => b - a);
	console.log(array[1]);
}
