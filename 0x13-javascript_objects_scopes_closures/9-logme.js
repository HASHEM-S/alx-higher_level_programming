#!/usr/bin/node
'use strict';
/* eslint-disable semi */

let counter = 0;

exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
