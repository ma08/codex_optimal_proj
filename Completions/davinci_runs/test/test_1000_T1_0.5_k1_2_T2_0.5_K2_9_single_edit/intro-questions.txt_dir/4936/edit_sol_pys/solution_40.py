# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

numDays = int(sys.stdin.readline())
temp = sys.stdin.readline().split()

minTemp = 100
minDay = 0
for i in range(0,numDays-2):
    if int(temp[i])+int(temp[i+1])+int(temp[i+2]) < minTemp:
        minTemp = int(temp[i])+int(temp[i+1])+int(temp[i+2])
        minDay = i+1

print(minDay, temp[minDay], end="")
