

#imports script, filename
from sys import argv
script, filename = argv

#sets line to open filename, then sets line to read line
line = open(filename)
line = line.read()

#sets ln to length of line, then sets first to first half of line
#and second to second half of line
ln = len(line)
first = line[:ln/2]
second = line[ln/2+1:]

#sets second to reversed second, then sets first to reversed first
second = second[::-1]
first = first[::-1]

#sets middle to middle of line, then if first and second are the same
#and line is the same as reversed line, print yes, otherwise print no
middle = line[ln/2]
if first == second and line == line[::-1]:
    print "Yes"
else:
    print "No"
