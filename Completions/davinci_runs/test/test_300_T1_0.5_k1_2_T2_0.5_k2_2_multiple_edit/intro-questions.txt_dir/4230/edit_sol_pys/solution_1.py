import math

def solve(x, p):
    p.sort()
    if x < p[0]:
        return p[0] - x
    elif x > p[n-1]:
        return x - p[n-1]
    else:
        for i in range(1, n):
            if p[i-1] < x and x < p[i]:
                if abs(p[i-1] - x) < abs(p[i] - x):
                    return p[i-1] - x
                else:
                    return p[i] - x
                break

x = float(input())
n = int(input())
p = list(map(float, input().split()))
print(solve(x, p))
