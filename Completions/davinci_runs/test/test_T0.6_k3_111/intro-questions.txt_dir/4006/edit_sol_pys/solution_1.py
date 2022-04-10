#!/bin/bash

# this script is used to create a new file

if [ -f "$1" ]
then
	echo "File '$1' already exists"
else
	touch "$1"
	echo "File '$1' has been created"
fi
