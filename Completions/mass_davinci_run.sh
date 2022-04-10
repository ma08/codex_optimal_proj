#!/bin/bash
#usage: ./mass_davinci_run.sh "test"/"train"
# test_or_train="$1"
function echo_ts
{
	echo $1 | ts
}
COUNTER=$(( 0 ))
LIMIT=$(( 2640 ))

input_set=train/intro-questions.txt
# for input_set in $test_or_train/*.txt; do 

input_dir="$input_set"_dir
# echo input_directory $input_dir

for question in $input_dir/*/question.txt; do
    echo_ts "completed: $COUNTER, next question: $question"
    arrIN=(${question//\// })
    # echo question $question
    num=${arrIN[2]}                  #


    out_dir=davinci_runs/$input_dir/$num
    echo_ts "output directory: $out_dir"
    mkdir -p $out_dir
    # echo out_directory $out_dir

    # echo num $num
    # echo $question $out_dir $num

    python3 run_davinci.py $question $out_dir 2>&1 
    #python3 $out_dir/gen_code_out.py > $out_dir/out_of_gen_code.txt 2>&1 &

    (( COUNTER++ ))
    echo_ts "completed: $COUNTER, completed question: $question"
    # echo $question $out_dir $num $COUNTER
    if (( COUNTER >= LIMIT )); then
        exit 1
    fi


done
# done

