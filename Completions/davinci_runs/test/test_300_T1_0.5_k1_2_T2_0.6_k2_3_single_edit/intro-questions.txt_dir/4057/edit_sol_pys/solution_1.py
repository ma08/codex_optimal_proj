import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = [int(i) for i in input().split()]

def solve(n, a):
    if n == 0:
        return 0
    if n == 1:
        return 1
    cnt = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            cnt += 1
    return cnt

print(solve(n, a))
