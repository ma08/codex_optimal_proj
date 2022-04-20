

def solve(n, d):
    if n == 1:
        return 2*d[0]
    if n == 2:
        return d[0] * d[1]

    d.sort()
    if d[0] * d[1] < d[-2] * d[-1]:
        return -1
    return d[-1] * d[-2]

t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    print(solve(n, d))