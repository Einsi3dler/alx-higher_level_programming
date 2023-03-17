#!/usr/bin/node
const num = process.argv;
const str = 'X';
if (!isNaN(num[2])) {
  for (let x = 0; x < parseInt(num[2]); x++) {
    console.log(str.repeat(parseInt(num[2])));
  }
} else {
  console.log('Missing size');
}
