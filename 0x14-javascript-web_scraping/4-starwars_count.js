#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  films.forEach(film => {
    film.characters.forEach(characterUrl => {
      if (characterUrl.includes('/18/')) {
        count++;
      }
    });
  });

  console.log(count);
});
