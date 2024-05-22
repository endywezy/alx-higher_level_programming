#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user id
    const completedTasksByUser = {};

    // Loop through the tasks to count completed tasks by user id
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    // Print users with completed tasks
    console.log(completedTasksByUser);
  } else {
    console.log('Error fetching data from the API');
  }
});
