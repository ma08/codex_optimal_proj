#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./file.sh [filename]"
    exit 1
fi

if [ -f $1 ]; then
    echo "File $1 exists"
    if [ -w $1 ]; then
        echo "File $1 has write permission"
    fi
else
    echo "File $1 does not exist"
fi

exit 0
