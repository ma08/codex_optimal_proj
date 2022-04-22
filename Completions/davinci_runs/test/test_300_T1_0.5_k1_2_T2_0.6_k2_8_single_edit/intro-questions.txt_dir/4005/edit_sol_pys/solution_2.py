// const fs = require('fs');
// fs.readFile('file.js',(err,data) => {
//     if(err) console.log(err);
//     else console.log(data);
// });

// fs.writeFile('file1.txt','hello world',(err)=>{
//     if(err) console.log(err);
//     else console.log('write file success');
// });

// fs.readdir('./',(err,data)=>{
//     if(err) console.log(err);
//     else console.log(data);
// });


const fs = require('fs');
const path = require('path');
// fs.mkdir('folder',(err)=>{
//     if(err) console.log(err);
//     else console.log('success');
// })

// fs.rmdir('folder',(err)=>{
//     if(err) console.log(err);
//     else console.log('success');
// });

// fs.mkdir('./folder/folder1',(err)=>{
//     if(err) console.log(err);
//     else console.log('success');
// });

// fs.unlink('./folder/folder1/file.js',(err)=>{
//     if(err) console.log(err);
//     else console.log('success');
// });

// fs.readdir('./folder',(err,data)=>{
//     if(err) console.log(err);
//     else console.log(data);
// });

// fs.readdir('./folder',(err,data)=>{
//     if(err) console.log(err);
//     else console.log(data);
// });

// const dirPath = path.join(__dirname,'./folder');
// fs.readdir(dirPath,(err,data)=>{
//     if(err) console.log(err);
//     else console.log(data);
// });

// fs.rmdir('./folder/folder1',(err)=>{
//     if(err) console.log(err);
//     else console.log('success');
// });

// fs.rmdir('./folder',(err)=>{
//     if(err) console.log(err);
//     else console.log('success');
// });

// const dirPath = path.join(__dirname,'./folder');
// fs.rmdir(dirPath,(err)=>{
//     if(err) console.log(err);
//     else console.log('success');
// });

const dirPath = path.join(__dirname,'./folder');
fs.readdir(dirPath,(err,data)=>{
    if(err) console.log(err);
    else{
        data.forEach(file => {
            const filePath = path.join(dirPath,file);
            fs.unlink(filePath,(err)=>{
                if(err) console.log(err);
                else console.log('success');
            });
        });
        fs.rmdir(dirPath,(err)=>{
            if(err) console.log(err);
            else console.log('success');
        });
    }
});
