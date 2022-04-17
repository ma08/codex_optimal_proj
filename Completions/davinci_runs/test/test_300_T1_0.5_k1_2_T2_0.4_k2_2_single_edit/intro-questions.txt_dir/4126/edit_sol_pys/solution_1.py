

#imports script, filename
from sys import argv
script, filename = argv

#sets txt to open filename
txt = open(filename)

#sets line to read txt and strips newlines
line = line.rstrip()
line = txt.read()

#sets ln to length of line
ln = len(line)

#sets first to first half of line
first = line[:ln/2]

#sets second to second half of line
second = line[ln/2:]

#sets first and second to reversed first and second
first = first[::-1] 
second = second[::-1] 

#sets middle to middle of line
middle = line[ln/2]

#if first and second are the same and line is the same as reversed line, it's a palindrome.
if first == second and line == line[::-1]:
    print "Yes"
else:
    print "No"
