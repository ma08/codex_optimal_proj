#!/bin/bash

filename=$1

if [ -f $filename ]
then
	echo "$filename is a regular file."
elif [ -d $filename ]
then
	echo "$filename is a directory."
else
	echo "$filename is something other than a regular file or directory."
fi
ls -l $filename
