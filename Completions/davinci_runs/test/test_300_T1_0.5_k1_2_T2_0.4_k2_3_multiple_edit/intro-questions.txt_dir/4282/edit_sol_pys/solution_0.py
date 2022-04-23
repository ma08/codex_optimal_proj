
from collections import defaultdict, deque

def solve(n, a):
    res = deque()
    v = [0] * (n + 1)
    q = deque()
    q.append(1)
    v[1] = 1
    while q:
        cur = q.popleft()
        res.append(cur)
        for i in range(2):
            if not v[a[cur][i]]:
                v[a[cur][i]] = 1
                q.append(a[cur][i])
    res.append(1)
    return ' '.join(map(str, res))

n = int(input())
a = defaultdict(list)
for i in range(n):
    a[i + 1] = list(map(int, input().split()))
print(solve(n, a))
