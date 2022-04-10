#!/bin/bash

# A simple script to create a new file and add text to it.

# Create a new file
touch newfile.txt

# Add text to the file
echo "This is a new file" >> newfile.txt

# Append more text to the file
echo "This is more text" >> newfile.txt

# Show the contents of the file
cat newfile.txt
