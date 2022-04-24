#!/bin/bash

# This is a comment

# This is a variable

MY_MESSAGE="Hello World"

echo $MY_MESSAGE

# This is a function

function hello {
	echo "Hello World"
}

hello

# This is a loop

for i in {1..5}
do
	echo $i
done

# This is a condition

if [ $1 -gt 100 ]
then
	echo Hey that\'s a large number.
	pwd
fi

date

# This is a file test

FILE="test.txt"

if [ -e "$FILE" ]
then
	echo "$FILE exists"
else
	echo "$FILE does not exist"
fi

# This is a read from a file

cat $FILE

# This is a command line argument

echo $1 $2 $3 ' > echo $1 $2 $3'

# This is an array

args=("$@")

# This is a for loop

for i in "${args[@]}"
do
	echo $i
done

# This is a while loop

COUNTER=0

while [ $COUNTER -lt 10 ]
do
	echo The counter is $COUNTER
	let COUNTER=COUNTER+1
done

# This is a function

function quit {
	exit
}

function hello {
	echo Hello!
}

hello

quit

echo foo
