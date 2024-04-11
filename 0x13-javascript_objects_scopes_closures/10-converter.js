#!/usr/bin/node
'use strict';
/* eslint-disable semi */

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
