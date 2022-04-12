#!/bin/bash
# input_dir="davinci_runs/test/intro-questions.txt_dir"
function echo_ts
{
	echo $1 | ts
}
input_dir="$1"
COUNTER=$(( 0 ))
LIMIT=$(( 1001 ))
# CONTINUE_FROM=$(( 0 ))
CONTINUE_FROM=$(( 4112 ))

echo "---continuing----"

temp="$2"
k="$3"
sleep_time="$4"

echo_ts "Running EDIT API (second stage) for "
echo_ts "input directory $input_dir"
echo_ts "temperature  T2 $temp"
echo_ts "k  K2 $k"
echo_ts "sleep_time $sleep_time"
for question in $input_dir/*/codex_solutions.json; do
    arrIN=(${question//\// })
    num=${arrIN[-2]} 
    num_question=$(expr $num+0)
    if (( num_question < CONTINUE_FROM )); then
        continue 
    fi
    echo_ts "completed: $COUNTER, next question: $question"
    out_dir=$input_dir/$num
    echo_ts "$num  $out_dir"
    # echo_ts $question
    python3 run_edit_module.py $question $out_dir $temp $k $sleep_time 2>&1 
    (( COUNTER++ ))
    echo_ts "completed: $COUNTER, completed question: $question"
    # echo $question $out_dir $num $COUNTER
    if (( COUNTER >= LIMIT )); then
        exit 1
    fi
done

#Write a function to echo input with timestamp...