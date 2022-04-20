

#imports script, filename
from sys import argv
script, filename = argv

#sets txt to open filename
txt = open(filename)

#sets line to read txt
line = txt.read()

#sets first to first half of line
first = line[:len(line)/2]

#sets middle to middle of line
middle = line[len(line)/2]
#sets second to second half of line
second = line[len(line)/2+1:]

#sets second to reversed second
second = second[::-1]

#sets first to reversed first
first = first[::-1]

#if first and second are the same and line is the same as reversed line
if first == second and line == line[::-1]:
    print "Yes"
else:
    print "No"
