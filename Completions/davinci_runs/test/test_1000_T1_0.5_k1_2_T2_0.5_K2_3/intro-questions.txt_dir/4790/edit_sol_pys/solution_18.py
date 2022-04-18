import sys
import math

#number of test case
t = int(input())

#iterate through test cases
for i in range(t):
    #get the string to check
    s = input()
    #count the number of white stones
    w = s.count('W')
    #count the number of black stones
    b = s.count('B')
    #if the number of black and white stones are equal, then we can balance them
    if w == b:
        print(1)
    #otherwise, we cannot balance them
    else:
        print(0)
