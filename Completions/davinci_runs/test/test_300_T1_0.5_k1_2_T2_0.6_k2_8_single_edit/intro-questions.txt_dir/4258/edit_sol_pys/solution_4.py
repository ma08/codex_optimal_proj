var fs = require('fs');

// Sync
console.log(1);
var data = fs.readFileSync('data.txt', {encoding:'utf8'});
console.log(data);

// Async
console.log(2);
fs.readFile('data.txt', {encoding:'utf8'}, function(err, data){
	console.log(3);
	console.log(data);
});
console.log(4);

//
// 파일 읽기
//
// 동기식 읽기
var data = fs.readFileSync('data.txt', {encoding:'utf8'});
console.log(data);

// 비동기식 읽기
fs.readFile('data.txt', {encoding:'utf8'}, function(err, data){
	console.log(data);
});

//
// 파일 쓰기
//
// 동기식 쓰기
//
var data = "Hello World...\n";
fs.writeFileSync('data2.txt', data);

// 비동기식 쓰기
var data = "Hello World...\n";
fs.writeFile('data2.txt', data);

//
// 파일 삭제
//
// 동기식 삭제
fs.unlinkSync('data2.txt');

// 비동기식 삭제
fs.unlink('data2.txt');

//
// 폴더 생성
//
// 동기식 생성
fs.mkdirSync('docs');
fs.mkdirSync('docs/node');

// 비동기식 생성
fs.mkdir('docs');
fs.mkdir('docs/node');

//
// 폴더 삭제
//
// 동기식 삭제
fs.rmdirSync('docs/node');
fs.rmdirSync('docs');

// 비동기식 삭제
fs.rmdir('docs/node');
fs.rmdir('docs');

//
// 파일이동
//
// 동기식 이동
fs.renameSync('data.txt', 'node.txt');

// 비동기식 이동
fs.rename('data.txt', 'node.txt');

//
// 파일 복사
//
// 동기식 복사
fs.copyFileSync('node.txt', 'node2.txt');

// 비동기식 복사
fs.copyFile('node.txt', 'node2.txt');
