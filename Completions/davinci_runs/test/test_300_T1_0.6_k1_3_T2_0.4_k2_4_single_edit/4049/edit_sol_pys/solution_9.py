#!/bin/bash

# This script is used to fix the syntax error in the .sh file

for file in `ls *.sh`; do
	echo $file
	sed -i 's/\r//g' $file
done
