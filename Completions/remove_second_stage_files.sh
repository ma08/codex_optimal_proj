#!/bin/bash
input_dir="$1"

#Loop over subdirectories in "input_dir" directory and delete "edit_sol_pys" and "codex_edit_solutions.json" in each subdirectory
for question in $input_dir/*/; do
    echo $question
    rm -rf $question/edit_sol_pys
    rm -rf $question/codex_edit_solutions.json
done
