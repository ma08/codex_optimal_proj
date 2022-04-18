

import sys

# Get Input and Split
s = sys.stdin.readline().rstrip().split()

# Get Values
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

# Check if in range
if a < b < c < d:
    print('Fish Rising')
elif a > b > c > d:
    print('Fish Diving')
elif a == b and c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')
