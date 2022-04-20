import sys

# Get Input and split
s = sys.stdin.readline().rstrip().split()

# Check if coffee-like
if s[0][1] == s[0][2] and s[1][0] == s[1][1]:
    print('Yes')
else:
    print('No')

# Check if coffee-like
if s1[1] == s1[2] and s2[0] == s2[1]:
    print('Yes')
else:
    print('No')
