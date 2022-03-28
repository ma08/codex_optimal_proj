#!/bin/bash
#Usage ./extract_files.sh <file containing paths of input file line by line>
#It is expected that train folder from the APPS dataset is available in the current directory
target="$1_dir"
mkdir $target
while IFS= read -r line; do 
    cp -r $line $target
done < "$1"