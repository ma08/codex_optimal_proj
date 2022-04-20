#!/bin/bash

# This script is used to fix syntax errors in the files.
#
# Author: Yuxiang Chen
# Date: 02/26/2019

# Fix syntax errors in the files.
for file in "$@"
do
    # Check whether the file exists.
    if [ ! -f "$file" ]; then
        echo "$file does not exist."
        continue
    fi

    # Check whether the file is empty.
    if [ ! -s "$file" ]; then
        echo "$file is empty."
        continue
    fi

    # Check whether the file is a text file.
    if file "$file" | grep -q "text"; then
        echo "$file is a text file."
    else
        echo "$file is not a text file."
        continue
    fi

    # Check whether the file has syntax errors.
    if grep -q "^$" "$file"; then
        echo "$file has syntax errors."
        sed -i '/^$/d' "$file"
        echo "Syntax errors in $file are fixed."
    else
        echo "$file has no syntax errors."
    fi
done
