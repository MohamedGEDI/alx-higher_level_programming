#!/usr/bin/node
const language = 'C is fun';
let i = 0;
if (process.argv[2]) {
  while (i < process.argv[2]) {
    console.log(language);
    i += 1;
  }
} else { console.log('Missing number of occurences'); }
