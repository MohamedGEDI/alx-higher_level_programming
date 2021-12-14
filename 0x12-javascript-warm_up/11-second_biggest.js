#!/usr/bin/node
let max = 0;
let sec = 0;
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > max) {
      sec = max;
      max = num;
    } else if (num > sec) {
      sec = num;
    }
  }
  console.log(sec);
}
