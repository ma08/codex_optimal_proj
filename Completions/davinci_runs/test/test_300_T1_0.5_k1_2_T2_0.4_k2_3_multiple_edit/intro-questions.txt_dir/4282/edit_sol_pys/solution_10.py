
from collections import defaultdict

def solve(n, a):
    d = defaultdict(list)
    for i in range(1, n + 1):
        d[a[i][0]].append(i)
        d[a[i][1]].append(i)
    start = 1
    for i in range(1, n + 1):
        if len(d[i]) == 1:
            start = i
            break
    res = []
    for i in range(n):
        res.append(start)
        start = a[start][0] if a[start][0] != res[-1] else a[start][1]
    return ' '.join(map(str, res))

n = int(input())
a = defaultdict(tuple)
for i in range(n):
    a[i + 1] = tuple(map(int, input().split()))
print(solve(n, a))
