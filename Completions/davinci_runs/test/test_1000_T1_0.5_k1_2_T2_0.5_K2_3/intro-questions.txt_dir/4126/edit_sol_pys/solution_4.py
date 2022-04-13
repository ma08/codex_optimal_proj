

#imports script, filename
from sys import argv
script, filename = argv

#sets txt to open filename
txt = open(filename)

#sets line to read txt
line = txt.read()

#sets ln to length of line without spaces
ln = len(line.replace(" ", ""))

#sets first to first half of line without spaces
first = line.replace(" ", "")[:ln/2]

#sets second to second half of line without spaces
second = line.replace(" ", "")[ln/2:]

#sets second to reversed second
second = second[::-1][1:]

#sets first to reversed first
first = first[::-1][1:]

#sets middle to middle of line without spaces
middle = line.replace(" ", "")[ln/2:]

#if first and second are the same and line is the same as reversed line
if first == second and line.replace(" ", "") == line.replace(" ", "")[::-1]:
    print "Yes"
else:
    print "No"
