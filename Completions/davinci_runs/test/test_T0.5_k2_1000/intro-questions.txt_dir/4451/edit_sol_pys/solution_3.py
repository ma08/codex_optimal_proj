#!/bin/bash

# This script will create a new file and add some text to it

echo "Enter the filename to create: "
read FILE

touch $FILE

echo "Enter some text to add to the file: "
read TEXT

echo $TEXT >> $FILE

echo "Here is the text in the file:"
cat $FILE
