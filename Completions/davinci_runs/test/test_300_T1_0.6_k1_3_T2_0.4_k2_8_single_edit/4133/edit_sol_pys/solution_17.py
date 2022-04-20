#!/bin/bash

# This script is used to fix syntax errors in the pug files

# Fix syntax errors in the pug files
find . -name "*.pug" -exec pug-lint {} \;

# Fix syntax errors in the javascript files
find . -name "*.js" -exec eslint {} \;

# Fix syntax errors in the scss files
find . -name "*.scss" -exec sass-lint {} \;
