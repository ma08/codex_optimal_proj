

import sys

for line in sys.stdin:
    X, Y = [int(x) for x in line.split()]
    if X * 2 == Y or X * 4 == Y:
        print('Yes')
    else:
        print('No')