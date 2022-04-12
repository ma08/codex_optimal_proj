

#imports script, filename
from sys import argv
script, filename = argv

#sets txt to open filename and read it
txt = open(filename)
line = txt.read()

#sets ln to length of line and middle to middle of line
ln = len(line)
middle = line[len(line)/2]

first = line[:ln/2]
first = first[::-1]

#sets second to second half of line and reversed
second = line[ln/2+1:][::-1]

#if first and second are the same and line is the same as reversed line
if first == second and line == line[::-1]:
    print "Yes"
else:
    print "No"
