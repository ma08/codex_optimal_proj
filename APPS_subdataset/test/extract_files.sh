#!/bin/bash
#Usage ./extract_files.sh <file containing paths of input file line by line>
#It is expected that train folder from the APPS dataset is available in the current directory
for input_file in *.txt; do
    target="$input_file"_dir
    # echo $input_file $num
    mkdir $target
    while IFS= read -r line; do 
        arrIN=(${line//\// })
        num=${arrIN[2]}                  #
        # echo ""
        source=test/$num
        echo $source $target/$num;
        # echo $line $target/$num;
        cp -r $source $target
    done < $input_file
done