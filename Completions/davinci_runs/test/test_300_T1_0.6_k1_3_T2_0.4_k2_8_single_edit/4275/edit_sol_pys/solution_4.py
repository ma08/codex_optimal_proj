

import sys

# Get Inputs
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

# Check if coffee-like and print
if s1[1] == s1[2] and s2[0] == s2[1]: 
    print('Yes')
else:
    print('No')
