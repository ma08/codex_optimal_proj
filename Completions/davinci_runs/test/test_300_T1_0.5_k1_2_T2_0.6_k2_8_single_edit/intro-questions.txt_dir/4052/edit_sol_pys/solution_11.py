function read(filename)
{
return fs.readFileSync(filename, "utf-8");
}

function write(filename, contents)
{
return fs.writeFileSync(filename, contents, "utf-8");
}

function readJSON(filename)
{
return JSON.parse(read(filename));
}

function writeJSON(filename, contents)
{
return write(filename, JSON.stringify(contents));
}

function copy(source, target)
{
return fs.createReadStream(source).pipe(fs.createWriteStream(target));
}

function remove(filename)
{
return fs.unlinkSync(filename);
}

function mkdir(dirname)
{
return fs.mkdirSync(dirname);
}
