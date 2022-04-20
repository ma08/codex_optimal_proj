import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

if a[m-1] >= sum(a)/(4*m) and a[m-1] > 0:
    print("Yes")
else:
    print("No")
