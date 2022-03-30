#!/bin/bash
# It is assumed that the train and test folders from the APPS dataset is in the same directory as this script

# mkdir train-questions
# mkdir test-questions

# For introductory questions, we select questions with
# "introductory" level of difficulty detailed in each
# question's metadata.json
grep -rl introductory ./train --include=metadata.json > ./train-questions/intro-questions.txt
grep -rl introductory ./test --include=metadata.json > ./test-questions/intro-questions.txt
