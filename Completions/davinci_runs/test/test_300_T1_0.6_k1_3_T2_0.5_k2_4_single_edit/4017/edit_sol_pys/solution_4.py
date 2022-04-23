

import sys

# SOLUTION
n = int(input())

if n == 1:
    print(1)
    sys.exit()
a = list(map(int, input().split()))

# check if the array is good
if sum(a) - max(a) == max(a):
    print(1)
    print(a.index(max(a))+1)
else:
    print(0)

"""
Good luck!
"""
