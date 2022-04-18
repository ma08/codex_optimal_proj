//fs module
var fs = require('fs');
//readFileSync
console.log(fs.readFileSync('file.js'));
//readFile
fs.readFile('file.js',function(err,data){
	console.log(data)
});
//writeFileSync
fs.writeFileSync('test.txt','test content');
//writeFile
fs.writeFile('test.txt','test content',function(err){
	if(err){
		console.log('write error');
	}
});
//appendFileSync
fs.appendFileSync('test.txt','append content');
//appendFile
fs.appendFile('test.txt','append content',function(err){
	if(err){
		console.log('append error');
	}
});
//unlinkSync
fs.unlinkSync('test.txt');
//unlink
fs.unlink('test.txt',function(err){
	if(err){
		console.log('unlink error');
	}
});
//renameSync
fs.renameSync('file.js','file-rename.js');
//rename
fs.rename('file-rename.js','file.js',function(err){
	if(err){
		console.log('rename error');
	}
});
//mkdirSync
fs.mkdirSync('newdir');
//mkdir
fs.mkdir('newdir',function(err){
	if(err){
		console.log('mkdir error');
	}
});
//rmdirSync
fs.rmdirSync('newdir');
//rmdir
fs.rmdir('newdir',function(err){
	if(err){
		console.log('rmdir error');
	}
});
//readdirSync
console.log(fs.readdirSync('.'));
//readdir
fs.readdir('.',function(err,files){
	if(err){
		console.log('readdir error');
	}else{
		console.log(files);
	}
});
//existsSync
console.log(fs.existsSync('file.js'));
//exists
fs.exists('file.js',function(exists){
	console.log(exists);
});
//statSync
console.log(fs.statSync('file.js'));
//stat
fs.stat('file.js',function(err,stats){
	if(err){
		console.log('stat error');
	}else{
		console.log(stats);
	}
});
//lstatSync
console.log(fs.lstatSync('file.js'));
//lstat
fs.lstat('file.js',function(err,stats){
	if(err){
		console.log('lstat error');
	}else{
		console.log(stats);
	}
});
//linkSync
fs.linkSync('file.js','file-link.js');
//link
fs.link('file.js','file-link.js',function(err){
	if(err){
		console.log('link error');
	}
});
//unlinkSync
fs.unlinkSync('file-link.js');
//unlink
fs.unlink('file-link.js',function(err){
	if(err){
		console.log('unlink error');
	}
});
//readlinkSync
console.log(fs.readlinkSync('file.js'));
//readlink
fs.readlink('file.js',function(err,linkString){
	if(err){
		console.log('readlink error');
	}else{
		console.log(linkString);
	}
});
//symlinkSync
fs.symlinkSync('file.js','file-symlink.js');
//symlink
fs.symlink('file.js','file-symlink.js',function(err){
	if(err){
		console.log('symlink error');
	}
});
//unlinkSync
fs.unlinkSync('file-symlink.js');
//unlink
fs.unlink('file-symlink.js',function(err){
	if(err){
		console.log('unlink error');
	}
});
//realpathSync
console.log(fs.realpathSync('file.js'));
//realpath
fs.realpath('file.js',function(err,resolvedPath){
	if(err){
		console.log('realpath error');
	}else{
		console.log(resolvedPath);
	}
});
//truncateSync
fs.truncateSync('file.js',20);
//truncate
fs.truncate('file.js',20,function(err){
	if(err){
		console.log('truncate error');
	}
});
//ftruncateSync
fs.ftruncateSync(1,20);
//ftruncate
fs.ftruncate(1,20,function(err){
	if(err){
		console.log('ftruncate error');
	}
});
//chownSync
fs.chownSync('file.js',1000,1000);
//chown
fs.chown('file.js',1000,1000,function(err){
	if(err){
		console.log('chown error');
	}
});
//fchownSync
fs.fchownSync(1,1000,1000);
//fchown
fs.fchown(1,1000,1000,function(err){
	if(err){
		console.log('fchown error');
	}
});
//lchownSync
fs.lchownSync('file.js',1000,1000);
//lchown
fs.lchown('file.js',1000,1000,function(err){
	if(err){
		console.log('lchown error');
	}
});
//chmodSync
fs.chmodSync('file.js','755');
//chmod
fs.chmod('file.js','755',function(err){
	if(err){
		console.log('chmod error');
	}
});
//fchmodSync
fs.fchmodSync(1,'755');
//fchmod
fs.fchmod(1,'755',function(err){
	if(err){
		console.log('fchmod error');
	}
});
//lchmodSync
fs.lchmodSync('file.js','755');
//lchmod
fs.lchmod('file.js','755',function(err){
	if(err){
		console.log('lchmod error');
	}
});
//utimesSync
fs.utimesSync('file.js',new Date(),new Date());
//utimes
fs.utimes('file.js',new Date(),new Date(),function(err){
	if(err){
		console.log('utimes error');
	}
});
//futimesSync
fs.futimesSync(1,new Date(),new Date());
//futimes
fs.futimes(1,new Date(),new Date(),function(err){
	if(err){
		console.log('futimes error');
	}
});
//fsyncSync
fs.fsyncSync(1);
//fsync
fs.fsync(1,function(err){
	if(err){
	
