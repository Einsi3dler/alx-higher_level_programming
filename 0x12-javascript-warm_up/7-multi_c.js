#!/usr/bin/node
const num = process.argv;
const str = 'C is fun';
if (!isNaN(num[2])) {
  for (let x = 0; x < parseInt(num[2]); x++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
