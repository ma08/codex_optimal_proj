#!/bin/bash

#This script takes a file as an argument and displays it on the standard output

if [ -z $1 ] || [ ! -e $1 ]
then
  echo "Usage: $0 file"
  exit 1
fi

cat $1
