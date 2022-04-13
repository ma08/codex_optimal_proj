#!/bin/bash

# file: file.sh

# This script will check if a file exists
# and if it does it will delete it.

# Check if file exists
if [ -e $HOME/Desktop/file.txt ]
then
	# File exists, so delete it
	rm $HOME/Desktop/file.txt
fi
