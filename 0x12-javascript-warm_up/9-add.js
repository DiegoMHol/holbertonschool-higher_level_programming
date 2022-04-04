#!/usr/bin/node
const args = process.argv;
const first = parseInt(args[2]);
const second = parseInt(args[3]);
function add (first, second) {
	console.log(first + second);
}
add(first, second);
