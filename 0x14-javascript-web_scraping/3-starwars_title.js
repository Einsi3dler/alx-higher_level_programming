#!/usr/bin/node

const request = require('request');
const api_num = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

request(URL + api_num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const response_JSON = JSON.parse(body);
    console.log(response_JSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
