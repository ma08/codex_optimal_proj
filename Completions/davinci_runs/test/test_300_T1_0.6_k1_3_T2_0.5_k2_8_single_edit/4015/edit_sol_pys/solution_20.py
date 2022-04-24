const fs = require("fs");

function readFile(path) {
  return new Promise((resolve, reject) => {
    try {
      const result = fs.readFileSync(path, "utf-8");
      resolve(result);
    } catch (error) {
      reject(error);
    }
  });
}

function writeFile(path, content) {
  return new Promise((resolve, reject) => {
    try {
      fs.writeFileSync(path, content);
      resolve();
    } catch (error) {
      reject(error);
    }
  });
}

module.exports = {
  readFile,
  writeFile,
};
