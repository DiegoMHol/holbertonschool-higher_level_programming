#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const todos = JSON.parse(body);
  const employeeTasks = {};
  for (const todo of todos) {
    if (todo.completed) {
      if (employeeTasks[todo.userId]) {
        employeeTasks[todo.userId] += 1;
      } else {
        employeeTasks[todo.userId] = 1;
      }
    }
  }
  console.log(employeeTasks);
});
