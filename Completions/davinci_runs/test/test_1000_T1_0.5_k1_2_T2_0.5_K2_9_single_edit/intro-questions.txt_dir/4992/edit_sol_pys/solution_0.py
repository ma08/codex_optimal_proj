
import sys,string
n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n) :
    if ((i+1)%2 == 1 and L[i]%2 == 0) or ((i+1)%2 == 0 and L[i]%2 == 1) :
        L2.append(L[i])
print(*L2)
