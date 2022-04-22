#!/bin/bash

#--- file test ---#

# test if file exists

# [-e] file exists
# [-r] readable
# [-w] writable
# [-x] executable
# [-d] directory
# [-s] size is >0 bytes
# [-f] file
# [-L] symbolic link
# [-p] pipe
# [-S] socket

# if test -e /etc/passwd
# then
# 	echo "passwd file exists"
# fi

# if [ -e /etc/shadow ]
# then
# 	echo "shadow file exists"
# fi

# if [ -d /etc/shadow ]
# then
# 	echo "shadow file is a directory"
# fi

# if [ -f /etc/passwd ]
# then
# 	echo "passwd file is a regular file"
# fi

# if [ -r /etc/shadow ]
# then
# 	echo "shadow file is readable"
# fi

# if [ -w /etc/shadow ]
# then
# 	echo "shadow file is writable"
# fi

# if [ -x /etc/shadow ]
# then
# 	echo "shadow file is executable"
# fi

# if [ -s /etc/shadow ]
# then
# 	echo "shadow file has non-zero size"
# fi

# if [ -p /etc/shadow ]
# then
# 	echo "shadow file is a pipe"
# fi

# if [ -L /etc/shadow ]
# then
# 	echo "shadow file is a symbolic link"
# fi

# if [ -S /etc/shadow ]
# then
# 	echo "shadow file is a socket"
# fi

# --- string test ---#

# read -p "Enter your name: " name

# if [ $name == "John" ]
# then
# 	echo "You are John"
# fi

#--- number test ---#

# if [ $# -eq 0 ]
# then
# 	echo "No arguments were passed"
# else
# 	echo "Number of arguments: $#"
# fi

# if [ $# -eq 1 ]
# then
# 	echo "Number of arguments: $#"
# else
# 	echo "No arguments were passed"
# fi

# if [ $# -ne 1 ]
# then
# 	echo "No arguments were passed"
# else
# 	echo "Number of arguments: $#"
# fi

# if [ $# -ge 2 ]
# then
# 	echo "Number of arguments: $#"
# else
# 	echo "No arguments were passed"
# fi

# if [ $# -gt 2 ]
# then
# 	echo "Number of arguments: $#"
# else
# 	echo "No arguments were passed"
# fi

# if [ $# -le 2 ]
# then
# 	echo "Number of arguments: $#"
# else
# 	echo "No arguments were passed"
# fi

# if [ $# -lt 2 ]
# then
# 	echo "No arguments were passed"
# else
# 	echo "Number of arguments: $#"
# fi

#--- combine tests ---#

# if [ -f /etc/shadow -a -w /etc/shadow ]
# then
# 	echo "You have permissions to edit /etc/shadow"
# else
# 	echo "You do NOT have permissions to edit /etc/shadow"
# fi

# if [ -f /etc/shadow -a -w /etc/shadow ]
# then
# 	echo "You have permissions to edit /etc/shadow"
# 	echo "You can edit /etc/shadow"
# else
# 	echo "You do NOT have permissions to edit /etc/shadow"
# 	echo "You cannot edit /etc/shadow"
# fi

# if [ -f /etc/shadow -a -w /etc/shadow ] || [ -f /etc/passwd -a -w /etc/passwd ]
# then
# 	echo "You have permissions to edit /etc/shadow or /etc/passwd"
# else
# 	echo "You do NOT have permissions to edit /etc/shadow or /etc/passwd"
# fi

# if [ -f /etc/shadow -a -w /etc/shadow ] || [ -f /etc/passwd -a -w /etc/passwd ]
# then
# 	echo "You have permissions to edit /etc/shadow or /etc/passwd"
# 	echo "You can edit /etc/shadow or /etc/passwd"
# else
# 	echo "You do NOT have permissions to edit /etc/shadow or /etc/passwd"
# 	echo "You cannot edit /etc/shadow or /etc/passwd"
# fi

# if [ -f /etc/shadow -a -w /etc/shadow ] || [ -f /etc/passwd -a -w /etc/passwd ]
# then
# 	echo "You have permissions to edit /etc/shadow or /etc/passwd"
# elif [ -f /etc/hosts -a -w /etc/hosts ]
# then
# 	echo "You have permissions to edit /etc/hosts"
# else
# 	echo "You do NOT have permissions to edit anything"
# fi







