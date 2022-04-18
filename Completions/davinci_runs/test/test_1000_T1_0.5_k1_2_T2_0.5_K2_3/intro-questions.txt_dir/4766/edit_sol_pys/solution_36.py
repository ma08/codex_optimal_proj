

import re
n = int(input()) # number of lines
for i in range(n): # read each line
    line = input() # read line
    if line.startswith("Simon says "): # if the line starts with "Simon says"
        print(line[11:]) # print the line without "Simon says"
