#!/bin/bash
# input_dir="davinci_runs/test/intro-questions.txt_dir"
function echo_ts
{
	echo $1 | ts
}
input_dir="$1"
COUNTER=$(( 0 ))
LIMIT=$(( 112 ))
for question in $input_dir/*/codex_solutions.json; do
    echo_ts "completed: $COUNTER, next question: $question"
    arrIN=(${question//\// })
    num=${arrIN[-2]} 
    out_dir=$input_dir/$num
    echo_ts "$num  $out_dir"
    # echo_ts $question
    python3 run_edit_module.py $question $out_dir 2>&1 
    (( COUNTER++ ))
    echo_ts "completed: $COUNTER, completed question: $question"
    # echo $question $out_dir $num $COUNTER
    if (( COUNTER >= LIMIT )); then
        exit 1
    fi
done