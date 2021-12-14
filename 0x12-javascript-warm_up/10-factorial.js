#!/usr/bin/node
function factorial (n) {
  if (n < 1) return 1;
  return n * factorial(n - 1);
}

if (process.argv[2]) {
  const num = parseInt(process.argv[2]);
  console.log(factorial(num));
} else {
  console.log(1);
}
