
# SOLUTION
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = [0] * n
r = [0] * n

# get the left and right k-th max elements
for i in range(1, n):
    l[i] = max(l[i-1], a[i-1])
    r[n-i-1] = max(r[n-i], a[n-i])

ans = [0] * n
for i in range(n):
    if l[i] == max(l[i], r[i]):
        ans[i] = 1
    else:
        ans[i] = 2

print("".join(map(str, ans)))
