
import sys

def solve(n, a):
    a.sort()
    if n == 1:
        return a[0]
    if n == 2:
        return a[1]
    return max(a[0] * a[1] * a[2], a[0] * a[1] * a[n-1])

q = int(input())
for query_number in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
