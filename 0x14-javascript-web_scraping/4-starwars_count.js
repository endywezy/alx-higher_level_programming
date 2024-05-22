#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the command line argument
const characterId = 18; // Character ID for Wedge Antilles

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode == 200) {
        const filmsData = JSON.parse(body).results;
        let movieCount = 0;

        // Loop through each movie data
        filmsData.forEach((movie) => {
            const characters = movie.characters.map((character) => character.split('/').slice(-2, -1)[0]);
            
            // Check if Wedge Antilles is present in the characters list
            if (characters.includes(characterId.toString())) {
                movieCount++;
            }
        });

        console.log(movieCount);
    } else {
        console.log('Error fetching data from the API');
    }
});
