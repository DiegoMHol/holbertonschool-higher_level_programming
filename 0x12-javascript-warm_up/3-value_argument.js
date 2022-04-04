#!/usr/bin/node
const args = process.argv;
let size = 0;
args.forEach(element => {
  size++;
});
if (size <= 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
