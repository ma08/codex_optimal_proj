// function readFile(file, onSuccess) {
//   fs.readFile(file, function(err, content) {
//     if (err) {
//       return console.log(err);
//     }
//     onSuccess(content);
//   });
// }

// function writeFile(file, content, onSuccess) {
//   fs.writeFile(file, content, function(err) {
//     if (err) {
//       return console.log(err);
//     }
//     onSuccess(content);
//   });
// }

// function appendFile(file, content, onSuccess) {
//   fs.appendFile(file, content, function(err) {
//     if (err) {
//       return console.log(err);
//     }
//     onSuccess(content);
//   });
// }

// function readFilePromise(file) {
//   return new Promise(function(resolve, reject) {
//     fs.readFile(file, function(err, content) {
//       if (err) {
//         reject(err);
//       }
//       resolve(content);
//     });
//   });
// }

// function writeFilePromise(file, content) {
//   return new Promise(function(resolve, reject) {
//     fs.writeFile(file, content, function(err) {
//       if (err) {
//         reject(err);
//       }
//       resolve(content);
//     });
//   });
// }

// function appendFilePromise(file, content) {
//   return new Promise(function(resolve, reject) {
//     fs.appendFile(file, content, function(err) {
//       if (err) {
//         reject(err);
//       }
//       resolve(content);
//     });
//   });
// }

// readFilePromise(file).then(function(content) {
//   console.log(content);
// });

// readFilePromise(file)
//   .then(function(content) {
//     return writeFilePromise(file, content + '\nHello');
//   })
//   .then(function(content) {
//     console.log(content);
//   })
//   .catch(function(err) {
//     console.log(err);
//   });

// readFilePromise(file)
//   .then(function(content) {
//     return appendFilePromise(file, content + '\nHello');
//   })
//   .then(function(content) {
//     console.log(content);
//   })
//   .catch(function(err) {
//     console.log(err);
//   });

// Promise.all([readFilePromise(file), readFilePromise(file)]).then(function(
//   contents
// ) {
//   // console.log(contents);
// });

// Promise.race([readFilePromise(file), readFilePromise(file)]).then(function(
//   firstContent
// ) {
//   console.log(firstContent);
// });

// async function readFileAsync(file) {
//   const content = await readFilePromise(file);
//   console.log(content);
// }

// readFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await writeFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await appendFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await writeFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await appendFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await writeFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await appendFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await writeFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await appendFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await writeFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await appendFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await writeFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);

// async function readWriteFileAsync(file) {
//   const content = await readFilePromise(file);
//   await appendFilePromise(file, content + '\nHello');
//   console.log(content);
// }

// readWriteFileAsync(file);
