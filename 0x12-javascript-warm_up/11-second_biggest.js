#!/usr/bin/node
function myarr (arr) {
  const arrLen = arr.length;
  if (arrLen <= 1) {
    return (0);
  } else {
    arr.sort(function (a, b) { return a - b; });
    return (arr[arrLen - 2]);
  }
}
const val = process.argv;
const valLen = val.length;
const resArr = [];
for (let i = 2; i < valLen; i++) {
  resArr.push(Number(val[i]));
}
console.log(myarr(resArr));
