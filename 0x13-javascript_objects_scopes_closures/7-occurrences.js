#!/usr/bin/node
'use strict';
/* eslint-disable semi */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};

