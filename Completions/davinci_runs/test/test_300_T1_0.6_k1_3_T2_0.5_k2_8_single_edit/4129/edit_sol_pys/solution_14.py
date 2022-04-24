function readFile(file){
	var fs = require('fs');
	var array = fs.readFileSync(file).toString().split("\n");
	for(i in array) {
	    console.log(array[i]);
	}
}

readFile(process.argv[2]);
