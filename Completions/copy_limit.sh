#!/bin/bash
#usage: ./mass_davinci_run.sh "test"/"train"
# test_or_train="$1"
function echo_ts
{
	echo $1 | ts
}

COUNTER=$(( 0 ))
LIMIT=$(( 300 ))
CONTINUE_FROM=$(( 0 ))

# input_set=train/intro-questions.txt
input_dir="$1"
out_dir="$2"


# input_dir="$input_set"_dir
echo_ts "input directory $input_dir"
echo_ts "output directory $out_dir"
echo_ts "sleep_time $sleep_time"

# for input_set in $test_or_train/*.txt; do 

# echo input_directory $input_dir

for question in $input_dir/*/; do
    echo_ts "completed: $COUNTER, next question: $question"
    # echo question $question


    #continue
    mkdir -p $out_dir
    cp -r $question "$out_dir"

    (( COUNTER++ ))
    echo_ts "completed: $COUNTER, completed question: $question"
    # echo $question $out_dir $num $COUNTER
    if (( COUNTER >= LIMIT )); then
        exit 1
    fi


done
# done

