const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('What file should I read? ', (answer) => {
  fs.readFile(answer, 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
  });

  rl.close();
});
