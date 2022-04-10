#!/bin/bash
input_dir="davinci_runs/test/intro-questions.txt_dir"
COUNTER=$(( 0 ))
LIMIT=$(( 200 ))
for question in $input_dir/*/*codex_solutions.json; do
    echo $question
    python3 run_edit_module.py $question 2>&1 
    (( COUNTER++ ))
    # echo $question $out_dir $num $COUNTER
    if (( COUNTER >= LIMIT )); then
        exit 1
    fi
done