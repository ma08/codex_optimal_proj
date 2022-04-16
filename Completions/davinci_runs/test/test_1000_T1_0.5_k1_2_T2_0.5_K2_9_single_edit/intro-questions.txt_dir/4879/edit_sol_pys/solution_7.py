

import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()

# a = 'South'
# b = 'West'
# c = 'East'

directions = ['North', 'South', 'East', 'West']

if a == c:
    print("No")
else:
    i = directions.index(a)
    j = directions.index(b)
    k = directions.index(c)
    if (i + 2) % 4 == k or (i + 1) % 4 == k:
        print("Yes")
    else:
        print("No")
