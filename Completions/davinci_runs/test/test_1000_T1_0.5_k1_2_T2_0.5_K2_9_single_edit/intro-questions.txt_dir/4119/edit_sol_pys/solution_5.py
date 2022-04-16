#imports
import sys
import math


#input
n,m = map(int,sys.stdin.readline().rstrip().split(" "))
x = list(map(int,sys.stdin.readline().rstrip().split(" ")))
#sort

x.sort()
#var

left = x[0]
right = x[-1]
#output
ans = 0

for i in range(m):
    ans += min(abs(x[i] - left),abs(x[i] - right))
    left = min(left,x[i])
    right = max(right,x[i])

print(ans)
