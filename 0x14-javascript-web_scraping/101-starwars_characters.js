#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    const fetchCharacterData = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            resolve(JSON.parse(charBody).name);
          }
        });
      });
    };

    const fetchAllCharacters = async () => {
      const characters = [];
      for (const characterUrl of characterUrls) {
        const characterName = await fetchCharacterData(characterUrl);
        characters.push(characterName);
      }
      return characters;
    };

    fetchAllCharacters()
      .then(characters => {
        characters.forEach(character => {
          console.log(character);
        });
      })
      .catch(err => {
        console.error('Error fetching character data:', err);
      });
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});
