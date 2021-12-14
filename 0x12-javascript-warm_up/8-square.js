#!/usr/bin/node
let j = 0;
const string = 'X';
if (process.argv[2]) {
  const number = parseInt(process.argv[2]);
  if (isNaN(number) === false) {
    for (; j < number; j++) {
      console.log(string.repeat(number));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
