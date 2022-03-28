#!/bin/bash
#Usage example ./get_wc.sh sort-questions.txt_dir > word_counts/sort-quesitons_wc.txt
input_dir="$1"
echo $input_dir
for question in $input_dir/*/question.txt; do
    wc -w $question 
done