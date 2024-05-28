#!/usr/bin/node
// Export a function that increments and calls a function

const addMeMaybe = (number, theFunction) => {
  theFunction(number + 1);
};

module.exports = { addMeMaybe };
