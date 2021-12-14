#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const string = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(string.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
