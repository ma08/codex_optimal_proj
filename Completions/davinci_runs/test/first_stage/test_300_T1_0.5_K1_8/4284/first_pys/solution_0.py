

import sys

def solve(k,n,a,b):
    if k<a and k<b:
        return -1
    if k<a:
        return 0
    if a<=b:
        return n
    if k<a+b:
        return 1
    if k==a+b:
        return n-1
    if k==a+b+1:
        return n-2
    return n-2-((k-a-b-2)//(b-1))

q = int(input())
for i in range(q):
    k,n,a,b = map(int,input().split())
    print(solve(k,n,a,b))