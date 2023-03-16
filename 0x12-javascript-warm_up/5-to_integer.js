#!/usr/bin/node
var num = process.argv;
if (!isNaN(num[2]))
{
	console.log('My number:' + int (num[2]));
}
else
{
	console.log('Not a number');
}
