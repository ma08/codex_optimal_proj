const fs = require("fs");

module.exports = {
  read: (file) => {
    return new Promise((resolve, reject) => {
      fs.readFile(file, "utf8", (err, data) => {
        if (err) reject(err);
        resolve(data);
      });
    });
  },

  write: (file, data) => {
    return new Promise((resolve, reject) => {
      fs.writeFile(file, data, "utf8", (err) => {
        if (err) reject(err);
        resolve();
      });
    });
  },
};
