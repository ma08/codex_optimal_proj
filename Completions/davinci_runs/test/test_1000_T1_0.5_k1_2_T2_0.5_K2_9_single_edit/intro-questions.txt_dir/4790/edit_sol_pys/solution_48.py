
import sys

#function to find the number of stones in each pile
def get_stones(s):
    #count the number of white stones
    w = s.count('W')
    #count the number of black stones
    b = s.count('B')
    #return the number of white stones and black stones
    return w, b
import math

#number of test cases
t = int(input())

#iterate through test cases
for i in range(t):
    #get the string to check
    s = input()
    w, b = get_stones(s)
    #if the number of black and white stones are equal, then we can balance them
    if w == b:
        print(1)
    #otherwise, we cannot balance them
    else:
        print(0)
