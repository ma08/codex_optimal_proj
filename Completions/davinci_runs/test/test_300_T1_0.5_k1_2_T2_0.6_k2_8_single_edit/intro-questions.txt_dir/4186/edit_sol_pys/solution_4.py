# https://atcoder.jp/contests/abc133/tasks/abc133_a

n = int(input())
a = list(map(int, input().split()))

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ans = 0
for i in d:
    ans += d[i] - 2


# https://atcoder.jp/contests/abc133/tasks/abc133_b
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k]) ** 2
        if dist ** 0.5 == int(dist ** 0.5):
            ans += 1
print(ans)

# https://atcoder.jp/contests/abc133/tasks/abc133_c
l, r = map(int, input().split())

if r - l >= 2019:
    print(0)
else:
    ans = 10**10
    for i in range(l, r):
        for j in range(i+1, r+1):
            ans = min(ans, i*j%2019)
    print(ans)


# https://atcoder.jp/contests/abc133/tasks/abc133_d
n = int(input())
a = list(map(int, input().split()))

b = [0] * n
for i in range(n):
    if i % 2 == 0:
        b[0] += a[i]
    else:
        b[0] -= a[i]

for i in range(1, n):
    b[i] = 2 * a[i-1] - b[i-1]

print(" ".join(map(str, b)))

# https://atcoder.jp/contests/abc133/tasks/abc133_e
from collections import deque

n, k = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)

q = deque([0])
used = [False] * n
used[0] = True

while len(q) > 0:
    x = q.popleft()
    for i in g[x]:
        if not used[i]:
            used[i] = True
            q.append(i)

print("Yes" if used.count(True) == n else "No")
print(ans)
