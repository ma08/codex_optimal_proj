#!/usr/bin/env node

var program = require('commander');
var fs = require('fs');
var path = require('path');
var mkdirp = require('mkdirp');

program
  .version('0.0.1')
  .option('-t, --type [type]', 'Type of file to create')
  .option('-n, --name [name]', 'Name of file to create')
  .parse(process.argv);

if (!program.type) {
  console.error('--type is required');
  process.exit(1);
}

if (!program.name) {
  console.error('--name is required');
  process.exit(1);
}

var type = program.type;
var name = program.name;

var fileType = '';

switch (type) {
  case 'component':
    fileType = 'components';
    break;
  case 'container':
    fileType = 'containers';
    break;
  case 'route':
    fileType = 'routes';
    break;
  case 'reducer':
    fileType = 'reducers';
    break;
  case 'action':
    fileType = 'actions';
    break;
}

var fileName = name + '.' + type + '.js';
var targetPath = path.join(process.cwd(), fileType, fileName);

mkdirp(path.join(process.cwd(), fileType), function (err) {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.writeFile(targetPath, '', function (err) {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    console.log('File created at ' + targetPath);
  });
});
