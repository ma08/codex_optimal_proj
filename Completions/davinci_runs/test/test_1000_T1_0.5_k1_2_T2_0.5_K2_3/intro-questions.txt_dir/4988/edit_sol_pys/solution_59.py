
import sys

#number of test cases
T = int(sys.stdin.readline())

#factorial array
factorials = [1]
#last factorial
last = 1 
#last factorial digits
digits = [1]

#for each test case
for i in range(T):
	#read in the number
	N = int(sys.stdin.readline())
	#if we need more factorials
	if N > len(factorials):
		#compute all of the factorials
		for j in range(len(factorials), N):
			last *= j+1
			digits.append(last % 10)	
	#print out the last digit
	print(digits[N-1])
