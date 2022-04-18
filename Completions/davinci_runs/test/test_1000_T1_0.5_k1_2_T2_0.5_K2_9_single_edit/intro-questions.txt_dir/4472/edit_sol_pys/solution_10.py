// file.js
import fs from 'fs';

export default {
  readFile: (path, callback) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        console.error(err);
        return;
      }
      callback(data);
    });
  },

  writeFile: (path, data, callback) => {
    fs.writeFile(path, data, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      callback();
    });
  }
}
