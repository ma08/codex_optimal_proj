#!/bin/bash

# Bash script to check for syntax errors in all .sh files in a directory
#
# Usage:
# ./file.sh [directory]
#
# Example:
# ./file.sh /path/to/bash/scripts

if [ -z "$1" ]
then
    echo "Usage: $0 [directory]"
    exit 1
fi

for file in $(find $1 -name '*.sh')
do
    shellcheck -x $file
done
