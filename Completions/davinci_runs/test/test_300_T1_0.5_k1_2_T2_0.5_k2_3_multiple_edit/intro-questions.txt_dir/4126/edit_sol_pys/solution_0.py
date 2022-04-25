

#imports script, filename
from sys import argv
script, filename = argv

#sets txt to open filename
txt = open(filename)

#sets line to txt.read()
line = txt.read()

#sets ln to length of line
ln = len(line)

#sets first to first half of line
first = line[:ln/2]

#sets second to second half of line
second = line[ln/2+1:]

#sets middle to middle of line
middle = line[ln/2]

#sets line to reversed line
line = line[::-1]

#if first and second are the same and line is the same as reversed line
if first == second and line == line:
    print "Yes"
else:
    print "No"
