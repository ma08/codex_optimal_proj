#!/bin/bash
#usage: ./mass_davinci_run.sh "test"/"train"
# test_or_train="$1"
function echo_ts
{
	echo $1 | ts
}

COUNTER=$(( 0 ))
LIMIT=$(( 1500 ))
CONTINUE_FROM=$(( 0 ))

# input_set=train/intro-questions.txt
input_dir="$1"

temp="$2"
k="$3"
sleep_time="$4"

# input_dir="$input_set"_dir
echo_ts "Runnin completion API (first stage) for "
echo_ts "input directory $input_dir"
echo_ts "temperature  T1 $temp"
echo_ts "k  K1 $k"
echo_ts "CONTINUE_FROM  $CONTINUE_FROM"
echo_ts "LIMIT $LIMIT"
echo_ts "sleep_time $sleep_time"

# for input_set in $test_or_train/*.txt; do 

# echo input_directory $input_dir

for question in $input_dir/*/question.txt; do
    arrIN=(${question//\// })
    num=${arrIN[2]}                  #
    echo_ts $num
    num_question=$(expr $num+0)
    #echo_ts $num_question
    if (( num_question <= CONTINUE_FROM )); then
        continue 
    fi
    echo_ts "completed: $COUNTER, next question: $question"
    # echo question $question


    out_dir=davinci_runs/test_T1_"$temp"_K1_"$k"/$num
    echo_ts "output directory: $out_dir"
    #continue
    mkdir -p $out_dir
    # echo out_directory $out_dir

    # echo num $num
    # echo $question $out_dir $num

    python3 run_davinci.py $question $out_dir $temp $k $sleep_time 2>&1 
    #python3 $out_dir/gen_code_out.py > $out_dir/out_of_gen_code.txt 2>&1 &

    (( COUNTER++ ))
    echo_ts "completed: $COUNTER, completed question: $question"
    # echo $question $out_dir $num $COUNTER
    if (( COUNTER >= LIMIT )); then
        exit 1
    fi


done
# done

