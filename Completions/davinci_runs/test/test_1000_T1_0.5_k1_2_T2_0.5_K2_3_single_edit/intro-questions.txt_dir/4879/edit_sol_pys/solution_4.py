

import sys

# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()
# c = sys.stdin.readline().strip()

a = 'North'
b = 'East'
c = 'North'



def get_index(d):
    return directions.index(d)
directions = ['North', 'South', 'East', 'West']

if a == c:
    print("No")
else:
    i = get_index(a)
    j = get_index(b)
    k = get_index(c)
    if (i + 1) % 4 == k or (i + 2) % 4 == k:
        print("Yes")
    else:
        print("No")
