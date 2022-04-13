

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')
from math import ceil
n = int(input())
a = list(map(int, input().split()))

#a.sort()

#print(a) # 1 2 3 4 5

#s = 0
#for i in range(n):
#    s += a[i]*(i+1) + 1

s = sum([a[i]*(i+1) for i in range(n)]) + n

print(s)
print(*[i+1 for i in range(n)])
