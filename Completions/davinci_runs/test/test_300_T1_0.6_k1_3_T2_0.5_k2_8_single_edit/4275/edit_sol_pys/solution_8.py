import sys

# Get Input
s = sys.stdin.readline().rstrip()

# Split Input
s1 = s[0:3]
s2 = s[3:6]

# Check if coffee-like
if s1[1] == s1[2] and s2[0] == s2[1]:
    print('Yes')
else:
    print('No')


import sys
