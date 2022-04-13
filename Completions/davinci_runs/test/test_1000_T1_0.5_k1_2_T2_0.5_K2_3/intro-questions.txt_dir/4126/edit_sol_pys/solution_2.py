

#imports script, filename
from sys import argv
script, filename = argv

#sets txt to open filename
txt = open(filename)

#sets line to read txt
line = txt.read()

#sets ln to length of line
ln = len(line)

#sets first to first half of line
first = line[:ln/2]

#sets second to second half of line
second = line[ln/2+1:]

#sets middle to middle of line
middle = line[ln/2]

#sets reversed_line to reversed line
reversed_line = line[::-1]

#sets reversed_first to reversed first
reversed_first = first[::-1]

#sets reversed_second to reversed second
reversed_second = second[::-1]

#if first and second are the same and line is the same as reversed line
if reversed_first == reversed_second and line == reversed_line:
    print "Yes"
else:
    print "No"
