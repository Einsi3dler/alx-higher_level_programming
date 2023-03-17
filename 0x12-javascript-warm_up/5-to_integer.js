#!/usr/bin/node
const num = process.argv;
if (!isNaN(num[2])) {
  console.log('My number:' + parseInt(num[2]));
} else {
  console.log('Not a number');
}
