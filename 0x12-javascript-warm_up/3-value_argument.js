#!/usr/bin/node
var myva = process.argv[1]
if (myva == 'undefined')
{
	console.log('No argument')
}
else
{
	console.log(process.argv[2])
}
