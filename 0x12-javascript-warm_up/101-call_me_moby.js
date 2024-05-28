#!/usr/bin/node
// Export function

const callMeMoby = (x, theFunction) => {
  for (; x > 0; x--) {
    theFunction();
  }
};

module.exports = { callMeMoby };
