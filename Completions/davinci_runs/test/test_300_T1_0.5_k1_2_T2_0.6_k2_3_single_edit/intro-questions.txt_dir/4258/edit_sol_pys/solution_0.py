#!/bin/bash


# This is a comment!

echo Hello World	# This is a comment, too!

echo Our shell name is $BASH

echo Our shell version name is $BASH_VERSION

echo Our home directory is $HOME

echo Our current working directory is $PWD


name=Mark		# No space permitted

echo The name is $name


val=10

echo The value is $val


echo "Enter name : "
read name1 name2 name3

echo "Entered name : $name1, $name2, $name3"


echo -e "Enter name : \c"
read name
echo "Name : $name"


echo "File name : $0"
echo "Command Line Argument 1 : $1"


echo -e "Enter name : \c"
read name
echo "Name : $name"


echo $1 $2 $3 ' > echo $1 $2 $3'


echo Enter some characters : 
read
echo You entered : '"$REPLY"'


echo -n "Enter name : "
read
echo "Name : $REPLY"


read -p 'username : ' user_var
read -sp 'password : ' pass_var
echo
echo username : $user_var
echo password : $pass_var


echo -e "Enter some characters : \c"
read -n 2 var
echo
echo You entered : "$var"


echo -e "Enter some characters : \c"
read -t 2 var
echo
echo You entered : "$var"


echo -e "Enter some characters : \c"
read -n 2 -t 2 var
echo
echo You entered : "$var"


echo -e "Enter some characters : \c"
read -s -n 2 var
echo
echo You entered : "$var"


echo -e "Enter some characters : \c"
read -s -n 2 -t 2 var
echo
echo You entered : "$var"


echo -e "Enter some characters : \c"
read -p 'Username : ' -s -n 2 var1
echo
echo You entered : "$var1"


echo -e "Enter some characters : \c"
read -p 'Username : ' -s -n 2 -t 2 var1
echo
echo You entered : "$var1"


read -p 'Username : ' user_var
read -sp 'Password : ' pass_var
echo
echo "username : $user_var"
echo "password : $pass_var"


#!/bin/bash

echo "Enter the name of the file : "
read file_name

if [ -e $file_name ]
	then 
		echo "$file_name found"
	else
		echo "$file_name not found"
fi



#!/bin/bash

echo "Enter the name of the file : "
read file_name

if [ -e $file_name ]
	then 
		if [ -f $file_name ]
			then
				echo "$file_name is a regular file"
			else
				echo "$file_name is not a regular file"
		fi
	else
		echo "$file_name not found"
fi


#!/bin/bash

echo "Enter the name of the file : "
read file_name

if [ -e $file_name ]
	then 
		if [ -f $file_name ]
			then
				echo "$file_name is a regular file"
			elif [ -d $file_name ]
				then
					echo "$file_name is a directory"
			else
				echo "$file_name is not a regular file"
		fi
	else
		echo "$file_name not found"
fi


















































































































































































































































































































































































































































































