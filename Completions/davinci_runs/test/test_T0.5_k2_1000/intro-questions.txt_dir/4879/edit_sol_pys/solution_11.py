

import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()

a = 'South'
b = 'West'
c = 'East'

directions = ['North', 'South', 'East', 'West']

if a == b:
    print("No")
else:
    j = directions.index(a)
    k = directions.index(b)
    l = directions.index(c)
    if (j + 1) % 4 == l or (j + 2) % 4 == l:
        print("Yes")
    else:
        print("No")
