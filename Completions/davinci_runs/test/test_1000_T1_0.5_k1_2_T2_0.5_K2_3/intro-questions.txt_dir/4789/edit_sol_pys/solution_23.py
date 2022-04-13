#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:01:28 2019

@author: sarath
"""
#importing fileinput
import fileinput
#reading the input from the file
lines = fileinput.input()

k = int(lines[0])
desks = list(map(int, lines[1:k+1]))
#storing the first line as k and the remaining lines as desks
# Sort the desks in ascending order
desks.sort()
#sorting the desks
# Find the minimum number of passes through the line
# by finding the maximum distance between two adjacent desk numbers.
print(max(desks[i] - desks[i-1] for i in range(1, k+1)))
#printing the maximum distance between any two adjacent desks
