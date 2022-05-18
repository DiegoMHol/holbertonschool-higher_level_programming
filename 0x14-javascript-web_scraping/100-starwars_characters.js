#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const urlstar = 'https://swapi-api.hbtn.io/api/films';

request(urlstar, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body).results[argv[2] - 1];
  const characters = movie.characters;
  for (const char of characters) {
    request(char, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
