
from collections import defaultdict

def solve(n, a):
    d = defaultdict(list)
    for i in range(n):
        d[a[i][0]].append(i)
        d[a[i][1]].append(i)
    start = 1
    for i in range(n):
        if len(d[i]) == 1:
            start = i
            break
    res = []
    for i in range(n + 1):
        res.append(start)
        start = a[start][0] if a[start][0] != res[-1] else a[start][1]
    return ' '.join(map(str, res))

n = int(input())
a = defaultdict(list)
for i in range(n):
    a[i] = list(map(int, input().split()))
print(solve(n, a))
