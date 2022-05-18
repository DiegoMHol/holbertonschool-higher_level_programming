#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movies = JSON.parse(body).results;
  let count = 0;
  for (const movie of movies) {
    const characters = movie.characters;
    for (const character of characters){
      if (character.includes('18')){
	      count++;
      }
    }
  }
  console.log(count);
});
