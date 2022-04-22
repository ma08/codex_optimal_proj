#!/usr/bin/python


from sys import argv
script,f_name = argv
f_obj = open(f_name)

def is_palindrome(line):
    length = len(line)
    if length == 1:
        return True
    elif length == 2:
        return line[0] == line[1]
    else:
        if line[0] == line[length - 1]:
            return is_palindrome(line[1:length - 1])
        else:
            return False

p = is_palindrome(f_obj.read())
if p:
    print "Yes"
else:
    print "No"
