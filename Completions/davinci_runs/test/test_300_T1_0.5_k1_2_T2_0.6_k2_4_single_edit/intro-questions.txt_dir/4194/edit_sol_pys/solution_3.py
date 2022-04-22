import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = list(map(int, input().split()))[::-1]
 
def f(i, s):
    if i == m and s == n:
        return 0
    elif i == m:
        return (10**10)
    else:
        return min(f(i + 1, s), f(i + 1, s + a[i]) + 1)
 
if f(0, 0) == (10**10):
    print(-1)
else:
    print(f(0, 0))
