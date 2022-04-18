// file.js
const fs = require('fs');
const path = require('path');

module.exports = {
  /**
   * @param {string} dirname
   * @returns {string[]}
   */
  readdirRecursiveSync: dirname => {
    let results = [];

    fs.readdirSync(dirname).forEach(file => {
      file = path.resolve(dirname, file);
      const stat = fs.statSync(file);

      if (stat && stat.isDirectory()) {
        results = results.concat(module.exports.readdirRecursiveSync(file));
      } else {
        results.push(file);
      }
    });

    return results;
  }
};
