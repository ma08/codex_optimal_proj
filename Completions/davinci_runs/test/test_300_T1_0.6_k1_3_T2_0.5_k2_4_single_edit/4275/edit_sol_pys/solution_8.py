

import sys

# Get Inputs
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

# Check if s2 is substring of s1
if s2 in s1:
    print('Yes') # Print Yes if true
else:
    print('No') # Print No if false
