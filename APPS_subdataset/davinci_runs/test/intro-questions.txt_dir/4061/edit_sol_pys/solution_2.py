#!/usr/bin/env python

import sys

# read in the data 
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

# the answer is the length of s minus the length of the longest common subsequence of s and t
print len(s) - len(lcs(s,t))
