#!/bin/bash
target="$1_dir"
mkdir $target
while IFS= read -r line; do 
    cp -r $line $target
done < "$1"