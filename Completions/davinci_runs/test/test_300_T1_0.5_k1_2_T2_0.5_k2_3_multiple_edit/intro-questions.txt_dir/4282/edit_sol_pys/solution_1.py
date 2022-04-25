
from collections import defaultdict, deque

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
    res = deque()
    for i in range(n):
        res.appendleft(start)
        start = a[start][0] if a[start][0] != res[0] else a[start][1]
    return ' '.join(map(str, list(res)))

n = int(input())
a = defaultdict(list)
for i in range(n):
    a[i + 1] = list(map(int, input().split()))
print(solve(n, a))
