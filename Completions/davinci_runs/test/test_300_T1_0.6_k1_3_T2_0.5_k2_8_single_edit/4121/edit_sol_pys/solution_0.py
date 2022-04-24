#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Usage: $0 <filename>"
else
	if [ -e $1 ]; then
		if [ -d $1 ]; then
			echo "$1 is a directory"
		elif [ -f $1 ]; then
			echo "$1 is a regular file"
		else
			echo "$1 is something else"
		fi
	else
		echo "File $1 does not exist"
	fi
fi
