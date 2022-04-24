#!/bin/bash

# Author: Michael Ambrus (ambrmi09@gmail.com)
# 2013-05-19

if [ -z $FILE_SH ]; then

FILE_SH="file.sh"

# Returns the file-type of a file
#
# $1 - File to get file-type of
function file_type() {
	file --mime-type "${1}" | awk '{print $NF}'
}

source s3.ebasename.sh
if [ "$FILE_SH" == $( ebasename $0 ) ]; then
	#Not sourced, do something with this.

	FILE_SH_INFO=${FILE_SH}
	source .src.ui..file.sh

	file "$@"

	exit $?
fi

fi
