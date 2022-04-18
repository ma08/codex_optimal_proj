#!/bin/bash

# this script will create a file

echo "Please enter the file name:"
read NAME

echo "Please enter the file extension:"
read EXTENSION

echo "Please enter the file content:"
read CONTENT

echo "$CONTENT" > "$NAME"."$EXTENSION"

echo "Your file is ready"
