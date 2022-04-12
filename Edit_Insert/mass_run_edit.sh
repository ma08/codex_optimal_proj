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
    python3 run_edit_module.py $question $out_dir 2>&1 
    (( COUNTER++ ))
    echo_ts "completed: $COUNTER, completed question: $question"
    # echo $question $out_dir $num $COUNTER
    if (( COUNTER >= LIMIT )); then
        exit 1
    fi
done