

from collections import defaultdict, deque

def solve(n, a):
    d = defaultdict(list)
    for i in range(n - 1):
        d[a[i][0]].append(a[i][1])
        d[a[i][1]].append(a[i][0])
    q = deque()
    q.append(1)
    used = [False] * (n + 1)
    used[1] = True
    res = [1]
    while q:
        v = q.popleft()
        for to in d[v]:
            if not used[to]:
                used[to] = True
                res.append(to)
                q.append(to)
    return ' '.join(map(str, res[1:]))

n = int(input())
a = defaultdict(list)
for i in range(n - 1):
    a[i + 1] = list(map(int, input().split()))
print(solve(n, a))
