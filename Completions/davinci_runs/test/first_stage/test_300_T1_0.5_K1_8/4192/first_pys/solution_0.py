

import sys

# Read the input
d, t, s = map(int, sys.stdin.readline().rstrip().split(' '))

if d / s <= t:
    print('Yes')
else:
    print('No')