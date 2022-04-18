

import sys

def rearrange(n, array):
    array = sorted(array)
    if n%2 == 0:
        t1 = array[:n//2]
        t2 = array[n//2:]
    else:
        t1 = array[:n//2]
        t2 = array[n//2+1:]
    t1.reverse()
    t1 = t1 + t2
    return t1

n = int(input())
array = [int(x) for x in input().split()]

print(*rearrange(n, array))
