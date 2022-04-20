

from collections import defaultdict, deque

def solve(n, a):
    d = defaultdict(list)
    for i in range(n - 1):
        d[a[i][0]].append(a[i][1])
        d[a[i][1]].append(a[i][0])
    q = deque([1])
    visited = set()
    res = ''
    while q:
        x = q.popleft()
        visited.add(x)
        res += str(x) + ' '
        for y in d[x]:
            if y not in visited:
                q.append(y)
                visited.add(y)
    return res

n = int(input())
a = defaultdict(list)
for i in range(n):
    a[i + 1] = list(map(int, input().split()))
print(solve(n, a))
