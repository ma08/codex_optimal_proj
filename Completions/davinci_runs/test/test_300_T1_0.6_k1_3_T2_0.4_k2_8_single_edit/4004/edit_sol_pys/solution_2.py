import math


def solve(n, m, a):
    for i in range(n):
        a[i] = a[i] / m
    a.sort()
    a.reverse()
    res = 0
    for i in range(n):
        res += a[i] * (math.pow(0.5, i + 1))
    return res


n, m = map(int, input().split())
a = [int(x) for x in input().split()] 
print(solve(n, m, a))
