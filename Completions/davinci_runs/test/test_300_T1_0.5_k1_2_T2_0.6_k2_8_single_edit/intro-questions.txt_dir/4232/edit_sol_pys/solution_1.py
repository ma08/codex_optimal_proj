import sys
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
a = list(map(int, input().split()))

def check(x):
    ret = 0
    for i in range(1, n):
        ret += min(x, a[i] - a[i-1])
    return ret >= k

while l <= r:
    m = (l+r)//2

    if sum(1 for x in a if x <= m) >= k:
        r = m-1
    else:
        l = m+1

if sum(1 for x in a if x <= l) == k:
    print(l)
else:
    print(-1)
