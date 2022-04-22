

from collections import defaultdict

def solve(n, a):
    d = defaultdict(set)
    for i in range(1, n + 1):
        d[a[i][0]].add(i)
        d[a[i][1]].add(i)
    start = 1
    for i in range(1, n + 1):
        if len(d[i]) == 1:
            start = i
            break
    res = []
        if start == 0:
            break
        res.append(start)
        next = a[start][0] if a[start][0] != res[-1] else a[start][1]
        a[start] = []
        start = next
    return ' '.join(map(str, res))

n = int(input())
a = defaultdict(list)
for i in range(n):
    a[i + 1] = list(map(int, input().split()))
print(solve(n, a))
