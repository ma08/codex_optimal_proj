#!/bin/bash
#
# Make a new file with the given name
#

if [ $# -ne 1 ]; then
  echo "Usage: $0 <file_name>"
  exit 1
fi

touch "$1"
chmod +x "$1"
echo "File created: $1"
