#!/usr/bin/node
const myva = process.argv;
let len = 0;
for (const x in myva) {
  len = x;
}
if (len <= 1) {
  console.log('No argument');
} else {
  console.log(myva[2]);
}
