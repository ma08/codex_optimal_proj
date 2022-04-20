#!/bin/bash

# This script will check if a file exists, and will create it if it doesn't

FILE=/home/chris/Documents/Linux/file

if [ -f "$FILE" ]; then
	echo "File $FILE exists"
else
	echo "File $FILE does not exist"
	touch $FILE
fi
