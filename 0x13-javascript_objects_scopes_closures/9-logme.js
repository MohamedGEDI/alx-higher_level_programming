#!/usr/bin/node
exports.logMe = function (item) {
  item.forEach((data, index) => {
    console.log(index + ": " + data);
    });
};
