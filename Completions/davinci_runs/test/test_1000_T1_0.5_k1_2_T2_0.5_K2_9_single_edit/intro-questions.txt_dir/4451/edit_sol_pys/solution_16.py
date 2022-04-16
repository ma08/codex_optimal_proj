// const fs = require('fs');
// const path = require('path');

// const srcPath = path.join(__dirname, 'src');
// const distPath = path.join(__dirname, 'dist');

// function copyDir(src, dist) {
//   if (!fs.existsSync(dist)) {
//     fs.mkdirSync(dist);
//   }

//   fs.readdirSync(src).forEach((file) => {
//     const _src = path.join(src, file);
//     const _dist = path.join(dist, file);
//     const stat = fs.statSync(_src);

//     if (stat.isFile()) {
//       fs.writeFileSync(_dist, fs.readFileSync(_src));
//     } else if (stat.isDirectory()) {
//       copyDir(_src, _dist);
//     }
//   });
// }

// copyDir(srcPath, distPath);


// const fs = require('fs');
// const path = require('path');

// const srcPath = path.join(__dirname, 'src');
// const distPath = path.join(__dirname, 'dist');

// function copyDir(src, dist) {
//   if (!fs.existsSync(dist)) {
//     fs.mkdirSync(dist);
//   }

//   fs.readdirSync(src).forEach((file) => {
//     const _src = path.join(src, file);
//     const _dist = path.join(dist, file);
//     const stat = fs.statSync(_src);

//     if (stat.isFile()) {
//       fs.writeFileSync(_dist, fs.readFileSync(_src));
//     } else if (stat.isDirectory()) {
//       copyDir(_src, _dist);
//     }
//   });
// }

// copyDir(srcPath, distPath);

// const fs = require('fs');
// const path = require('path');

// const srcPath = path.join(__dirname, 'src');
// const distPath = path.join(__dirname, 'dist');

// function copyDir(src, dist) {
//   if (!fs.existsSync(dist)) {
//     fs.mkdirSync(dist);
//   }

//   fs.readdirSync(src).forEach((file) => {
//     const _src = path.join(src, file);
//     const _dist = path.join(dist, file);
//     const stat = fs.statSync(_src);

//     if (stat.isFile()) {
//       fs.writeFileSync(_dist, fs.readFileSync(_src));
//     } else if (stat.isDirectory()) {
//       copyDir(_src, _dist);
//     }
//   });
// }

// copyDir(srcPath, distPath);

// const fs = require('fs');
// const path = require('path');

// const srcPath = path.join(__dirname, 'src');
// const distPath = path.join(__dirname, 'dist');

// function copyDir(src, dist) {
//   if (!fs.existsSync(dist)) {
//     fs.mkdirSync(dist);
//   }

//   fs.readdirSync(src).forEach((file) => {
//     const _src = path.join(src, file);
//     const _dist = path.join(dist, file);
//     const stat = fs.statSync(_src);

//     if (stat.isFile()) {
//       fs.writeFileSync(_dist, fs.readFileSync(_src));
//     } else if (stat.isDirectory()) {
//       copyDir(_src, _dist);
//     }
//   });
// }

// copyDir(srcPath, distPath);

// const fs = require('fs');
// const path = require('path');

// const srcPath = path.join(__dirname, 'src');
// const distPath = path.join(__dirname, 'dist');

// function copyDir(src, dist) {
//   if (!fs.existsSync(dist)) {
//     fs.mkdirSync(dist);
//   }

//   fs.readdirSync(src).forEach((file) => {
//     const _src = path.join(src, file);
//     const _dist = path.join(dist, file);
//     const stat = fs.statSync(_src);

//     if (stat.isFile()) {
//       fs.writeFileSync(_dist, fs.readFileSync(_src));
//     } else if (stat.isDirectory()) {
//       copyDir(_src, _dist);
//     }
//   });
// }

// copyDir(srcPath, distPath);

// const fs = require('fs');
// const path = require('path');

// const srcPath = path.join(__dirname, 'src');
// const distPath = path.join(__dirname, 'dist');

// function copyDir(src, dist) {
//   if (!fs.existsSync(dist)) {
//     fs.mkdirSync(dist);
//   }

//   fs.readdirSync(src).forEach((file) => {
//     const _src = path.join(src, file);
//     const _dist = path.join(dist, file);
//     const stat = fs.statSync(_src);

//     if (stat.isFile()) {
//       fs.writeFileSync(_dist, fs.readFileSync(_src));
//     } else if (stat.isDirectory()) {
//       copyDir(_src, _dist);
//     }
//   });
// }

// copyDir(srcPath, distPath);

// const fs = require('fs');
// const path = require('path');

// const srcPath = path.join(__dirname, 'src');
// const distPath = path.join(__dirname, 'dist');

// function copyDir(src, dist) {
//   if (!fs.existsSync(dist)) {
//     fs.mkdirSync(dist);
//   }

//   fs.readdirSync(src).forEach((file) => {
//     const _src = path.join(src, file);
//     const _dist = path.join(dist, file);
//     const stat = fs.statSync(_src);

//     if (stat.isFile()) {
//       fs.writeFileSync(_dist, fs.readFileSync(_src));
//     } else if (stat.isDirectory()) {
//       copyDir(_src, _dist);
//     }
//   });
// }

// copyDir(srcPath, distPath);


const fs = require('fs');
const path = require('path');

const srcPath = path.join(__dirname, 'src');
const distPath = path.join(__dirname, 'dist');

function copyDir(src, dist) {
  if (!fs.existsSync(dist)) {
    fs.mkdirSync(dist);
  }

  fs.readdirSync(src).forEach((file) => {
    const _src = path.join(src, file);
    const _dist = path.join(dist, file);
    const stat = fs.statSync(_src);

    if (stat.isFile()) {
      fs.writeFileSync(_dist, fs.readFileSync(_src));
    } else if (stat.isDirectory()) {
      copyDir
