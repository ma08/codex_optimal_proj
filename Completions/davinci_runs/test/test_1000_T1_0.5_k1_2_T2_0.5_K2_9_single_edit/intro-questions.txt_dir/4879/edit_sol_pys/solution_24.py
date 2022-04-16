

import sys

# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()
# c = sys.stdin.readline().strip()

a = 'South'
b = 'West'
c = 'East'

directions = ['North', 'South', 'East', 'West']

if a == c:
elif a == b:
    print("No")
    print("No")
else:
    if (directions.index(a) + 1) % 4 == directions.index(c) or (directions.index(a) + 2) % 4 == directions.index(c):
        print("Yes")
    else:
        print("No")
