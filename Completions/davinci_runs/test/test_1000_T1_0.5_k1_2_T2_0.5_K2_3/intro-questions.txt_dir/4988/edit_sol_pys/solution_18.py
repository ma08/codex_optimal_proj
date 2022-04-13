#!/usr/bin/env python
import sys

#number of test cases
T = int(sys.stdin.readline())

#digit array
digits = [1]
#last digit
last = 1

#for each test case
for i in range(T):
	#read in the number
	N = int(sys.stdin.readline())
	#if we need more digits
	if N > len(digits):
		#compute all of the digits
		for j in range(len(digits), N):
			last = last * (j+1)
			digits.append(last % 10)
	#print out the last digit
	print(digits[N-1])
