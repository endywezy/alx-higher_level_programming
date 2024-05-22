#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes(wedgeUrl)) {
      count++;
    }
  });

  console.log(count);
});
