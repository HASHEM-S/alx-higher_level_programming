#!/usr/bin/node
'use strict';
/* eslint-disable semi */

const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const value = dict[key];
    if (!newDict[value]) {
      newDict[value] = [key];
    } else {
      newDict[value].push(key);
    }
  }
}

console.log(newDict);
