// const fs = require('fs');

// fs.writeFile('./text.txt', 'Hello World!', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         console.log('File successfully created!')
//     }
// });

// fs.readFile('./text.txt', 'utf8', function(err, data){
//     if(err){
//         console.log(err);
//     }else{
//         console.log(data)
//     }
// });

// fs.rename('./text.txt', './hello.txt', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         console.log('File successfully renamed!')
//     }
// });

// fs.appendFile('./hello.txt', '\nHello Again!', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         console.log('File successfully updated!')
//     }
// });

// fs.unlink('./hello.txt', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         console.log('File successfully deleted!')
//     }
// });

// fs.mkdir('tutorial', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         console.log('Folder successfully created!')
//     }
// });

// fs.rmdir('tutorial', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         console.log('Folder successfully deleted!')
//     }
// });

// fs.mkdir('tutorial', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         fs.writeFile('./tutorial/example.txt', '123', function(err){
//             if(err){
//                 console.log(err);
//             }else{
//                 console.log('File successfully created!')
//             }
//         });
//     }
// });

// fs.unlink('./tutorial/example.txt', function(err){
//     if(err){
//         console.log(err);
//     }else{
//         fs.rmdir('tutorial', function(err){
//             if(err){
//                 console.log(err);
//             }else{
//                 console.log('Folder successfully deleted!')
//             }
//         });
//     }
// });

// fs.readdir('example', function(err, files){
//     if(err){
//         console.log(err);
//     }else{
//         console.log(files);
//     }
// });

const fs = require('fs');

fs.readdir('example', function(err, files){
    if(err){
        console.log(err);
    }else{
        for(let file of files){
            fs.unlink('./example/' + file, function(err){
                if(err){
                    console.log(err);
                }else{
                    console.log('File successfully deleted!')
                }
            });
        }
    }
});
