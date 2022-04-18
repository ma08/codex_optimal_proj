//create a file and write to it
var fs= require('fs');

fs.writeFile('mynewfile3.txt','Hello content!', function(err){
    if(err) throw err;
    console.log('Saved!');
});

//open a file and append to it
fs.appendFile('mynewfile3.txt','This is my text', function(err){
    if(err) throw err;
    console.log('Updated!');
});

//open a file and replace the content
fs.writeFile('mynewfile3.txt','This is my text', function(err){
    if(err) throw err;
    console.log('Replaced!');
});

//delete a file
fs.unlink('mynewfile2.txt', function(err){
    if(err) throw err;
    console.log('File deleted!');
});

//rename a file
fs.rename('mynewfile1.txt', 'myrenamedfile.txt', function(err){
    if(err) throw err;
    console.log('File renamed!');
});
