#!/bin/bash

# This is a simple bash script to create a new file

echo "Enter filename to create:"
read file_name

if [ -f $file_name ]; then
	echo "File '$file_name' already exists"
else
	touch $file_name
	echo "File '$file_name' has been created"
fi
