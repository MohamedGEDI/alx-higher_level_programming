#!/usr/bin/node
if (process.argv[2])
{
let number = parseInt(process.argv[2]);
if (isNaN(number) === false)
{ console.log("My number: " + number);
}
else
{ console.log("Not a number");
}
}
else
{ console.log("Not a number");
}
