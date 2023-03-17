#!/usr/bin/node
function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }
  if (a === 0) {
    return (1);
  }
  return a * factorial(a - 1);
}

const val = factorial(Number(process.argv[2]));
console.log(val);
