// function readFile(file) {
//   // return a promise
//   return new Promise((resolve, reject) => {
//     fs.readFile(file, 'utf-8', (err, data) => {
//       if (err) {
//         reject(err);
//         return;
//       }
//       resolve(data);
//     });
//   });
// }
//
// function readAllFiles() {
//   const promises = [];
//   for (let i = 1; i <= 5; i++) {
//     promises.push(readFile(`file${i}.txt`));
//   }
//   return Promise.all(promises);
// }
//
// readAllFiles()
//   .then(data => {
//     console.log(data);
//   })
//   .catch(err => {
//     console.log(err);
//   });

// fs.readFile('file1.txt', 'utf-8', (err, data) => {
//   if (err) {
//     console.log(err);
//     return;
//   }
//   console.log(data);
// });
//
// fs.readFile('file2.txt', 'utf-8', (err, data) => {
//   if (err) {
//     console.log(err);
//     return;
//   }
//   console.log(data);
// });

// fs.readFile('file1.txt', 'utf-8', (err, data) => {
//   if (err) {
//     console.log(err);
//     return;
//   }
//   fs.readFile('file2.txt', 'utf-8', (err, data) => {
//     if (err) {
//       console.log(err);
//       return;
//     }
//     console.log(data);
//   });
// });

// function readFile(file) {
//   // return a promise
//   return new Promise((resolve, reject) => {
//     fs.readFile(file, 'utf-8', (err, data) => {
//       if (err) {
//         reject(err);
//         return;
//       }
//       resolve(data);
//     });
//   });
// }
//
// function readAllFiles() {
//   const promises = [];
//   for (let i = 1; i <= 5; i++) {
//     promises.push(readFile(`file${i}.txt`));
//   }
//   return Promise.all(promises);
// }
//
// readAllFiles()
//   .then(data => {
//     console.log(data);
//   })
//   .catch(err => {
//     console.log(err);
//   });

// const fs = require('fs');
// const util = require('util');
//
// const readFile = util.promisify(fs.readFile);
//
// function readAllFiles() {
//   const promises = [];
//   for (let i = 1; i <= 5; i++) {
//     promises.push(readFile(`file${i}.txt`, 'utf-8'));
//   }
//   return Promise.all(promises);
// }
//
// readAllFiles()
//   .then(data => {
//     console.log(data);
//   })
//   .catch(err => {
//     console.log(err);
//   });

// function readFile(file) {
//   // return a promise
//   return new Promise((resolve, reject) => {
//     fs.readFile(file, 'utf-8', (err, data) => {
//       if (err) {
//         reject(err);
//         return;
//       }
//       resolve(data);
//     });
//   });
// }
//
// function readAllFiles() {
//   const promises = [];
//   for (let i = 1; i <= 5; i++) {
//     promises.push(readFile(`file${i}.txt`));
//   }
//   return Promise.all(promises);
// }
//
// readAllFiles()
//   .then(data => {
//     console.log(data);
//   })
//   .catch(err => {
//     console.log(err);
//   });

// function readFile(file) {
//   // return a promise
//   return new Promise((resolve, reject) => {
//     fs.readFile(file, 'utf-8', (err, data) => {
//       if (err) {
//         reject(err);
//         return;
//       }
//       resolve(data);
//     });
//   });
// }
//
// function readAllFiles() {
//   const promises = [];
//   for (let i = 1; i <= 5; i++) {
//     promises.push(readFile(`file${i}.txt`));
//   }
//   return Promise.all(promises);
// }
//
// readAllFiles()
//   .then(data => {
//     console.log(data);
//   })
//   .catch(err => {
//     console.log(err);
//   });

// function readFile(file) {
//   // return a promise
//   return new Promise((resolve, reject) => {
//     fs.readFile(file, 'utf-8', (err, data) => {
//       if (err) {
//         reject(err);
//         return;
//       }
//       resolve(data);
//     });
//   });
// }
//
// function readAllFiles() {
//   const promises = [];
//   for (let i = 1; i <= 5; i++) {
//     promises.push(readFile(`file${i}.txt`));
//   }
//   return Promise.all(promises);
// }
//
// readAllFiles()
//   .then(data => {
//     console.log(data);
//   })
//   .catch(err => {
//     console.log(err);
//   });

// function readFile(file) {
//   // return a promise
//   return new Promise((resolve, reject) => {
//     fs.readFile(file, 'utf-8', (err, data) => {
//       if (err) {
//         reject(err);
//         return;
//       }
//       resolve(data);
//     });
//   });
// }
//
// function readAllFiles() {
//   const promises = [];
//   for (let i = 1; i <= 5; i++) {
//     promises.push(readFile(`file${i}.txt`));
//   }
//   return Promise.all(promises);
// }
//
// readAllFiles()
//   .then(data => {
//     console.log(data);
//   })
//   .catch(err => {
//     console.log(err);
//   });
