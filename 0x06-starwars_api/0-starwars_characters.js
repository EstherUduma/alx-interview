#!/usr/bin/env node

const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: ./0-starwars_characters.js <Movie ID>');
    process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error fetching movie data:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
        process.exit(1);
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach(url => {
        request(url, (error, response, body) => {
            if (error) {
                console.error('Error fetching character data:', error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
                return;
            }

            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});
