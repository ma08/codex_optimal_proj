const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

const filePath = path.join(__dirname, './file.txt');

const read = async () => {
  const data = await readFile(filePath, 'utf8');
  console.log(data);
};

const write = async () => {
  const data = await readFile(filePath, 'utf8');
  const newData = `${data} \n new data`;
  await writeFile(filePath, newData);
};

const remove = async () => {
  await fs.unlink(filePath, (err) => {
    if (err) {
      console.log(err);
    }
  });
};

const rename = async () => {
  await fs.rename(filePath, './file-renamed.txt', (err) => {
    if (err) {
      console.log(err);
    }
  });
};

// read();
// write();
// remove();
rename();
