#!/usr/bin/node
/**
 * 0-starwars_characters.js
 * Algorithm to list out all the characters in a particular star wars
 * movie as listed on the public Star Wars API.
 */
const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (err, res, body) => {
  if (!err) {
    if (res.statusCode === 200) {
      const characterURLs = JSON.parse(body).characters;
      displayCharacterName(characterURLs, 0);
    }
  }
});

function displayCharacterName (characterUrls, index) {
  if (index >= characterUrls.length) return;
  request(characterUrls[index], (err, res, character) => {
    if (!err) {
      if (res.statusCode === 200) {
        console.log(JSON.parse(character).name);
        displayCharacterName(characterUrls, index + 1);
      }
    }
  });
}
