import sys
import os
import subprocess


argvs = sys.argv
argc = len(argvs)

f = open(argvs[1])

line = f.readline()

while line:
    print(line.strip())
    line = f.readline()

f.close()
