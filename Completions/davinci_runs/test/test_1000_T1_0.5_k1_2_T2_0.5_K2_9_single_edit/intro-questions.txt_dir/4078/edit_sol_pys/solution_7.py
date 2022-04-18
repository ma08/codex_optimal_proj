var fs = require('fs');

fs.readFile('./textfile.txt', function(err, data) {
    if (err) {
        console.log('Error', err);
    } else {
        console.log('Async', data.toString());
    }
})

var data = fs.readFileSync('./textfile.txt');
console.log('Sync', data.toString());

console.log('프로젝트 폴더 안의 textfile.txt 파일을 읽도록 요청했습니다.');
