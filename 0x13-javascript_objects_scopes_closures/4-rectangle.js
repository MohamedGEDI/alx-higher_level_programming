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
  
  rotate() {
    let temp;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  
  double() {
    this.width = 2 * this.width
    this.height = 2 * this.height
  }
}

module.exports = Rectangle;
