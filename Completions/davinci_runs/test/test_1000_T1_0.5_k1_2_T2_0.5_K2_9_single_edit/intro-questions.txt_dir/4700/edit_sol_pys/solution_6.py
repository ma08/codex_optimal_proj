

import sys

n,m = [int(i) for i in input().split()]

h = [int(i) for i in input().split()]

#a = [int(i) for i in input().split() for i in input().split()]

a = []
for i in range(m):
    x,y = [int(j) for j in input().split()]
    a.append(x)
    a.append(y)
    

print(n)
print(m)
print(h)
print(a)
