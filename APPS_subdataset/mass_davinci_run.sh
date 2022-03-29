#!/bin/bash

test_or_train="test"
COUNTER=$(( 0 ))
LIMIT = $(( 10 ))

for input_set in $test_or_train/*.txt; do 

    input_dir="$input_set"_dir
    # echo input_directory $input_dir

    for question in $input_dir/*/question.txt; do
        arrIN=(${question//\// })
        # echo question $question
        num=${arrIN[2]}                  #


        out_dir=davinci_runs/$input_dir/$num
        mkdir -p $out_dir
        # echo out_directory $out_dir

        # echo num $num
        # echo $question $out_dir $num

        python3 run_davinci.py $question $out_dir 2>&1 
        python3 $out_dir/gen_code_out.py > $out_dir/out_of_gen_code.txt 2>&1 &

        (( COUNTER++ ))
        # echo $question $out_dir $num $COUNTER
        if (( COUNTER >= LIMIT )); then
            exit 1
        fi


    done
done

