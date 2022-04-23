

from collections import defaultdict, deque

def solve(n, a):
    res = deque()
    v = [0] * (n)
    q = deque()
    q.append(0)
    v[0] = 1
    while q:
        cur = q.popleft()
        res.append(cur)
        for i in range(2):
            if not v[a[cur][i] - 1]:
                v[a[cur][i] - 1] = 1
                q.append(a[cur][i] - 1)
    res.append(0)
    return ' '.join(map(str, res))

n = int(input())
a = defaultdict(list)
for i in range(n):
    a[i + 1] = list(map(int, input().split()))
print(solve(n, a))
