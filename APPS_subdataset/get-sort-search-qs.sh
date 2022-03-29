#!/bin/bash
# It is assumed that the train and test folders from the APPS dataset is in the same directory as this script

mkdir train-questions
mkdir test-questions

# For sort-related questions, we select questions that contain the word "sort" or "index"
grep -rl sort ./train --include=\*.txt > ./train-questions/has-sort-text.txt
grep -rl index ./train --include=\*.txt > ./train-questions/has-index-text.txt
grep -rl sort ./test --include=\*.txt > ./test-questions/has-sort-text.txt
grep -rl index ./test --include=\*.txt > ./test-questions/has-index-text.txt

# For search-related questions, we select questions that contain the word "search", "retriev", and "compar"
grep -rl search ./train --include=\*.txt > ./train-questions/has-search-text.txt
grep -rl retriev ./train --include=\*.txt > ./train-questions/has-retriev-text.txt
grep -rl compar ./train --include=\*.txt > ./train-questions/has-compar-text.txt
grep -rl search ./test --include=\*.txt > ./test-questions/has-search-text.txt
grep -rl retriev ./test --include=\*.txt > ./test-questions/has-retriev-text.txt
grep -rl compar ./test --include=\*.txt > ./test-questions/has-compar-text.txt


cd train-questions
cat has-index-text.txt >> has-sort-text.txt
awk '!seen[$0]++' has-sort-text.txt > sort-questions.txt
cat has-retriev-text.txt >> has-search-text.txt
cat has-compar-text.txt >> has-search-text.txt
awk '!seen[$0]++' has-search-text.txt > search-questions.txt
rm has-index-text.txt
rm has-sort-text.txt
rm has-retriev-text.txt
rm has-compar-text.txt
rm has-search-text.txt

cd ../test-questions
cat has-index-text.txt >> has-sort-text.txt
awk '!seen[$0]++' has-sort-text.txt > sort-questions.txt
cat has-retriev-text.txt >> has-search-text.txt
cat has-compar-text.txt >> has-search-text.txt
awk '!seen[$0]++' has-search-text.txt > search-questions.txt
rm has-index-text.txt
rm has-sort-text.txt
rm has-retriev-text.txt
rm has-compar-text.txt
rm has-search-text.txt
