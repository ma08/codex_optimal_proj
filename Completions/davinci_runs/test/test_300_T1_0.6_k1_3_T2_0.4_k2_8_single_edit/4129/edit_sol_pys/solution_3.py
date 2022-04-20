#!/bin/bash

# This script will fix syntax errors in the current directory

for file in $(find . -type f -name "*.php")
do
	php -l $file
	if [ $? -eq 0 ]
	then
		echo "$file is valid"
	else
		echo "$file is invalid"
		php -l -d display_errors=0 $file | grep -v "No syntax errors detected"
		php -l -d display_errors=0 $file | grep "No syntax errors detected" > /dev/null
		if [ $? -eq 0 ]
		then
			echo "Fixing $file"
			php -l -d display_errors=0 $file | grep -v "No syntax errors detected"
			php -l -d display_errors=0 $file | grep -v "No syntax errors detected" | sed -e 's/ in \/.* on line /: /' > $file.errors
			sed -i -f $file.errors $file
			php -l $file
			if [ $? -eq 0 ]
			then
				echo "$file is valid"
			else
				echo "$file is invalid"
			fi
			rm $file.errors
		fi
	fi
done
