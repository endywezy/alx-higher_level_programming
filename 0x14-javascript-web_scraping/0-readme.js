#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/posts/1';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('Status Code:', response && response.statusCode);
  console.log('Body:', body);
});
