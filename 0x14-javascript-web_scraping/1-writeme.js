#!/usr/bin/node

const fs = require('fs');

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
