import sys
read = sys.stdin.readline

def solve(n, m, a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    res = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            res += 1
            i += 1
        j += 1
    return res

n, m = list(map(int, read().split()))
a = list(map(int, read().split()))
b = list(map(int, read().split()))
print(solve(n, m, a, b))
