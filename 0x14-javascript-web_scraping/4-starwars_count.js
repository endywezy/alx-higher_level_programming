#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.some(url => url.includes(`/${wedgeId}/`))) {
        count++;
      }
    });

    console.log(count);
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});
