#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const urlstar = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(urlstar, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
