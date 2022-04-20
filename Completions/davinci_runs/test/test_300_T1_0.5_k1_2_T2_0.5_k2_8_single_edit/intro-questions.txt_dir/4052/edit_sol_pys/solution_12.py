// var fs = require('fs');
// var path = require('path');
//
// function deleteFolderRecursive(path) {
//   if (fs.existsSync(path)) {
//     fs.readdirSync(path).forEach(function(file, index){
//       var curPath = path + "/" + file;
//       if (fs.lstatSync(curPath).isDirectory()) { // recurse
//         deleteFolderRecursive(curPath);
//       } else { // delete file
//         fs.unlinkSync(curPath);
//       }
//     });
//     fs.rmdirSync(path);
//   }
// };
//
// deleteFolderRecursive('/Users/jason/Desktop/test');
//
// // fs.readdirSync('/Users/jason/Desktop/test').forEach(function(file, index){
// //   var curPath = '/Users/jason/Desktop/test' + "/" + file;
// //   if (fs.lstatSync(curPath).isDirectory()) { // recurse
// //     deleteFolderRecursive(curPath);
// //   } else { // delete file
// //     fs.unlinkSync(curPath);
// //   }
// // });
// // fs.rmdirSync('/Users/jason/Desktop/test');
//
//
//
//
// function deleteFilesInFolder(folder){
//   fs.readdirSync(folder).forEach(function(file, index){
//     var curPath = folder + "/" + file;
//     if (fs.lstatSync(curPath).isDirectory()) { // recurse
//       deleteFolderRecursive(curPath);
//     } else { // delete file
//       fs.unlinkSync(curPath);
//     }
//   });
// }
//
// function deleteFolder(folder){
//   deleteFilesInFolder(folder);
//   fs.rmdirSync(folder);
// }
//
// deleteFolder('/Users/jason/Desktop/test');
//
// // fs.readdirSync('/Users/jason/Desktop/test').forEach(function(file, index){
// //   var curPath = '/Users/jason/Desktop/test' + "/" + file;
// //   if (fs.lstatSync(curPath).isDirectory()) { // recurse
// //     deleteFolderRecursive(curPath);
// //   } else { // delete file
// //     fs.unlinkSync(curPath);
// //   }
// // });
// // fs.rmdirSync('/Users/jason/Desktop/test');
//
//
// function deleteFilesInFolder(folder){
//   fs.readdirSync(folder).forEach(function(file, index){
//     var curPath = folder + "/" + file;
//     if (fs.lstatSync(curPath).isDirectory()) { // recurse
//       deleteFolderRecursive(curPath);
//     } else { // delete file
//       fs.unlinkSync(curPath);
//     }
//   });
// }
//
// function deleteFolder(folder){
//   deleteFilesInFolder(folder);
//   fs.rmdirSync(folder);
// }
//
// deleteFolder('/Users/jason/Desktop/test');
//
// // fs.readdirSync('/Users/jason/Desktop/test').forEach(function(file, index){
// //   var curPath = '/Users/jason/Desktop/test' + "/" + file;
// //   if (fs.lstatSync(curPath).isDirectory()) { // recurse
// //     deleteFolderRecursive(curPath);
// //   } else { // delete file
// //     fs.unlinkSync(curPath);
// //   }
// // });
// // fs.rmdirSync('/Users/jason/Desktop/test');
