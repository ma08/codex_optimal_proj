
import sys

#number of test cases
t = int(raw_input())

#iterate through test cases
for i in range(t):
    #get the string to check
    s = raw_input()
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
