#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const fs = require('fs');

request(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(argv[3], body, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
