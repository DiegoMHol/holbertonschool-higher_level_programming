#!/usr/bin/node
const args = process.argv;
if (args.length < 2 || isNaN(parseInt(args[2]))) {
	console.log(factorial(1));
}else{
	console.log(factorial(parseInt(args[2])));
}
function factorial(n) {
	if (n < 0)
		return;
	if (n === 1)
		return 1;
	return n * factorial(n - 1);
}
