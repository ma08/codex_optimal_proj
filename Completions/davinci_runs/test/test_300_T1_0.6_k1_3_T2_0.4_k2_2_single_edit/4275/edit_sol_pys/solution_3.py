
import sys

# Get Input
s = sys.stdin.readline().rstrip() # rstrip() removes the newline character

# Split Input
s1 = s[0:3] # first three characters
s2 = s[3:6] # last three characters

# Check if coffee-like
if s1[1] == s1[2] and s2[0] == s2[1]:
    print('Yes')
else:
    print('No')
